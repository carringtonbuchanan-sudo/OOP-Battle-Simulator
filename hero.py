import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0

    def battle_cry(self, name):
        print(f"{name} says 'For my kingdom!!' as they charge into the battle.")

    pass
