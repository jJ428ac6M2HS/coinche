from declaClasse import Card, Deck, Player, Hand


"""
premier système pour générer des cartes
i = 1
while i < 10:
    carte1 = Card("9", "coeur")
    carte1.randGenerate()
    print(carte1)

    i += 1
"""

deck1 = Deck()
deck1.generate()
print(deck1)
print(deck1.decklist[0])


"""
révèle le deck complet dans l'ordre
deck1.fullReveal()
"""
deck1.shuffle()
deck1.smallReveal()
print("_________________________")
deck1.cut()
deck1.smallReveal()
print("_________________________")
joueur1 = Player("Patheman")
print(joueur1)
joueur1.hand.revealHand()
joueur1.hand.cardlist.append(deck1.decklist[0])
joueur1.hand.revealHand()
deck1.smallReveal()
joueur1.hand.cardlist.append(deck1.decklist.pop(1 ) )
joueur1.hand.revealHand()
deck1.smallReveal()
print(deck1)