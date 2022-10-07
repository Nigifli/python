from os import system

bandName: str=None
songName: str=None
songLenght: int=None

print("Kérem adja meg a kedvenc együttesének a nevét: ")
bandName=str(input())

print("Kérem adja meg a kedvenc együttesének legjobb zeneszámának a nevét: ")
songName=str(input())

print("Kérem adja meg a kedvenc együttesének legjobb zeneszámának a hosszát percben: ")
songLenght=str(input())

system('cls')

