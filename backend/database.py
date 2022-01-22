import json
import mtg

ATOMIC_CARDS = "db/AtomicCards.json"
CUBE = "db/CompanionCube.txt"

def get_card_database():
    with open(ATOMIC_CARDS) as fh:
        return mtg.AtomicCardsDatabase(json.load(fh))

def get_cube(cube_id=None):
    with open(CUBE) as fh:
        return mtg.Deck.load(fh)
