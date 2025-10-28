class Potion():
    def __init__(self,name:str,effect,amount,duration=None):
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
    def amount(self,value):
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
        if self.__effect == "heal":
            self.__apply_heal(target)
            print({"effect":"heal", "amount":self.__amount, "duration":self.__duration})
        else:
            print({"effect": self.__effect, "amount":self.__amount, "duration":self.__duration})
            self.__apply_buff(target)

    def __apply_heal(self, target):
        if hasattr(target, 'health'):
            target.health = self.__amount

    def __apply_buff(self,target,stat):
        if hasattr(target,stat):
            target.stat = self.__amount
    
    def __str__(self):
        return f"Potion {self.__effect} + {self.__amount}"
    



    



        