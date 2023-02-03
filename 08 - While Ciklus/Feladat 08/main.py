valasztas: int = None
ideiglenes: str = None
ital: int = None

print("1 - 7UP\n2 - Kinley\n3 - Fanta\n4 - Sió\n5 - Kubu")

while (valasztas == None or not (valasztas > 0 and valasztas <= 5)):
    print("Kérem válasszon egy üdítőt a felsoroltak közül: ")
    ideiglenes = input()

    if(ideiglenes.isnumeric()):
        valasztas = int(ideiglenes)

match valasztas:
    case 1:
        ital = "7UP"
    case 2:
        ital = "Kinley"
    case 3:
        ital = "Fanta"
    case 4:
        ital = "Sió"
    case 5:
        ital = "Kubu"

print(f"Az üdítő amit választott: {ital}")