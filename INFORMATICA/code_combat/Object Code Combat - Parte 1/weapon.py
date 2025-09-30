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
        return f"\nWeapon Info:\n Name:{self.name}\n Damage range: {self.min_damage}-{self.max_damage} "










        