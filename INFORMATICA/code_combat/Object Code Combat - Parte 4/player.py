from random import randint
import json
from weapon import Weapon
from potion import Potion

class Player:
    def __init__(self, name: str, max_health: int, strength: int, dexterity: int):
        if not isinstance(name, str):
            raise TypeError("name must be a string.")
        if max_health <= 0 or strength <= 0 or dexterity <= 0:
            raise ValueError("max_health, strength, and dexterity must be greater than 0.")
        
        self.__name = name
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
        if not isinstance(info, tuple) or len(info) != 2:
            raise TypeError("Formato non valido per la modifica della salute. Atteso: (amount, source).")
        
        amount, source = info

        if not isinstance(source, Potion):
            raise TypeError("La salute può essere modificata solo tramite un oggetto Potion.")
        
        if not isinstance(amount, int):
            raise TypeError("La quantità di modifica della salute deve essere un intero.")

        # clamp a [0, max_health]
        self.__health = max(0, min(self.__max_health, self.__health + amount))


    @property
    def strength(self):
        return self.__strength
    
    @strength.setter
    def strength(self, value):
        if not isinstance(value, int):
            raise TypeError("La forza deve essere un intero.")
        if value < 0:
            raise ValueError("La forza non può essere negativa.")
        self.__strength = value

    @property
    def dexterity(self):
        return self.__dexterity

    @dexterity.setter
    def dexterity(self, value):
        if not isinstance(value, int):
            raise TypeError("La destrezza deve essere un intero.")
        if value < 0:
            raise ValueError("La destrezza non può essere negativa.")
        self.__dexterity = value

    @property
    def weapon(self):
        return self.__weapon
    
    @property
    def potions(self):
        return self.__potions
    
    @potions.setter
    def potions(self,new_el):
        if not isinstance(new_el, Potion):
            raise TypeError("L'elemento non è un'instanza di Potion.")
        if len(self.__potions) >= 3:
            raise ValueError("Impossibile aggiungere la pozione, quantità massima raggiunta (3).")
        self.__potions.append(new_el)

    def get_weapons(self):
        """
        Retrieves a list of weapons from a JSON file filtered by the given weapon type.

        Returns:
            list: A list of Weapon instances matching the specified type.

        Raises:
            FileNotFoundError: If the weapon.json file is not found.
            ValueError: If data in weapon.json is malformed.
        """

        try:
            with open("weapon.json", "r") as file:
                weapons_data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("The weapon.json file is missing.")
        
        if not isinstance(weapons_data, list):
            raise ValueError("weapon.json must contain a list of weapons.")
            
        weapon_type = "ranged" if self.__dexterity > self.__strength else "melee"
        filtered_weapons = []

        for info in weapons_data:
            if not isinstance(info, dict):
                continue
            if info.get("type") != weapon_type:
                continue
            try:
                w = Weapon(
                    name=info["name"],
                    min_damage=info["min_damage"],
                    max_damage=info["max_damage"],
                    type=info["type"],
                )
            except (KeyError, TypeError, ValueError) as e:
                # arma malformata nel json → la salto
                continue
            filtered_weapons.append(w)

        return filtered_weapons
    
    @weapon.setter
    def weapon(self, weapon: Weapon) -> None:
        if not isinstance(weapon, Weapon):
            raise TypeError("Object not equipable: must be a Weapon instance.")
        
        if not (hasattr(weapon,"get_damage") and callable(getattr(weapon,"get_damage"))):
            raise TypeError("Object not equipable: missing get_damage().")
        
        if not hasattr(weapon, "type"):
            raise TypeError("Object not equipable: missing type attribute.")
        
        self.__weapon = weapon

    @property
    def buffs(self):
        return self.__buffs

    def modifier(self, value: int) -> int:
        if not isinstance(value, int):
            raise TypeError("modifier value must be an integer.")
        return (value - 10) // 2
    
    def is_alive(self) -> bool:
        return self.__health > 0 
    
    def __take(self, damage: int) -> int:
        if not isinstance(damage, int):
            raise TypeError("Damage must be an integer.")
        if damage < 0:
            raise ValueError("Damage cannot be negative.")
        # clamp a 0
        self.__health = max(0, self.__health - damage)
        return damage
    
    def attack(self, enemy: "Player") -> int:
        if not isinstance(enemy, Player):
            raise TypeError("enemy must be a Player instance.")
        
        if self.__weapon is None:
            damage = 1
            enemy.__take(damage)
            print(f"{self.__name} attacca {enemy.name} e infligge {damage} danno!")
            print(enemy)
            return damage

        modifier_value = self.__dexterity if self.__weapon.type == "ranged" else self.__strength
        damage = self.__weapon.get_damage() + self.modifier(modifier_value)
        enemy.__take(damage)
        print(f"⚔️ {self.__name} attacca {enemy.name} e infligge {damage} danni!")
        print(enemy)
        return damage
    
    def tick_buffs(self):
        for buff in self.__buffs:
            if buff[2] > 0:
                buff[2] -= 1
            else:
                # buff = [stat, amount, duration]
                stat, amount, _ = buff
                if hasattr(self, stat):
                    setattr(self, stat, getattr(self, stat) - amount)
                self.__buffs.remove(buff)
    
    def __calculate_damage(self):
        if self.__weapon is None:
            raise RuntimeError("No weapon equipped.")
        weapon_damage = self.__weapon.min_damage
        modifier_value = self.__dexterity if self.__weapon.type == "ranged" else self.__strength
        return weapon_damage + self.modifier(modifier_value)
    
    def __add_buff(self,stat:str,amount:int,duration:int):
        if not isinstance(stat, str):
            raise TypeError("stat must be a string.")
        if not isinstance(amount, int) or not isinstance(duration, int):
            raise TypeError("amount and duration must be integers.")
        if duration < 0:
            raise ValueError("duration cannot be negative.")
        self.__buffs.append([stat,amount,duration])

    def use_potion(self,p:"Potion") -> dict:
        if not isinstance(p, Potion):
            raise TypeError("Invalid potion.")
        if p not in self.__potions:
            raise ValueError("Potion not in inventory.")
        p.apply_to(self)
        self.__potions.remove(p)

    def should_use_potion(self,enemy: "Player"):
        if not isinstance(enemy, Player):
            raise TypeError("enemy must be a Player instance.")
        
        if getattr(enemy, "weapon", None) and hasattr(enemy.weapon, "min_damage") and hasattr(enemy.weapon, "max_damage"):
            danno_atteso = (enemy.weapon.min_damage + enemy.weapon.max_damage) / 2
        else:
            danno_atteso = 1  # fallback se il nemico è disarmato

        # Pozioni di cura
        if any(pz.effect == "heal" for pz in self.__potions):
            healing_potions = [potion for potion in self.__potions if potion.effect == "heal"]
            if healing_potions:
                best_potion = max(healing_potions, key=lambda x :x.amount)
                if self.__health < ((35*self.__max_health)/100) or best_potion.amount + self.__health <= danno_atteso:
                    self.use_potion(best_potion)

        # Pozioni buff
        buffs_potions = [potion for potion in self.__potions if potion.effect in ['buff_str','buff_dex']]
        if buffs_potions:
            best_potion = max(buffs_potions, key=lambda x: x.amount) 
            if not self.__buffs and enemy.__health >= ((50*enemy.__max_health)/100):
                self.use_potion(best_potion)
                effect = "dexterity" if best_potion.effect == "buff_dex" else "strength"
                self.__add_buff(effect,best_potion.amount,best_potion.duration)

    def __str__(self):
        return (f"{self.__name} (HP:{self.__health}/{self.__max_health})")
