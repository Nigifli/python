start: int=None
end: int=None
harommaloszthatoparatlan: int = 0


print("Kérem adja meg az intervallum kezdőértékét: ")
start=int(input())

print("Kérem adja meg az intervallum végértékét: ")
end=int(input())

for i in range(start, end + 1, 1):
    if(i % 3 == 0 and i % 2 != 0):
        harommaloszthatoparatlan += 1
print(f"Az intervallumban {harommaloszthatoparatlan} mennyiségű szám van.")
