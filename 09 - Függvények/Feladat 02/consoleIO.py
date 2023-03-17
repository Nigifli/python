def readNameFromConsole() -> str:
    name: str = None

    while(name == None or len(name) < 2 ):
        print("Név: ", end ="")
        name = input()

        if(len(name) < 2 ):
            print ("Nem megfelelo a nev!")
        

    return name.capitalize().strip()

def printWelcomeMessage(name: str) -> None:
    print(f"Welcome {name}.")