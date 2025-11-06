from hand import Hand
from card import Card
from deck import Deck,EmptyDeckError

class BlackjackTable():
    def __init__(self):
        self.__player_hand = Hand(list())
        self.__dealer_hand = Hand(list())
        self.__deck = Deck(self.__create_deck_std())
        self.__deck.shuffle()
        
    def __create_deck_std(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = [Card(suit, rank) for suit in suits for rank in ranks]
        return deck
    
    def __calculate_points(self,hand:Hand):
        points = 0
        hand.cards.sort(key=lambda card: card.value)
        for card in hand.cards:
            if points + card.value > 21:
                if card.value == 11:
                    points +=1
                else:
                    points += card.value
            else:
                points += card.value
        return points


    
    def __player_turn(self):
        print(f" Your card:\n{self.__player_hand}")
        print(f"First dealer's card: {self.__dealer_hand.cards[0]}")
        ans = input("Hit(H) Stand(S)?")
        while not ans in ["H","S"]:
            ans = input("You can only choose btw Hit(H) or Stand(S)")
        return ans
    
    def __dealer_turn(self):
        points = self.__calculate_points(self.__dealer_hand)
        if points <=16:
            return "H"
        else:
            return "S"
        
    def is_busted(self,hand:Hand):
        points = self.__calculate_points(hand)
        if points > 21:
            return True
        else:
            return False


        
    
        
    def play_game(self):
        for i in range(2):
            while True:
                try:
                    self.__player_hand.add_card(self.__deck.pick())
                    self.__dealer_hand.add_card(self.__deck.pick())
                    break
                except EmptyDeckError:
                    self.__deck = Deck(self.__create_deck_std())
                    self.__deck.shuffle()

        while self.__player_turn() == "H":
            while True:
                try:
                    self.__player_hand.add_card(self.__deck.pick())
                    break
                except EmptyDeckError:
                    self.__deck = Deck(self.__create_deck_std())
                    self.__deck.shuffle()
            if self.is_busted(self.__player_hand):
                return "Dealer wins, Player busted"
        while self.__dealer_turn() == "H":
            while True:
                try:
                    self.__dealer_hand.add_card(self.__deck.pick())
                    break
                except EmptyDeckError:
                    self.__deck = Deck(self.__create_deck_std())
                    self.__deck.shuffle()
            print(f"Dealer's Cards: \n{self.__dealer_hand}")
            if self.is_busted(self.__dealer_hand):
                return "Player wins, Dealer busted"
        
        if self.__calculate_points(self.__dealer_hand) > self.__calculate_points(self.__player_hand):
            return "Dealer wins!"
        elif self.__calculate_points(self.__dealer_hand) < self.__calculate_points(self.__player_hand):
            return "Player wins!"
        else:
            return "Draw."
        
        



Table = BlackjackTable()

            
print(Table.play_game())
