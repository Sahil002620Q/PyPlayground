x = [1,2,3,4,5,6]
import random
import time
die = random.choice(x)
choice = input("Roll a die  ~[y/n] : \n")
time.sleep(2)
if choice == 'y':
    print("you got ",die)
else:
    print("user cancelled operation")