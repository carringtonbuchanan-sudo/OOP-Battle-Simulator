import random
from enemy import Enemy

class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""

    def __init__(self, name):
        super().__init__(name, health=250, attackPower=30)

    def attack(self, attackPower = 4): #overrides enemy attack
        attackStyle = random.randint(1,2)
        if attackStyle == 1:
            print("FIREBALL")
            return 5 * random.randint(1,4)
        else:
            print("STOMP")
            return attackPower * random.randint(1,2)

    #hybrid override, we do sumn special but still use parent function
    def take_damage(self, damage):
        damage = damage * .75
        super().take_damage(damage)