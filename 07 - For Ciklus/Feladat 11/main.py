start: int=None
end: int=None
sum: int=0
product: int=0

print("Kérem adja meg az intervallum kezdőértékét: ")
start=int(input())

print("Kérem adja meg az intervallum végértékét: ")
end=int(input())

for i in range(start, end + 1, 1):
    if(i % 2 == 0):
        sum = sum + i
    else:
        product = product * i
