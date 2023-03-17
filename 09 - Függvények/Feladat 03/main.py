from consoleIO import *
from helpers import *

name: str = None
birthYear: int = None

name = makeName()
birthYear = makeBirthYear()
age = calculateAge(birthYear)
print(f"{name} ön az idén {age} éves")







