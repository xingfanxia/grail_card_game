from random import shuffle
import Card

class Deck():
    def __init__(self):
        self.deck = []
        self.discard_deck = []

        # ATK Cards
        winds = [Card.Attack_Card("wind") for i in range(21)]
        self.deck.extend(winds)
        fires = [Card.Attack_Card("fire") for i in range(21)]
        self.deck.extend(fires)
        earths = [Card.Attack_Card("earth") for i in range(21)]
        self.deck.extend(earths)
        waters = [Card.Attack_Card("water") for i in range(21)]
        self.deck.extend(waters)
        elecs = [Card.Attack_Card("elec") for i in range(21)]
        self.deck.extend(elecs)
        darks = [Card.Attack_Card("dark") for i in range(6)]
        self.deck.extend(darks)

        #Magic Cards
        invincibles = [Card.Magic_Card("light", "invincible") for i in range(11)]
        self.deck.extend(invincibles)

        shields_1 = [Card.Magic_Card("earth", "shield") for i in range(3)]
        self.deck.extend(shields_1)
        shields_2 = [Card.Magic_Card("fire", "shield") for i in range(2)]
        self.deck.extend(shields_2)
        shields_3 = [Card.Magic_Card("elec", "shield") for i in range(2)]
        self.deck.extend(shields_3)
        shields_4 = [Card.Magic_Card("wind", "shield") for i in range(3)]
        self.deck.extend(shields_4)

        exhausts_1 = [Card.Magic_Card("earth", "exhaust") for i in range(1)]
        self.deck.extend(exhausts_1)
        exhausts_2 = [Card.Magic_Card("fire", "exhaust") for i in range(2)]
        self.deck.extend(exhausts_2)
        exhausts_3 = [Card.Magic_Card("water", "exhaust") for i in range(2)]
        self.deck.extend(exhausts_3)
        exhausts_4 = [Card.Magic_Card("wind", "exhaust") for i in range(1)]
        self.deck.extend(exhausts_4)

        poisons_1 = [Card.Magic_Card("earth", "poison") for i in range(1)]
        self.deck.extend(poisons_1)
        poisons_2 = [Card.Magic_Card("wind", "poison") for i in range(1)]
        self.deck.extend(poisons_2)
        poisons_3 = [Card.Magic_Card("water", "poison") for i in range(3)]
        self.deck.extend(poisons_3)
        poisons_4 = [Card.Magic_Card("elec", "poison") for i in range(1)]
        self.deck.extend(poisons_4)

        booms_1 = [Card.Magic_Card("fire", "boom") for i in range(1)]
        self.deck.extend(booms_1)
        booms_2 = [Card.Magic_Card("wind", "boom") for i in range(1)]
        self.deck.extend(booms_2)
        booms_3 = [Card.Magic_Card("water", "boom") for i in range(2)]
        self.deck.extend(booms_3)
        booms_4 = [Card.Magic_Card("elec", "boom") for i in range(2)]
        self.deck.extend(booms_4)
        
    def draw(self):
        return self.deck.pop()

    def shuffle(self):
        shuffle(self.deck)

if __name__ == '__main__':
    myDeck = Deck()
    myDeck.shuffle()
    print(len(myDeck.deck))
    for item in myDeck.deck:
        print(item.descriptor())

    print("I am drawing" + myDeck.draw().descriptor())
    print("remainning cards" + str(len(myDeck.deck)))