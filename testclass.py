import sys, pygame
from pygame.locals import *
from classe import *

deck = ['GeminiElf', 'MonsterReborn', 'SummonedSkull']

n = 0
for card in deck:
    carta = Card(card)

print carta.name
print carta.type
print carta.ATK
carta.Atack()
