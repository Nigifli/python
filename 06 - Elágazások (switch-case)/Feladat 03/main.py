choice: int=None

print("Kérem válasszon üdítőt: \n1 - Coca Cola\n2 - Pepsi\n3 - Fanta\n4 - Sprite")
choice=int(input())

match choice:
    case 1:
        print("Ezt az üdítőt választotta: Coca Cola")
    case 2:
        print("Ezt az üdítőt választotta: Pepsi")
    case 3:
        print("Ezt az üdítőt választotta: Fanta")
    case 4:
        print("Ezt az üdítőt választotta: Sprite")
    case _:
        print("Nincs ilyen üdítő!")