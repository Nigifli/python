def makeName() -> str:
    name: str = None

    while (name == None or len(name) < 2):
        print("Kérem írja be a nevét: ", end="")
        name = input()

    return name