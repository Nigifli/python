from os import system

releaseDate: int=None
directorName: str=None
movieName: str=None
protagonistName: str=None



print("Kérem adja meg a film megjelenési évét: ",end="")
releaseDate=int(input())

print("Kérem adja meg a film rendezője nevét: " ,end="")
directorName=str(input())

print("Kérem adja meg a film címét: " ,end="")
movieName=str(input())
system('cls')

print("Kérem adja meg a film főszereplője nevét: ",end="")
protagonistName=str(input())

print(f"{releaseDate}-ban {directorName} rendezésében megjelent a/az {movieName} című film {protagonistName} főszereplésével!")