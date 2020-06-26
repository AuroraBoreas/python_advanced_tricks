# Python >= 3.7
from dataclass import dataclass

@dataclass
class Card:
    rank: str
    suit: str

card1 = Card("Q", "hearts")
print(card1 == card1)
print(card1.rank)
print(card1)
