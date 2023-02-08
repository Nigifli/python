osszeg: float = None
temp: str = None
honap: int = 0

while (osszeg == None):
    print("Megtakarított pénz: ", end="")
    temp = input()
    if (temp.isnumeric()):
        osszeg = float(temp)

while (osszeg < 100000):
    osszeg = osszeg * 1.02
    honap = honap + 1

print(f"{honap} hónap alatt fogja a megtakarítás elérni a 100 000 Ft-ot")
