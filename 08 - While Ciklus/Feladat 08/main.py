valasztas: int = None
ideiglenes: int = None

print("1 - 7UP\n2 - Kinley\n3 - Fanta\n4 - Sió\n5 - Kubu")

while (valasztas == None or (valasztas > 0 and valasztas <= 5)):
    print("Kérem válasszon egy üdítőt a felsoroltak közül: ")
    ideiglenes = input()

