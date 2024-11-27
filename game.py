from time import sleep
import os
import combat

def clear():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

hero = {                # dictionary for hero
	"🩵 hp": 100,
	"⭐ xp": 0,
	"🏺 superpotion": 0,
	"📔 spellbook": False,
	"🔥 fireball": False
}

name = input("Hero name: ")
print(name, "wakes up in a dark dungeon, it stinks of goblins...")
input("[press enter to start]")

day = 0

def startgame():
    global day
    
    while day <= 10:
        day += 1
        
        print("☀️ Day", day, "started...")
        print(showstat())
        
        if hero["🏺 superpotion"] >= 1:                    #SUPERPOTION CODE
            print(f"{name}, you have {hero['🏺 superpotion']} 🏺superpotion in your backpack.")
            drink = input("Do you want to drink it? [y/n] ").lower()
            
            if drink == '' or 'y' in drink:             #DRINKING in the morning CODE
                hero["🩵 hp"] = 100
                hero["🏺 superpotion"] -= 1
                print("🩵 full health restored")
                print(f"now {name}, you have 🏺 {hero['🏺 superpotion']} superpotions left.")
                input("[press ENTER to continue]")
                clear()
                
        if day == 5:
            print("📔 Hero found a spellbook!")
            hero["📔 spellbook"] = True
            
        combat.event(hero)
        if hero["🩵 hp"] <= 0:
            gameover()
            return
        
        print("🌙 day is over, time to sleep")
        
        if hero["📔 spellbook"] and not hero["🔥 fireball"]:
            if hero["⭐ xp"] >= 100:
                hero["🔥 fireball"] = True
                print(f"{name}, has learned fireball🔥")
                
        input("Press ENTER to sleep...")
        sleep(1)
        clear()
        
        if day == 10:
            endgame()
    

def endgame():
    print(showstat())
    print(name, "has survived the dungeon")
    input("Press ENTER to play again")
    reset()
    startgame()
	
def reset():
    global hero
    global day
	
    hero = {
	"🩵 hp": 100,
	"⭐ xp": 0,
	"🏺 superpotion": 0,
	"📔 spellbook": False,
	"🔥 fireball": False
	}
	
    day = 0
	
def gameover():
    print(showstat())
    print("😵 you died (How did you die in text game...)")
    input("Press ENTER to play again")
    reset()
    startgame()
    
def showstat():
    stats = f"🩵Current HP: {hero['🩵 hp']}, ⭐XP: {hero['⭐ xp']}\n{hero}"
    return stats
startgame()