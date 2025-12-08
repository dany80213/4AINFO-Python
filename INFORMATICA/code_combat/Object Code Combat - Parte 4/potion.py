class Potion():
    def __init__(self, name: str, effect, amount, duration=0):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if name == "":
            raise ValueError("Name cannot be empty.")

        if effect not in ["heal", "buff_str", "buff_dex"]:
            raise ValueError("Invalid effect type. Allowed: 'heal', 'buff_str', 'buff_dex'.")

        if not isinstance(amount, int):
            raise TypeError("Amount must be an integer.")
        if amount < 1:
            raise ValueError("Amount must be >= 1.")

        if not isinstance(duration, int):
            raise TypeError("Duration must be an integer.")
        if duration < 0:
            raise ValueError("Duration must be >= 0.")

        self.__name = name
        self.__effect = effect
        self.__amount = amount
        self.__duration = duration

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if value == "":
            raise ValueError("Name cannot be empty.")
        self.__name = value

    @property
    def effect(self):
        return self.__effect
    
    @effect.setter
    def effect(self, value: str):
        if value not in ["heal", "buff_str", "buff_dex"]:
            raise ValueError("Invalid effect type. Allowed: 'heal', 'buff_str', 'buff_dex'.")
        self.__effect = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Amount must be an integer.")
        if value < 1:
            raise ValueError("Amount must be >= 1.")
        self.__amount = value
    
    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def duration(self, value):
        if not isinstance(value, int):
            raise TypeError("Duration must be an integer.")
        if value < 0:
            raise ValueError("Duration must be >= 0.")
        self.__duration = value

    def apply_to(self, target) -> dict:
        if self.__effect == "heal":
            self.__apply_heal(target)
            print({"effect": "heal", "amount": self.__amount, "duration": self.__duration})
        else:
            print({"effect": self.__effect, "amount": self.__amount, "duration": self.__duration})
            stat = "dexterity" if self.__effect == "buff_dex" else "strength"
            self.__apply_buff(target, stat)

    def __apply_heal(self, target):
        if not hasattr(target, "health") or not hasattr(target, "max_health"):
            raise TypeError("Potion not usable on this target.")
        
        if target.health == target.max_health:
            raise ValueError("Potion not usable: target already at max health.")
        
        # usa il setter di Player.health che si aspetta (amount, source)
        target.health = (self.__amount, self)

    def __apply_buff(self, target, stat):
        if not hasattr(target, stat):
            raise TypeError(f"Target does not have attribute '{stat}'.")

        for buff in target.buffs:
            if buff[0] == stat:
                raise ValueError(f"{stat} buff already in use")

        setattr(target, stat, getattr(target, stat) + self.__amount)
    
    def __str__(self):
        return f"Potion {self.__effect} + {self.__amount}"
