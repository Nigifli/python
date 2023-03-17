def calculateCount(word1: str, word2: str) -> int:

    matches: str = ""
    for i in word1:
        for j in word2:
            if (i == j and j not in matches):
                matches += j

    return len(matches)