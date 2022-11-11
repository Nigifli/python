from os import system

x: int = None
y: int = None
z: int = None

print("Kérem adjon meg egy számot (X): ", end="")
x=(input())

print("Kérem adjon meg egy másik számot (Y): ", end="")
y=(input())

print("Kérem adjon meg egy harmadik számot (Z): ", end="")
z=(input())

if(x%y==0 and x%z==0):
    print("Az X osztható Y-nal és Z-vel is.")
elif(x%y==0 and x%z!=0):
    print("Az X csak az Y-nal osztható.")
elif(x%y!=0 and x%z==0):
    print("Az X csak a Z-vel osztható.")
else:
    print("Az X se Y-nal se Z-vel nem osztható.")