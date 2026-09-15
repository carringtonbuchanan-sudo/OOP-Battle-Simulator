from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Diagonal Flame"


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
    
    print()

    print(f"Let the battle begin.")
    print()

    heroDamage = hero.attack()
    goblin.take_damage(heroDamage)
    print(f"{hero.name} attacks {goblin.name} with {heroDamage} power! {goblin.name}'s health is now {goblin.health}.")


if __name__ == "__main__":
    main()
