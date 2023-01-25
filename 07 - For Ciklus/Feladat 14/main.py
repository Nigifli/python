start: int=None
end: int=None
otteloszthato: int=0
hetteloszthato: int=0



print("Kérem adja meg az intervallum kezdőértékét: ")
start=int(input())

print("Kérem adja meg az intervallum végértékét: ")
end=int(input())

for i in range(start, end + 1, 1):
    if(i % 5 == 0 and i % 7 == 0):
        otteloszthato += i
        hetteloszthato +=i
    if (i % 5 == 0):
        otteloszthato += i
    elif (i % 7 == 0):
        hetteloszthato += i


if (otteloszthato > hetteloszthato):
    print(f"A öttel osztható számok összege a nagyobb. ({otteloszthato})")
elif (otteloszthato == hetteloszthato):
    print("A számok összege egyenlő.")
else:
    print(f"A héttel osztható számok összege a nagyobb. ({hetteloszthato}")