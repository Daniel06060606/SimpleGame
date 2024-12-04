from time import sleep
from utils import clear
from combat import no_fight,fight,event,boss_fight
from Story import story_1, story_2, story_3, story_4, boss_talk
from Hero import Hero

hero = Hero()
day = 0

def prepare_game():
    global hero, day

    day = 0 #resets the day
    hero.reset()

    name = input("Hero name: ")
    hero.name = name
    print(hero.name, "Arrives to the dungeon, ready to slay some monsters")
    input("[press enter to start]")

    startgame()


def startgame():
    global day

    while day <= 10:
        day += 1

        print(f"☀️ Day {day} started...")
        print(hero.show_stats())

        if hero.superpotion >= 1:
            print(f"{hero.name}, you have {hero.superpotion} 🏺superpotion(s) in your backpack.")
            drink = input("Do you want to drink it? [y/n] ").lower()

            if drink == '' or 'y' in drink:
                print(hero.drink_superpotion())
                input("[press ENTER to continue]")
                clear()

        if day == 2:
            story_1()

        if day == 4:
            story_2()
            escape()


        if day == 5:
            print(f"📔 {hero.name} found a spellbook!")
            hero.spellbook = True

        if day== 7:
            story_3()


        if day == 9:
            story_4()

        if day == 10:
            boss_talk()
            sleep(1)
            boss_fight(hero)
            if hero.hp > 0:
                msg = f"🎉 {hero.name} has purged the dungeon and executed the King Of Curses!"
            else:
                msg = "💀 You fell in the final battle."
            end_game(msg)
            return

        event(hero)
        if hero.hp <= 0:
            msg = "😵 you died... Unlucky i guess ;) "
            end_game(msg)
            return

        print("🌙 day is over, time to sleep")

        print(hero.learn_fireball())

        input("Press ENTER to sleep...")
        sleep(1)
        clear()

        if day == 10:

            msg = f"{hero.name} has purged the dungeon!"

            end_game(msg)


def end_game(msg):
    print(hero.show_stats())
    print(msg)

    input("[press ENTER to play again]")
    prepare_game()


def escape():
    run_away = input("Do you want to run away? [y/n] ").lower()
    if run_away == '' or 'y' in run_away:
        print(f"{hero.name} ran away in fear from the dungeon")
        print(hero.show_stats())
        prepare_game()
    else:
        print(f"{hero.name} overcame their fears and got rid of the voices.")


prepare_game()
