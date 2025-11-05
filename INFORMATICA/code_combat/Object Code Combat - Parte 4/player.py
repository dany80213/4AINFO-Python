from random import randint
import json
from weapon import Weapon
from potion import Potion

class Player:
    def __init__(self, name: str, max_health: int, strength: int, dexterity: int):
        self.__name = name
        if max_health <= 0 or strength <= 0 or dexterity <= 0:
            raise ValueError("max_health, strength, and dexterity must be greater than 0.")
        self.__max_health = max_health 
        self.__health = self.__max_health
        self.__strength = strength
        self.__dexterity = dexterity 
        self.__weapon = None
        self.__buffs = list()
        self.__potions = list()

    @property
    def name(self):
        return self.__name

    @property
    def max_health(self):
        return self.__max_health

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, info):
        try:
            amount, source = info
        except Exception:
            print("Formato non valido per la modifica della salute.")
            return
        if isinstance(source, Potion):
            # clamp a [0, max_health]
            self.__health = max(0, min(self.__max_health, self.__health + amount))
        else:
            print("La salute può essere modificata solo tramite un oggetto Potion.")

    @property
    def strength(self):
        return self.__strength
    
    
    @dexterity.setter
    def dexterity(self,value):
        self.__dexterity += value


    @property
    def weapon(self):
        return self.__weapon
    
    @property
    def potions(self):
        return self.__potions
    
    @potions.setter
    def potions(self,new_el):
        if isinstance(new_el, Potion):
            if len(self.__potions) <3:
                self.__potions.append(new_el)
            else: 
                print("Impossibile aggiungere la pozione, quantità massima raggiunta")
        else:
            print("L'elemento non è un' instanza di una classe")

    def get_weapons(self):
        """
        Retrieves a list of weapons from a JSON file filtered by the given weapon type.

        Args:
            weapon_type (str): The type of weapons to retrieve ("melee" or "ranged").

        Returns:
            list: A list of Weapon instances matching the specified type.

        Raises:
            FileNotFoundError: If the weapon.json file is not found.
        """

        try:
            with open("INFORMATICA/code_combat/Object Code Combat - Parte 1/weapon.json", "r") as file:
                weapons_data = json.load(file)
            
            weapon_type = "ranged" if self.__dexterity > self.__strength else "melee"
            filtered_weapons = [
                Weapon(
                    name=info["name"],
                    min_damage= info["min_damage"],
                    max_damage= info["max_damage"],
                    type= info["type"],
                )
                for info in weapons_data if info["type"] == weapon_type
            ]
            return filtered_weapons
        except FileNotFoundError:
            raise FileNotFoundError("The weapon.json file is missing.")
    
    @weapon.setter
    def weapon(self, weapon: Weapon) -> None:

        if not (hasattr(weapon,"get_damage") and callable(getattr(weapon,"get_damage"))):
            raise TypeError("Object not equipable")
        
        if not hasattr(weapon, "type"):
            raise TypeError("Object not equipable")
        
        self.__weapon = weapon

    @property
    def buffs(self):
        return self.__buffs

    def modifier(self, value: int) -> int:
        return (value - 10) // 2
    
    def is_alive(self) -> bool:
        return self.__health > 0 
    
    def __take(self, damage: int) -> int:
        try:
            if not isinstance(damage, int):
                raise TypeError("Damage must be an integer.")
        except TypeError as e:
            print(f"Error occurred: {e}")
        try:
            if damage < 0:
                raise ValueError("Damage cannot be negative.")
        except ValueError as e:
            print(f"Error occurred: {e}")
        self.__health -= damage if (self.__health - damage) >= 0 else self.__health 
    
    def attack(self, enemy: "Player") -> int:
        try:
            if self.__weapon is None:
                enemy.__take(1)
                print(f"{self.__name} attacca {enemy.name} e infligge 1  danno!")
                print(enemy)
            else:
                modifier_value = self.__dexterity if self.__weapon.type == "ranged" else self.__strength
                damage = self.__weapon.get_damage() + self.modifier(modifier_value)
                enemy.__take(damage)
                print(f"⚔️ {self.__name} attacca {enemy.name} e infligge {damage}  danni!")
                print(enemy)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    def tick_buffs(self):
        try:
            for buff in self.__buffs:
                if buff[2] > 0:
                    buff[2] -= 1
                else:
                    print(self.__buffs)
                    setattr(self,buff[0],buff[1])
                    self.__buffs.remove(buff)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    def __calculate_damage(self):
        weapon_damage = self.__weapon.min_damage
        modifier_value = self.__dexterity if self.__weapon.type == "ranged" else self.__strength
        return weapon_damage + self.modifier(modifier_value)
    
    def __add_buff(self,stat:str,amount:int,duration:int):
        self.__buffs.append([stat,amount,duration])


    
    def use_potion(self,p:"Potion") -> dict:
        try:
            if not isinstance(p, Potion):
                raise TypeError("Invalid potion.")
            p.apply_to(self)
            self.__potions.remove(p)
        except Exception as e:
            print(f"Error occurred: {e}")

    def should_use_potion(self,enemy: "Player"):
        try:
            if getattr(enemy, "weapon", None) and hasattr(enemy.weapon, "min_damage") and hasattr(enemy.weapon, "max_damage"):
                danno_atteso = (enemy.weapon.min_damage + enemy.weapon.max_damage) / 2
            else:
                danno_atteso = 1  # fallback se il nemico è disarmato
            if any(pz.effect == "heal" for pz in self.__potions):
                healing_potions = [potion for potion in self.__potions if potion.effect == "heal"]
                if healing_potions:
                    best_potion = max(healing_potions, key=lambda x :x.amount)
                    if self.__health < ((35*self.__max_health)/100) or best_potion.amount + self.__health <= danno_atteso:
                        self.use_potion(best_potion)
            buffs_potions = [potion for potion in self.__potions if potion.effect in ['buff_str','buff_dex']]
            if buffs_potions:
                best_potion = max(buffs_potions, key=lambda x: x.amount) 
                if not self.__buffs and enemy.__health >= ((50*enemy.__max_health)/100):
                    self.use_potion(best_potion)
                    effect = "dexterity" if best_potion.effect == "buff_dex" else "strength"
                    self.__add_buff(effect,best_potion.amount,best_potion.duration)
        except Exception as e:
            print(f"Error occurred: {e}")

    def __str__(self):
        return (f"{self.__name} (HP:{self.__health}/{self.__max_health})")