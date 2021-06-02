#######################################################################################################################
# Slot Machine Version 1
# Author: Jacob Rutkowski
# Class Period: Period 3
# Last Modified: 2/18/19
#######################################################################################################################
# Import libraries
import random
# Have the user randomly generate 7 number.
print("The machine is spinning...")
num = random.randint(0, 999)
total = 1
while num != 777:
    print("The machine spun a", num)
# If the numbers are equal to 777, then congratulate the user on hitting the jackpot.
    print("Sorry, you didn't win this time. Try again?")
    print("The machine is spinning...")
    num = random.randint(0, 999)
    total += 1
print("The machine spun a", num)
print("Congratulations! You hit the Jackpot! $$$")
print("The machine spun {} times!".format(total))