from random import random


import random
class Dice:

    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        output = (first, second)
        return output

dice = Dice()
output = ()
output = dice.roll()
print(output)
