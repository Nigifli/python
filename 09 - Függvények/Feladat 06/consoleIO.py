def makeCelsius() -> float:

    temp: str = None
    homerseklet: int = None
    
    while(homerseklet == None):
        print("Kérem írja be a hőmérsékletet Celsius-fokban: ", end="")
        temp = input()
        if(temp.isnumeric()):
            homerseklet = int(temp)

    return homerseklet

def makeUnit() -> float:

    temp: str = None
    unit: str = None

    while(unit == None or unit not in ["F", "K"]):
        print("Kérem írja be, hogy milyen mértékegységre szeretné átkonvertálni (F, K): ", end="")
        unit = input().upper()
        
    return unit
