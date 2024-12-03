from random import randint
from utils import clear

from Animations import fireballAni, fightAni, no_damage_fightAni, no_damage_fireballAni



def fight(hero):
    print("Hero decided to fight with a goblin...")

    if hero["healing_potion"] >= 1: #Heal before fight
        print(f"you have {hero['healing_potion']} 🍵healing potions in your backpack.")

        # HP healing
        heal = 25

        drink = input("Do you want to drink it? [y/n] ").lower()
        if drink == '' or 'y' in drink:
            hero["hp"] += heal
            hero["healing_potion"] -= 1

            print("🩵 you healed for 25 HP")
            print(f"now, you have 🍵 {hero['healing_potion']} healing potions left.")


    if hero["fireball"]:
        # Fireball attack
        damage = randint(0, 20)
        newxp = randint(10, 50)
        hero["hp"] -= damage
        hero["xp"] += newxp

        if damage == 0:
            print(f"{no_damage_fireballAni}")
            print("Hero easily defeated the goblin with a fireball! 😎")
        else:
            print(f"{fireballAni}")
            print(f"Hero got {damage} damage 🤕")

    else:
        # Regular attack
        damage = randint(0, 30)
        newxp = randint(5, 40)
        hero["hp"] -= damage
        hero["xp"] += newxp

        if damage == 0:
            print(f"{no_damage_fightAni}")
            print("Hero easily defeated the goblin! 😎")
        else:
            print(f"{fightAni}")
            print(f"Hero got {damage} damage 🤕")

    found_healing_potion = randint(0, 100) <= 30 # 30% chance to find healing
    if found_healing_potion:
        hero["healing_potion"] += 1
        print("hero found a healing potion 🍵!")

    if hero["spellbook"]:
        found_superpotion = randint(0, 100) <= 15  # 15% chance to find superpotion
        if found_superpotion:
            hero["superpotion"] += 1
            print("Hero found a 🏺 superpotion!")


    print(f"Hero won the fight and gained ⭐{newxp} XP!")


    print(f"🩵 Current HP: {hero['hp']}, ⭐XP: {hero['xp']}")

    input("[Press ENTER to finish the fight]")
    clear()


def no_fight(hero):
    print(f"hero decided to avoid the fight...")

    found_random_potion = randint(0, 100) <= 60  # 60% chance to find a potion
    if found_random_potion:
        print(f"hero found a potion!")

        drink = input("Do you want to drink it? [y/n] ").lower()
        if drink == '' or 'y' in drink:
            healing = randint(-20, 20)  # Random effect of potion
            hero["hp"] += healing

            if healing > 0:
                print(f"😋 The potion healed you for {healing} HP!")
            else:
                print(f"🤮 Oh no! The potion damaged you for {-healing} HP!")
        else:
            print("🙁 You chose not to drink the potion.")
    else:
        print(f"😐 hero found nothing while avoiding the fight.")

    print(f"🩵 Current HP: {hero['hp']}")

    input("[press ENTER to continue]")


def event(hero):
    want_to_fight = input('Fight with a goblin? [Y/n]').lower()

    if want_to_fight == '' or 'y' in want_to_fight:
        fight(hero)
    else:
        no_fight(hero)

