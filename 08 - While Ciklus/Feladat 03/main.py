from random import randint

number: int = None
solution: int = None
temp: str= None
tries = 0

solution = randint(1, 9)

while(tries < 5 and number != solution):
    print("Tippeljen: ")
    temp = input()
    if (temp.isnumeric()):
        number = int(temp)


if (number == solution):
    print("Talált!")
else:  
    print("Nem nyert!")
  
        

