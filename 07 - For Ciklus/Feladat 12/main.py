start: int=None
end: int=None
oszthatoharommal: int=0


print("Kérem adja meg az intervallum kezdőértékét: ")
start=int(input())

print("Kérem adja meg az intervallum végértékét: ")
end=int(input())

for i in range(start, end + 1, 1):
    if (i % 3 == 0):
        oszthatoharommal += 1
    
print(f"Az intervallumban {oszthatoharommal} szám osztható hárommal.")