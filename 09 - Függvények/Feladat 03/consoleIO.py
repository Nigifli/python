def makeName() -> str:
    name: str = None

    while (name == None or len(name) < 2):
        print("Kérem írja be a nevét: ", end="")
        name = input()

    return name

def makeBirthYear() -> int:
    temp: str = None
    date: int = None

    while (date == None):
        print("Kérem írja be a születési évét: ", end="")
        temp: str = input()
        if (temp.isnumeric() and len(temp) == 4):
            date = int(temp)
        
    return date