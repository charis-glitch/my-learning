class Dice:
    def roll(self):
        import random
        return (random.randint(1, 6), random.randint(1, 6))

dice = Dice()
print(dice.roll())

from pathlib import Path 
print(Path("email").rmdir())




