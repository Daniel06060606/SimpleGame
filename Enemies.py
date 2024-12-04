from random import randint

class Goblin:
    def __init__(self, name = "Goblin"):
        self.name = name
        self.hp = randint(20, 50)
        self.damage = randint(5,20)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            return f"💀 {self.name} has been slain!"
        return f"🤕 {self.name} took {damage} damage! Current HP: {self.hp}"


    def attack(self):
        return randint(2, self.damage)


    def is_alive(self):
        return self.hp > 0


    def show_stats(self):
        return f"{self.name} | 🩸 HP: {self.hp}, ⚔️ Damage: {self.damage}"


class Finalboss:
    def __init__(self, name = "King Of Curses"):
        self.name = name
        self.hp = 100
        self.damage = randint(10, 30)
        self.enraged = False # Tracks the damage boost

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            return f"💀 {self.name} has been Executed!"
        return f"🤕 {self.name} took {damage} damage! Current HP: {self.hp}"

    def attack(self):
        # Check if the boss should become enraged
        if not self.enraged and self.hp < 50:
            self.enraged = True
            print(f"{self.name}: YOU GODDAMNED BRAT. I WILL MAKE SURE TO END YOUR MISERABLE LIFE!")
            print(f"🔥 {self.name} becomes enraged")
            self.damage = randint(20, 40)  # Increase damage range after enragement
        return self.damage


    def is_alive(self):
        return self.hp > 0


    def show_stats(self):
        return f"{self.name} | 🩸 HP: {self.hp}, ⚔️ Damage: {self.damage}"