import random

random: int=None
guess: int=None
tries: int=0

random = random.randrange(1, 9)

print("Tippeljen egy számra 0 és 9 között! ", end="")
guess = int(input())

while(tries < 5):
    if (guess == random):
        print("Talált!")
    else:
        tries = tries + 1
        print("Tippeljen egy számra 0 és 9 között! ", end="")
        guess = int(input())
        
print(random)