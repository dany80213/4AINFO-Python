from random import randint

class Weapon:
    """
    Represents a weapon with attributes and functionality to generate random damage values within a specified range.
    
    Attributes:
        name (str): The name of the weapon, e.g., "Two-handed sword".
        min_damage (int): The minimum damage the weapon can deal (≥ 1).
        max_damage (int): The maximum damage the weapon can deal (≥ min_damage).
        type (str): The type of the weapon, either "melee" (close combat) or "ranged" (distance combat).
    
    Methods:
        get_damage() -> int:
            Returns a random integer within the range [min_damage, max_damage].
        
        __str__() -> str:
            Returns a readable string representation of the weapon, including its name and damage range.
    """

    def __init__(self, name: str,min_damage: int,max_damage: int,type:str):
        self.name = name
        self.min_damage = min_damage if min_damage >= 1 else 1
        self.max_damage = max_damage if max_damage >= min_damage else min_damage
        self.type = type if type in ['melee','ranged'] else None
        if self.type is None:
            raise(ValueError("Invalid weapon type. Allowed types are 'melee' or 'ranged'."))
    
    def get_damage(self) -> int:
        return randint(self.min_damage,self.max_damage)
    
    def __str__(self):
        return f"Weapon Info: \n Name:{self.name} \n Damage range: "


class Player:
    def __init__(self,name: str,max_health : int,strength: int,dexterity:int):
        self.name = name
        self.max_health = max_health if max_health >= 1 else 1
        self.health  = self.max_health
        self.strength = strength if strength >= 1 and strength <= 20 else randint(1,20)
        self.dexterity = dexterity if dexterity >= 1 and dexterity <= 20 else randint(1,20)
        self.weapon = None 
    
    def equip(self,weapon : Weapon) -> None:
        self.weapon = weapon

    def modifier(self,value:int) -> int:
        return (value -10) // 2
    
    def is_alive(self) -> bool:
        return self.health > 0 
    
    def take(self,damage: int) -> int: 
        self.health -= damage if (self.health - damage) >= 0 else 0 
        return self.health
    
    def attack(self,enemy: "Player") -> int:
        if self.weapon is None:
            enemy.take(1)
        else:
            enemy.take(self.weapon.get_damage())







        