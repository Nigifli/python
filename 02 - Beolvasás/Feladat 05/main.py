from os import system

bandName: str=None
songName: str=None
songLenght: int=None

print("Kérem adja meg a kedvenc együttesének a nevét: ", end="")
bandName=str(input())

print("Kérem adja meg a kedvenc együttesének legjobb zeneszámának a nevét: ", end="")
songName=str(input())

print("Kérem adja meg a kedvenc együttesének legjobb zeneszámának a hosszát percben: ", end="")
songLenght=str(input())

system('cls')

print(f"Az ön kedvenc együttesének {bandName} a legjobb zeneszáma {songName} melynek hosszaa {songLenght} perc!")