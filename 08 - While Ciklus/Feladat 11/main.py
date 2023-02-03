from random import randint

kisebbParos: int = None
nagyobbParatlan: int = None
randomSzam: int = None
tempParos: str = None
tempParatlan: str = None
neggyeloszthatodarab: int = 0


while (kisebbParos == None or kisebbParos % 2 != 0):
    print("Kérem írjon be egy páros számot: ", end="")
    tempParos = input()
    if (tempParos.isnumeric()):
        kisebbParos = int(tempParos)
    
while(nagyobbParatlan == None or nagyobbParatlan % 2 != 1 or nagyobbParatlan <= kisebbParos):
    print("Kérem írjon be egy, az előző számnál nagyobb páratlan számot: ", end="")
    tempParatlan = input()
    if (tempParatlan.isnumeric()):
        nagyobbParatlan = int(tempParatlan)

randomSzam = randint(kisebbParos, nagyobbParatlan)
print(f"A random szám: {randomSzam}.")

if(abs(nagyobbParatlan - randomSzam) > abs(kisebbParos - randomSzam)):
    print(f"A {nagyobbParatlan} messzebb van a random számtól. ({randomSzam})")
else:
    print(f"A {kisebbParos} messzebb van a random számtól. ({randomSzam})")

print(f"A két bekért érték átlaga: {(kisebbParos + nagyobbParatlan) / 2}")

for i in range(kisebbParos, nagyobbParatlan + 1, 1):
    if (i % 4 == 0):
        neggyeloszthatodarab = neggyeloszthatodarab + 1

print(f"A néggyel osztható számok mennyisége: {neggyeloszthatodarab}")