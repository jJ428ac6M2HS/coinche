from random import choice, shuffle, randint
from rules import suitsChoices, valueChoices

class Card:
    def __init__(self, suit = "a", value = "a"):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "Carte : {} de {}".format(self.value, self.suit)

    def randGenerate(self):
        self.suit = choice(suitsChoices)
        self.value = choice(valueChoices)

class Deck:
    def __init__(self):
        self.decklist = []

    def __str__(self):
        return"Deck de {}".format(len(self.decklist))

    def generate(self):
        for suit in suitsChoices:
            for value in valueChoices:
                self.decklist.append(Card(suit,value))

    def fullReveal(self):
        for card in self.decklist:
            print(card)

    def smallReveal(self):
        for card in self.decklist:
            print(card, end ="; ")
        print("")



    def shuffle(self):
        shuffle(self.decklist)

    def cut(self):
        cardCut = randint(0,31)
        print("Deck cut à la carte {}.".format(cardCut))
        for i in range(cardCut):
            self.decklist.append(self.decklist.pop(0))



class Hand:
    def __init__(self):
        self.cardlist = []
        self.index = len(self.cardlist)

    def revealHand(self):
        for card in self.cardlist:
            print(card, end="; ")
        print("")

class Mat:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __str__(self):
        print("1")


class DiscardPile:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __str__(self):
        print("1")

class Player:
    def __init__(self, nickname = "Joueur", points = 0):
        self.nickname = nickname
        self.points = points
        self.hand = Hand()

    def __str__(self):
        return "Joueur {} : {} points".format(self.nickname, self.points)
