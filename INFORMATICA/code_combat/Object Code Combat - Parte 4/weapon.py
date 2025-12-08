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

    def __init__(self, name: str, min_damage: int, max_damage: int, type: str):
        if not isinstance(name, str):
            raise TypeError("Weapon name must be a string.")
        if name == "":
            raise ValueError("Weapon name cannot be empty.")

        if not isinstance(min_damage, int):
            raise TypeError("min_damage must be an integer.")
        if min_damage < 1:
            raise ValueError("min_damage must be >= 1.")

        if not isinstance(max_damage, int):
            raise TypeError("max_damage must be an integer.")
        if max_damage < min_damage:
            raise ValueError("max_damage must be >= min_damage.")

        if type not in ['melee', 'ranged']:
            raise ValueError("Invalid weapon type. Allowed types are 'melee' or 'ranged'.")

        self.__name = name
        self.__min_damage = min_damage
        self.__max_damage = max_damage
        self.__type = type
    
    def get_damage(self) -> int:
        return randint(self.__min_damage, self.__max_damage)
    
    def __str__(self):
        return f"\nWeapon Info:\n Name: {self.__name}\n Damage range: {self.__min_damage}-{self.__max_damage} "

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Weapon name must be a string.")
        if value == "":
            raise ValueError("Weapon name cannot be empty.")
        self.__name = value

    @property
    def min_damage(self):
        return self.__min_damage

    @min_damage.setter
    def min_damage(self, value: int):
        if not isinstance(value, int):
            raise TypeError("min_damage must be an integer.")
        if value < 1:
            raise ValueError("min_damage must be >= 1.")
        if value > self.__max_damage:
            raise ValueError("min_damage cannot be greater than max_damage.")
        self.__min_damage = value

    @property
    def max_damage(self):
        return self.__max_damage

    @max_damage.setter
    def max_damage(self, value: int):
        if not isinstance(value, int):
            raise TypeError("max_damage must be an integer.")
        if value < self.__min_damage:
            raise ValueError("max_damage must be >= min_damage.")
        self.__max_damage = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value: str):
        if value not in ['melee', 'ranged']:
            raise ValueError("Invalid weapon type. Allowed types are 'melee' or 'ranged'.")
        self.__type = value
