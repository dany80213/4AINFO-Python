class Potion():
    def __init__(self,name:str,effect,amount,duration=0):
        self.__name = name
        self.__effect = effect if effect in ["heal","buff_str","buff_dex"] else ""
        self.__amount = amount if amount >= 1 else 1
        self.__duration = duration if duration >= 0 else 0 


    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        self.__name = value if value != "" else self._name

    @property
    def effect(self):
        return self.__effect
    
    @effect.setter
    def effect(self,value:str):
        self.__effect = value if value in ["heal","buff_str","buff_dex"] else self.__effect

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self,value:int):
        self.__amount = value if value >=1 else self.__amount
    
    @property
    def duration(self:int):
        return self.__duration
    
    @duration.setter
    def duration(self,value):
        self.__duration = value if value >= 0 else self.__duration

    def apply_to(self,target) -> dict:
        try:
            if self.__effect == "heal":
                self.__apply_heal(target)
                print({"effect":"heal", "amount":self.__amount, "duration":self.__duration})
            else:
                print({"effect": self.__effect, "amount":self.__amount, "duration":self.__duration})
                stat = "dexterity" if self.__effect == "buff_dex" else "strength"
                self.__apply_buff(target,stat)
        except Exception as e:
            print(f"Error occurred: {e}")

    def __apply_heal(self, target):
        if hasattr(target, 'health'):
            if target.health == target.max_health:
                raise ValueError("Potion not usable")
            target.health = (self.__amount,self)
        else:
            raise TypeError("Potion not usable")

    def __apply_buff(self,target,stat):
        if hasattr(target,stat):
            for buff in target.buffs:
                if buff[0] == stat:
                    raise ValueError(f"{stat} buff  already in use")

            target.stat = self.__amount
    
    def __str__(self):
        return f"Potion {self.__effect} + {self.__amount}"
    



    



        