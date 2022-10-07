from os import system

name: str=None
birthYear: int=None

print("Kérem adja meg a nevet: ")
name=str(input())

print("Kérem adja meg a szuletesi evet: ")
birthYear=int(input())

system('cls')

print(f"{name} ön {birthYear} született!")