nagyobbSzam: int = None
kisebbSzam: int = None
kisebbIdeiglenes: str = None
nagyobbIdeiglenes: str = None

while(kisebbSzam == None):
    print("Kérem írja be a kisebbik számot: ")
    kisebbIdeiglenes = input()
    if(kisebbIdeiglenes.isnumeric()):
        kisebbSzam == int(kisebbIdeiglenes)

while ((kisebbSzam == None or nagyobbSzam == None) or nagyobbSzam <= kisebbSzam):
    print("Kérem írja be a kisebbik számot: ")
    kisebbIdeiglenes=input()

    print("Kérem írja be a nagyobbik számot: ")
    nagyobbIdeiglenes=input()

    if (kisebbIdeiglenes.isnumeric() and (nagyobbIdeiglenes.isnumeric())):
        nagyobbSzam = int(nagyobbIdeiglenes)
        kisebbSzam = int(kisebbIdeiglenes)

for i in range (nagyobbSzam, kisebbSzam, -1):
    print(i)