import random

class Hero:
    def __init__(self, name):
        self.name = name #each hero created has different name
        self.health = 100 #each hero begins with 100 health
        self.attack_power = 20 #each hero can max at 20 damage

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0

    def battle_cry(self, name):
        print(f"{name} says 'For my kingdom!!' as they charge into the battle.")

    pass
