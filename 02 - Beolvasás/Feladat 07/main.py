from os import *

carBrandName: str=None
carModel: str=None
carType: str=None
cubiCentimeters: int=None
releaseDate: int=None

print("Kérem adja meg a kedvenc autójának a márkáját: ", end="")
carBrandName=str(input())

print("Kérem adja meg a kedvenc autójának a modelljét: ", end="")
carModel=str(input())

print("Kérem adja meg a kedvenc autójának a típusát: ", end="")
carType=str(input())

print("Kérem adja meg a kedvenc autója motorjának a köbcentijét: ", end="")
cubiCentimeters=int(input())

print("Kérem adja meg a kedvenc autójának a megjelenési évét: ", end="")
releaseDate=int(input())

system('cls')

print(f"Márka: {carBrandName}\nModell: {carModel}\nTípus: {carType}\nKöbcenti: {cubiCentimeters}\nMegjelenési év: {releaseDate}")