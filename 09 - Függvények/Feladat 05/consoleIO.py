def makeWord() -> str:
    szo: str = None

    while(szo == None or len(szo) < 2):
        print("Kérem írjon be egy szót: ", end="")
        szo = input()

    return szo