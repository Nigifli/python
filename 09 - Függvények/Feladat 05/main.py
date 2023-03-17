from consoleIO import *
from functions import *

word1: str = None
word2: str = None
count: int = None

word1 = makeWord()
word2 = makeWord()

count = calculateCount(word1, word2)

print(count)