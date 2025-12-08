from random import randint
import json
from weapon import Weapon

class Player:
    def __init__(self, name: str, max_health: int, strength: int, dexterity: int):
        self.__name = name
        self.__max_health = max_health if max_health >= 1 else 1
        self.__health = self.__max_health
        self.__strength = strength if 1 <= strength <= 20 else randint(1, 20)
        self.__dexterity = dexterity if 1 <= dexterity <= 20 else randint(1, 20)
        self.__weapon = None

    @property
    def name(self):
        return self.__name

    @property
    def max_health(self):
        return self.__max_health

    @property
    def health(self):
        return self.__health

    @property
    def strength(self):
        return self.__strength

    @property
    def dexterity(self):
        return self.__dexterity

    @property
    def weapon(self):
        return self.__weapon

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
            with open("weapon.json", "r") as file:
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
    
    def equip(self, weapon: Weapon) -> None:
        self.__weapon = weapon

    def modifier(self, value: int) -> int:
        return (value - 10) // 2
    
    def is_alive(self) -> bool:
        return self.__health > 0 
    
    def take(self, damage: int) -> int: 
        self.__health -= damage if (self.__health - damage) >= 0 else self.__health 
        return self.__health
    
    def attack(self, enemy: "Player") -> int:
        if self.__weapon is None:
            enemy.take(1)
            print(f"{self.__name} attacca {enemy.name} e infligge 1  danno!")
            print(enemy)
        else:
            modifier_value = self.__dexterity if self.__weapon.type == "ranged" else self.__strength
            damage = self.__weapon.get_damage() + self.modifier(modifier_value)
            enemy.take(damage)
            print(f"⚔️ {self.__name} attacca {enemy.name} e infligge {damage}  danni!")
            print(enemy)

    def __str__(self):
        return (f"{self.__name} (HP:{self.__health}/{self.__max_health})")