from random import randint

bedobottPenz: int = 0
valasztas: int = None
ideiglenes: str = None
uditoAr: int = 300
udito: str = None


while (bedobottPenz < 300):
    bedobottPenz = bedobottPenz + randint(0,200)
    print(f"Jelenleg {bedobottPenz} forintot dobott be eddig.")

while (valasztas == None or not(valasztas >=1 and valasztas <=5)):
    print("Nyomja meg a menü előtti számot a kívánt üdítőért: ")
    
    print("1 - Ice Tea\n2 - Limonádé\n3 - Epres Jégkása\n4 - Almalé\n5 - Szénsavmentes víz")
    ideiglenes = input().strip()
    if (ideiglenes.isnumeric()):
        valasztas = int(ideiglenes)


match valasztas:
    case 1:
        udito = "Ice Tea"
    case 2:
        udito = "Limonádé"
    case 3:
        udito = "Epres Jégkása"
    case 4:
        udito = "Almalé"
    case 5:
        udito = "Szénsavmentes víz"

print(f"Ön {udito} választott. Egeszsegere!")

print(f"Önnek jár visszajárandó {bedobottPenz-300} HUF! Kérem, vegye el a visszajárót.")