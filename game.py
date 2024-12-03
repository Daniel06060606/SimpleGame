from time import sleep
from utils import clear
import combat
from Story import story_1, story_2, story_3, story_4

hero = {  # dictionary for hero
    "hp": 100,
    "xp": 0,
    "healing_potion": 0,
    "superpotion": 0,
    "spellbook": False,
    "fireball": False
}
name = "Hero"
day = 0

def prepare_game():
    global name

    reset()

    name = input("Hero name: ")
    print(name, "wakes up in a dark dungeon, it stinks of goblins...")
    input("[press enter to start]")

    startgame()


def startgame():
    global day

    while day <= 10:
        day += 1

        print(f"☀️ Day {day} started...")
        showstat()

        if hero["superpotion"] >= 1:  # SUPERPOTION CODE
            print(f"{name}, you have {hero['superpotion']} 🏺superpotion in your backpack.")

            drink = input("Do you want to drink it? [y/n] ").lower()
            if drink == '' or 'y' in drink:  # DRINKING in the morning CODE
                hero["hp"] = 100
                hero["superpotion"] -= 1

                print("🩵 full health restored")
                print(f"now {name}, you have 🏺 {hero['superpotion']} superpotions left.")

                input("[press ENTER to continue]")
                clear()

        if day == 2:
            story_1()

        if day == 4:
            story_2()
            escape()


        if day == 5:
            print(f"📔 {name} found a spellbook!")
            hero["spellbook"] = True

        if day== 7:
            story_3()


        if day == 9:
            story_4()

        combat.event(hero)
        if hero["hp"] <= 0:
            msg = "😵 you died (How did you die in text game...)"
            end_game(msg)

            return

        print("🌙 day is over, time to sleep")

        if hero["spellbook"] and not hero["fireball"]:
            if hero["xp"] >= 100:
                hero["fireball"] = True
                print(f"{name}, has learned fireball🔥")

        input("Press ENTER to sleep...")
        sleep(1)
        clear()

        if day == 10:

            msg = f"{name} has purged the dungeon!"

            end_game(msg)


def reset():
    global hero, day

    hero = {
        "hp": 100,
        "xp": 0,
        "healing_potion": 0,
        "superpotion": 0,
        "spellbook": False,
        "fireball": False
    }
    day = 0


def end_game(msg):
    showstat()
    print(msg)

    input("Press ENTER to play again")
    prepare_game()


def showstat():
    print(f"🩵Current HP: {hero['hp']}, "
          f"⭐XP: {hero['xp']}, "
          f"healing_potion: {hero['healing_potion']}, "
          f"⚱️Superpotion: {hero['superpotion']}, "
          f"📔Spellbook: {hero['spellbook']}, "
          f"🔥Fireball: {hero['fireball']}"
          )

def escape():
    run_away = input("Do you want to run away? [y/n] ").lower()
    if run_away == '' or 'y' in run_away:
        print(f"{name} ran away in fear from the dungeon")
        showstat()
        prepare_game()
    else:
        print(f"{name} overcame his fears and got rid of the voices")


prepare_game()
