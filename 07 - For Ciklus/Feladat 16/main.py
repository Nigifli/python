start: int=None
end: int=None
paros: int=None
paratlan: int=None
average: int=None

print("Kérem adja meg az intervallum kezdőértékét: ")
start = int(input())

print("Kérem adja meg az intervallum végértékét: ")
end = int(input())

for i in range (start, end + 1, 1):
    if (i % 2 == 0):
        paros = paros + i
    else:
        paratlan = paratlan + i

average = (paros + paratlan) / 2
print (f"A páros és páratlan számok összegének az átlaga: {average}.")
    
