from card import Card

class Hand():
    def __init__(self,cards:list):
        self.__cards = cards

    
    def add_card(self,new_card):
        if not isinstance(new_card,Card):
            raise ValueError("The element to add must be a Card")
        self.__cards.append(new_card)

    @property 
    def cards(self):
        return self.__cards
    

    def empty(self):
        self.__cards.clear()

    def __str__(self):
        return "\n".join(str(card) for card in self.__cards)



