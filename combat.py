from random import randint
from time import sleep
from utils import clear
from Hero import Hero
from Enemies import Goblin, Finalboss


def fight(hero):
    clear()
    print(f"{hero.name} decided to fight with a goblin...")

    if hero.healing_potion >= 1:  # Heal before fight
        print(f"You have {hero.healing_potion} 🍵 healing potions in your backpack.")
        drink = input("Do you want to drink one? [y/n] ").lower()
        if drink == '' or 'y' in drink:
            print(hero.drink_healing_potion())

    goblin = Goblin()  # Create a new Goblin instance
    print(f"⚔️ A wild {goblin.name} appears!")
    print(goblin.show_stats())

    while goblin.is_alive() and hero.hp > 0:
        # Hero's turn to attack
        if hero.fireball:
            goblin_damage = randint(10, 30)  # Fireball does higher random damage
            print(f"🔥 {hero.name} casts Fireball!")
        else:
            goblin_damage = randint(5, 20)  # Normal attack range
        print(goblin.take_damage(goblin_damage))
        sleep(1.5)

        if not goblin.is_alive():
            print(f"🏆 {hero.name} defeated the {goblin.name}!")
            hero.add_xp(20)  # Reward XP for defeating the goblin
            break

        # Goblin's turn to attack
        print(f"🩸 {goblin.name} attacks!")
        if hero.attempt_dodge():
            print(f"🛡️ {hero.name} dodged the attack!")
        else:
            hero_damage = goblin.attack()
            print(hero.take_damage(hero_damage))
        sleep(1.5)

        if hero.hp <= 0:
            print(f"💀 {hero.name} has been defeated!")
            break

    if randint(0, 100) <= 30:  # 30% chance to find a healing potion
        hero.healing_potion += 1
        print("Hero found a healing potion 🍵!")

    if hero.spellbook and randint(0, 100) <= 15:  # 15% chance to find a superpotion
        hero.superpotion += 1
        print(f"{hero.name} found a 🏺 superpotion!")

    input("[Press ENTER to finish the fight]")
    clear()


def no_fight(hero):
    print("Hero decided to avoid the fight...")
    if randint(0, 100) <= 60: #60% chance to find random potion
        healing = randint(-20, 20)
        if input("Do you want to drink a found potion? [y/n] ").lower() in ['y', '']:
            if healing > 0:
                print(f"😋 The potion healed you for {healing} HP!")
            else:
                print(f"🤮 Oh no! The potion damaged you for {-healing} HP!")
            hero.hp += healing
        else:
            print("🙁 You chose not to drink the potion.")
    else:
        print("😐 Hero found nothing while avoiding the fight.")

    input("[Press ENTER to continue]")


def boss_fight(hero):
    clear()
    boss = Finalboss()
    print(f"👑 A fearsome {boss.name} appears!")
    print(boss.show_stats())

    while boss.is_alive() and hero.hp > 0:
        # Hero's turn to attack
        if hero.fireball:
            boss_damage = randint(20, 40)  # Fireball does higher damage against the boss
            print(f"🔥 {hero.name} casts Fireball!")
        else:
            boss_damage = randint(10, 20)  # Normal attack range
        sleep(2)
        print(boss.take_damage(boss_damage))
        sleep(2)

        if not boss.is_alive():
            print(f"{boss.name}: THIS ISN'T OVER. I WON'T DIE TO SOME WEAKLING LIKE YOU")
            sleep(2)
            print(f"{hero.name} dodges his attack and uses BLACK FLASH to end him!")
            sleep(2)
            print(f"🏆 {hero.name} has defeated the {boss.name}! Dungeon cleared!")
            hero.add_xp(100)  # Big XP reward
            return

        # Boss's turn to attack
        hero_damage = boss.attack()
        if hero.attempt_dodge():
            print(f"🛡️ {hero.name} dodged the incoming attack")
            sleep(2)
        else:
            if boss.enraged:  # Boss switches to enraged attack mode when HP < 50%
                print(f"{boss.name}: Furnace... Open.")
                sleep(2)
                print(f"{boss.name} sends a fire arrow towards {hero.name}!")
                sleep(2)
                print(hero.take_damage(hero_damage))
            else:
                print(f"💥 {boss.name} sends dozens of slashes towards {hero.name}!")
                sleep(2)
                print(hero.take_damage(hero_damage))


        if hero.hp <= 0:
            if boss.hp < 50:
                print(f"💀 {hero.name} has fallen in the final battle!")
                sleep(1)
                print(f"{boss.name}: The moonlight’s illumination makes it easier to see how pathetic you are.")
            else:
                print(f"💀 {hero.name} has fallen in the final battle!")
                print(f"{boss.name}: Stand Proud... you are strong")
            break

    input("[Press ENTER to finish the fight]")
    clear()



def event(hero):
    if input("Fight with a goblin? [y/n] ").lower() in ['y', '']:
        fight(hero)
    else:
        no_fight(hero)

