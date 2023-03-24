def makeHUF() -> int:

    temp: str = None
    huf: int = None
    truncatedString: str = None

    while(huf == None):
        print("Kérem írjon be egy értéket forintba (HUF): ", end="")
        temp = input()
        truncatedString = temp.replace(".","").replace("-", "")
        isNumber = truncatedString.isnumeric()

        if (isNumber):
            huf = float(temp)
        else: 
            print("Nem jó értéket adott meg!")

        return huf
        
def currency() -> float:

    currency: str = None

    while(currency == None or currency not in ["JPY", "USD", "EUR", "CHF"]):
        print("Kérem adja meg, hogy milyen valuta szeretné átkonvertálni a beírt forintot: ", end="")
        currency = input().upper()
        
    return currency

