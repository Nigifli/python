start: int=None
end: int=None
osszeg: int=0
valtozo: int= 1

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

for i in range (start, end + 1, 1):
    osszeg = osszeg + i * valtozo
    valtozo = valtozo * -1
    
print(f"Az erdemény: {osszeg}.")