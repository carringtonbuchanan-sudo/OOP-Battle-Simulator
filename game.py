from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Diagonal Flame"

def battle(hero : Hero, enemy : Goblin):
    round_num = 1
    while hero.is_alive() and enemy.is_alive():
        print(f"Round {round_num}")
        round_num += 1
        
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
        print()

    if hero.is_alive():
       print(f"{hero.name} wins!")
    else:
        print(f"{hero.name} has been defeated. {enemy.name} wins.")
    


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Kyrex")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Ezra")
    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")
    print()

    print("But no hero has answered the call... yet.")
    print()

    hero = Hero("Chast")
    print(f"But wait! Here comes our hero now. {hero.name} enters the arena with {hero.health} health.")
    hero.battle_cry("Chast")
    print(f"Let the battle begin.")
    print()

    battle(hero, goblin)

    
    


if __name__ == "__main__":
    main()