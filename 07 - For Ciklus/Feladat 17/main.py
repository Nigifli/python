start: int=None
end: int=None
average: int=None
osszeg: int=0
oszto: int=0

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

for i in range (start, end + 1, 1):
    osszeg = osszeg + i
    oszto = oszto + 1
average = osszeg / oszto

print(f"Az intervallum átlaga: {average}.")