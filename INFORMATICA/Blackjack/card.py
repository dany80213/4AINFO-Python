class Card():
    def __init__(self,seed,rank):
        if not isinstance(seed,str):
            raise TypeError("The seed must be a string")
        if not isinstance(rank,str):
            raise ValueError("The rank must be a string")
        self.__seed = seed
        self.__rank = rank

    @property
    def seed(self):
        return self.__seed
    
    @property
    def rank(self):
        return self.__rank
    
    @property
    def value(self):
        dict ={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":10,"Queen":10,"King":10,"Ace":11}
        try:
            return dict[self.__rank]
        except IndexError:
            return "Rank not valid."
    
    def __str__(self):
        return f"{self.__rank}{self.__seed}"

