from itertools import product
from random import choice

CARD_VALUES = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A',)

CARD_TYPES = ('Clubs', 'Diamonds', 'Hearts', 'Spades',)

deck = tuple(product(CARD_VALUES, CARD_TYPES))

print('The deck has {} cards.\n'.format(len(deck)))

print('The deck has the following cards:')
for card in deck:
    print(card)

print('\n')

random_card = choice(deck)
print(
    'I random chose a {0} of {1} from the deck!'.format(
        random_card[0],
        random_card[1],
    )
)
