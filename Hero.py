#Player and all his functions

class Hero:
    def __init__(self, name ="Hero"):
        self.name = name
        self.hp = 100
        self.xp = 0
        self.healing_potion = 0
        self.superpotion = 0
        self.spellbook = False
        self.fireball = False
        self.dodge_chance = 20 #20% to dodge the incoming attack

    def attempt_dodge(self):
        from random import randint
        return randint(1, 100) <= self.dodge_chance #calculates if the attack will be dodged

    def drink_superpotion(self):
        if self.superpotion > 0:
            self.hp = 100
            self.superpotion -= 1
            return (f"🩵 Full health restored!\n"
                f"Now {self.name}, you have 🏺 {self.superpotion} superpotions left.")
        return f"No superpotions left, {self.name}!"

    def drink_healing_potion(self):
        if self.healing_potion > 0:
            self.hp = min(self.hp +25, 100)
            self.healing_potion -= 1
            return "🩵 You healed for 25 HP!"
        return "No healing potions left!"

    def learn_fireball(self):
        if self.spellbook and self.xp >= 100 and not self.fireball:
            self.fireball = True
            return f"{self.name} has learned the fireball!"
        return f"{self.name} Tried to learn new spells, but failed"

    def add_xp(self, xp):
        self.xp += xp
        return f"⭐ {xp} XP gained! Current XP: {self.xp}"

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            return f"😵 {self.name} has died!"
        return f"🤕 Hero took {damage} damage! Current HP: {self.hp}"


    def show_stats(self):
        return (f"🩵 HP: {self.hp}, ⭐ XP: {self.xp}, 🍵 Healing potions: {self.healing_potion}, "
                f"⚱️ Superpotions: {self.superpotion}, 📔 Spellbook: {self.spellbook}, 🔥 Fireball: {self.fireball}")

    def reset(self):
        self.hp = 100
        self.xp = 0
        self.healing_potion = 0
        self.superpotion = 0
        self.spellbook = False
        self.fireball = False