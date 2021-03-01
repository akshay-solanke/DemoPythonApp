import random
#comment added here for testing
class Dice:
    def roll(self):
        First = random.randint(1,6)
        Second = random.randint(1, 6)
        return First,Second


dice = Dice()
print(dice.roll())