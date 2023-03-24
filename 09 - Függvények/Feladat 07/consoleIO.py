def makeCoor() -> float: 

    temp: str = None
    coordinate: float = None

    while (coordinate == None):
        print("Kérem adjon meg egy koordinátát: ", end="")
        temp = input()

        if (temp.isnumeric()):
            coordinate = float(temp)
            
    return coordinate
            

