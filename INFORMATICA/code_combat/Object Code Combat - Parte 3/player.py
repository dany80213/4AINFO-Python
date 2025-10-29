from random import randint
import json
from weapon import Weapon
from potion import Potion

class Player:
    def __init__(self, name: str, max_health: int, strength: int, dexterity: int):
        self.__name = name
        self.__max_health = max_health if max_health >= 1 else 1
        self.__health = self.__max_health
        self.__strength = strength if strength <= 1 and  strength <= 20 else randint(1, 20)
        self.__dexterity = dexterity if dexterity <= 1 and  dexterity <= 20 else randint(1, 20)
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
        if isinstance(info[1], Potion):
            self.__health += info[0]
        else:
            print("La salute può essere modificata solo tramite un oggetto Potion.")
    @property
    def strength(self):
        return self.__strength
    
    @strength.setter
    def strength(self,value):
        self.__strength -= value

    @property
    def dexterity(self):
        return self.__dexterity
    
    @dexterity.setter
    def dexterity(self,value):
        self.__dexterity -= value


    @property
    def weapon(self):
        return self.__weapon
    
    @property
    def potions(self):
        return self.__potions
    
    @potions.setter
    def potions(self,new_el):
        if isinstance(new_el, Potion):
            if len(self.__potions) <=2:
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
        self.__weapon = weapon

    def modifier(self, value: int) -> int:
        return (value - 10) // 2
    
    def is_alive(self) -> bool:
        return self.__health > 0 
    
    def __take(self, damage: int) -> int: 
        self.__health -= damage if (self.__health - damage) >= 0 else self.__health 
        return self.__health
    
    def attack(self, enemy: "Player") -> int:
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
            print(self)
            print(self.__potions)
    
    def tick_buffs(self):
        for buff in self.__buffs:
            if buff[2] > 0:
                buff[2] -= 1
            else:
                print(self.__buffs)
                setattr(self,buff[0],buff[1])
                self.__buffs.remove(buff)
    
    def __calculate_damage(self):
        weapon_damage = self.__weapon.min_damage
        modifier_value = self.__dexterity if self.__weapon.type == "ranged" else self.__strength
        return weapon_damage + self.modifier(modifier_value)
    
    def __add_buff(self,stat:str,amount:int,duration:int):
        self.__buffs.append([stat,amount,duration])


    
    def use_potion(self,p:"Potion") -> dict:
        p.apply_to(self)
        self.__potions.remove(p)

    def should_use_potion(self,enemy: "Player"):
        danno_atteso = (enemy.weapon.min_damage + enemy.weapon.max_damage) / 2
        if any(buff.effect == "heal" for buff in self.__potions):
            healing_potions = [potion for potion in self.__potions if potion.effect == "heal"]
            print(healing_potions)
            if healing_potions:
                best_potion = max(healing_potions, key=lambda x :x.amount)
                print(best_potion)
                if self.__health < ((35*self.__max_health)/100) or best_potion.amount + self.__health <= danno_atteso:
                    print("OK")
                    self.use_potion(best_potion)
        buffs_potions = [potion for potion in self.__potions if potion.effect in ['buff_str','buff_dex']]
        if buffs_potions:
            best_potion = max(buffs_potions, key=lambda x: x.amount) 
            if not  self.__buffs and enemy.__health >= ((50*enemy.__max_health)/100):
                self.use_potion(best_potion)
                effect = "dexterity" if best_potion.effect == "buff_dex" else "strength"
                self.__add_buff(effect,best_potion.amount,best_potion.duration)

        

    def __str__(self):
        return (f"{self.__name} (HP:{self.__health}/{self.__max_health})")