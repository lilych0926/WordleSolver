WORD_CHAR_LENGTH = 5

def FilterWordsLength(allWords):
    words = []
    for word in allWords:
        if (len(word) == WORD_CHAR_LENGTH):
            words.append(word)
    return words


def PrintWords(allWords):
    length = len(allWords)
    for i in range(0, length):
        print(str(i) + ": " + allWords[i], "")


def ChooseWordsCharLoc(allWords, char, locations): # index starts with 1
    words = []
    for word in allWords:
        if (len(word) >= locations[-1]):
            for location in locations:
                if (word[location - 1] == char):
                    words.append(word)
    return words


def ExcludeWordsChar(allWords, chars):
    words = []
    for word in allWords:
        bHave = False
        for char in word:
            if (char in chars):
                # print(char + " - " + word)
                bHave = True
                continue
        if (not bHave):
            words.append(word)
    return words


def ReadWordFile():
    allWordsFile = open("words.txt", 'r')
    allWords = allWordsFile.readlines()
    return allWords


def CapitalizeWords(allWords):
    words = []
    for word in allWords:
        words.append(word.upper())
    return words


def CountNumOfUniqueChar(word):
    return len(set(word))


def WildGuess(allWords):
    list = []
    for i in range(0, WORD_CHAR_LENGTH):
        list.append([])
    for word in allWords:
        numOfUniqueChar = CountNumOfUniqueChar(word)
        list[numOfUniqueChar - 1].append(word)
    words = []
    for i in range(0, 5):
        words.extend(list[i])
    return words


def FilterNonAlphabet(allWords):
    words = []
    for word in allWords:
        bNonAlpha = False
        for char in word:
            if (not char.isalpha()):
                bNonAlpha = True
                continue
        if (not bNonAlpha):
            words.append((word))
    return words


def RemoveNewLine(allWords):
    words = []
    for word in allWords:
        words.append((word[: -2]))
    return words


if __name__ == '__main__':
    words = ReadWordFile()
    words = RemoveNewLine(words)
    words = FilterWordsLength(words)
    words = CapitalizeWords(words)
    words = FilterNonAlphabet(words)
    words = WildGuess(words)

    # words = ExcludeWordsChar(words, ['M', 'O', 'N', 'E', 'Y'])
    # words = ExcludeWordsChar(words, ['C', 'L'])
    # words = ChooseWordsCharLoc(words, 'A', [3])
    # words = ChooseWordsCharLoc(words, 'S', [1, 2, 5])
    # words = ChooseWordsCharLoc(words, 'H', [1, 2, 4])
    # words = WildGuess((words))
    # words = ExcludeWordsChar(words, ['W', 'T'])
    # words = ChooseWordsCharLoc(words, 'H', [2])
    # words = ChooseWordsCharLoc(words, 'S', [1])
    # words = ChooseWordsCharLoc(words, 'R', [4])
    # words = ChooseWordsCharLoc(words, 'O', [2])
    # words = ChooseWordsCharLoc(words, 'I', [3])
    # words = ChooseWordsCharLoc(words, 'S', [4])
    # words = ChooseWordsCharLoc(words, 'T', [5])
    PrintWords(words)