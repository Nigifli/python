start: int=None
end: int=None
paros: int=0
paratlan: int=0
result: str=None


print("Kérem adja meg az intervallum kezdőértékét: ")
start=int(input())

print("Kérem adja meg az intervallum végértékét: ")
end=int(input())

for i in range(start, end + 1, 1):
    if (i % 2 == 0):
        paros += i
    else:
        paratlan +=i


    if (paros > paratlan):
        print(f"A {paros} szamok osszege nagyobb.")
    elif (paros == paratlan):
        print("A számok összege egyenlő.")
    else:
        print(f"A {paratlan} számok összege nagyobb.")

        
    