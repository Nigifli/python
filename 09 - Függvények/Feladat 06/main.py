from consoleIO import *
from functions import *

temperature: float = makeCelsius()
unit: str = makeUnit()
convertedTemp: float = calculateUnit(temperature, unit)

print(f"Az átváltott hőmérséklet {convertedTemp} {unit}.")