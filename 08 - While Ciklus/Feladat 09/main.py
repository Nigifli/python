szam: int = None
temp: str = None

while (szam == None or szam < 100 or szam > 999):
    print("Kérem adjon meg egy háromjegyű számot:")
    temp = input()
    if(temp.isnumeric() and len(temp) == 3):
        szam = int(temp)

if (szam % 7 == 0):
    print("A szám osztható 7-tel!")
else:
    print("A szám nem osztható 7-tel!")
