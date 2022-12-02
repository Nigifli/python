r1: float=None
r2: float=None
type: str=None
result: float=None

print("Kérem írja be az első ellenállás értékét: ")
r1=float(input())

print("Kérem írja be a második ellenállás értékét: ")
r2=float(input())

print("Kérem írja be a kapcsolás típusának az első betűjét: ")
type=str(input()).lower().strip()

match type:
    case "p":
        result=(r1 * r2) / (r1 + r2)
    case "s":
        result=r1 + r2
    case _:
        print("Nincs ilyen kötés.")
    
if(result != None):
    print(f"Az eredő ellenállás: {result}")

