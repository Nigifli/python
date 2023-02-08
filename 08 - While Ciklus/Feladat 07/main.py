nagyobbSzam: int = None
kisebbSzam: int = None
kisebbIdeiglenes: str = None
nagyobbIdeiglenes: str = None

while(kisebbSzam == None):
    print("Kérem írja be a kisebbik számot: ")
    kisebbIdeiglenes = input()
    if(kisebbIdeiglenes.isnumeric()):
        kisebbSzam == int(kisebbIdeiglenes)

while (nagyobbSzam == None or nagyobbSzam <= kisebbSzam):
    print("Kérem írja be a nagyobbik számot: ")
    nagyobbIdeiglenes=input()

    if (nagyobbIdeiglenes.isnumeric()):
        nagyobbSzam = int(nagyobbIdeiglenes)

for i in range (nagyobbSzam, kisebbSzam, -1):
    print(i)