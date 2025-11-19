class Item:
    def __init__(self,kind,name,power: int):
        if not isinstance(power,int):
            raise TypeError("power must be int")
        if not isinstance(kind,str):
            raise TypeError("kind must be str")
        if not isinstance(name,str):
            raise TypeError("name must be str")
        if power <= 0:
            raise ValueError("power must be greater then 0")
        self.__kind = kind
        self.__name = name
        self.__power = power 

    @property 
    def kind(self):
        return self.__kind
    @property 
    def name(self):
        return self.__name
    @property 
    def name(self):
        return self.__power
        