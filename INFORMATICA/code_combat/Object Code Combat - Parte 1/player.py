from random import randint
import json
from weapon import Weapon

class Player:
    def __init__(self,name: str,max_health : int,strength: int,dexterity:int):
        self.name = name
        self.max_health = max_health if max_health >= 1 else 1
        self.health  = self.max_health
        self.strength = strength if strength >= 1 and strength <= 20 else randint(1,20)
        self.dexterity = dexterity if dexterity >= 1 and dexterity <= 20 else randint(1,20)
        self.weapon = None

    
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
            
            weapon_type = "ranged" if self.dexterity > self.strength else "melee"
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
    
    def equip(self,weapon : Weapon) -> None:
        self.weapon = weapon

    def modifier(self,value:int) -> int:
        return (value -10) // 2
    
    def is_alive(self) -> bool:
        return self.health > 0 
    
    def take(self,damage: int) -> int: 
        self.health -= damage if (self.health - damage) >= 0 else self.health 
        return self.health
    
    def attack(self,enemy: "Player") -> int:
        if self.weapon is None:
            enemy.take(1)
            print(f"{self.name} attacca {enemy.name} e infligge 1  danno!")
            print(enemy)
        else:
            modifier_value = self.dexterity  if self.weapon.type == "ranged" else self.strength
            damage = self.weapon.get_damage() + self.modifier(modifier_value)
            enemy.take(damage)
            print(f"⚔️{self.name} attacca {enemy.name} e infligge {damage}  danni!")
            print(enemy)

    def __str__(self):
        return (f"{self.name} (HP:{self.health}/{self.max_health})")