from time import sleep
import os
from utils import clear


def play(animation, speed=0.2):
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
    '🤸‍♂️🤛👹',  #hero dodged the attack
    '😠🗡👹',
    '😠  💀'
]

no_damage_fireballAni = [
	'😠      👹',
	'😠🔥    👹',
	'😠 🔥   👹',
	'😠  🔥  👹',
	'😠   🔥 👹',
	'😠    🔥👹',
	'😠      💥',
	'😠      💀'
]