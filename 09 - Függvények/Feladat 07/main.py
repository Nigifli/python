from functions import *
from consoleIO import *

x1: float = makeCoor()
x2: float = makeCoor()
y1: float = makeCoor()
y2: float = makeCoor()

coordinateDistance: float = round(distance(x1, x2, y1, y2), 2)

print(f"A két pont közötti távolság {coordinateDistance}.")