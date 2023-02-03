num: int = None
temp: str = None
ottelOszthato: int = 0
tizenegyelOszthato: int = 0

while(num == None):
    print("Írjon be egy max kétjegyű számot: ")
    temp = input()
    if (temp.isnumeric() and len(temp) < 3):
        num = int(temp)   

print(f"A 0 és az ön által megadott szám ({num}) közötti páros számok: ", end="")
for i in range (0, num, 1):
    if(i % 2 == 0):
        print(i, end=", ")
    if (i % 5 == 0):
        ottelOszthato = ottelOszthato + i
    if (i % 11 == 0):
        tizenegyelOszthato = tizenegyelOszthato + 1

print("\nSzámok amelyeket, hogyha 7-tel elosztjuk, 3-mat adnak maradékul: ", end="")
for i in range (0, num+1, 1):
    if (i % 7 == 3):
        print(i, end=", ")

print(f"\nAz öttel osztható számoknak az összege: {ottelOszthato}")
print(f"A tizenegyel osztható számok darabszáma: {tizenegyelOszthato}")
