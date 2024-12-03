from time import sleep
import os
from utils import clear




def play(animation, speed=0.5):
    for step in animation:
        clear()
        print()
        print(step)
        print()
        sleep(speed)

fireballAni = [
	'😠      👹',
    '😠🤛👹',
	'😠🔥    👹',
	'😠 🔥   👹',
	'😠  🔥  👹',
	'😠   🔥 👹',
	'😠    🔥👹',
	'😠      💥',
	'😠      💀'
]


fightAni = [
    '😠       👹',
    '😠   👹',
    '😠🤛👹',
    '🤕🗡👹',
    '🤕  💀'
]


no_damage_fightAni = [
    '😠       👹',
    '😠   👹',
    '🤸‍♂️🤛👹',
    '😠🗡👹',
    '😠  💀'
]       #Hero dodged the attack

no_damage_fireballAni = [
	'😠      👹',
	'😠🔥    👹',
	'😠 🔥   👹',
	'😠  🔥  👹',
	'😠   🔥 👹',
	'😠    🔥👹',
	'😠      💥',
	'😠      💀'
] #Launched the fireball before enemy could react