from random import shuffle

class EmptyDeckError(Exception):
    """Exception in case the deck is Empty"""
    pass

class Deck():
    def __init__(self,cards : list):
        self.__cards = cards

    def shuffle(self):
        shuffle(self.__cards)

    def pick(self):
        if len([self.__cards]) == 0:
            raise EmptyDeckError("The Deck is Empty")
        last_card = self.__cards[-1]
        self.__cards.pop()
        return last_card
    
    def __str__(self):
        return ", ".join(str(card.value) for card in self.__cards)




        