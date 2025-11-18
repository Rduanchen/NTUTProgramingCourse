def awf(line, wordIndex, word, document:list): # add before the word
    document[line].insert(wordIndex, word)
    return document

def awa(line, wordIndex, word, document): # add after the word
    document[line].insert(wordIndex + 1, word)
    return document

def asf(line, sentence, document): # add sentence before line i
    document[line] = [''] + sentence + document[line][1::]
    return document

def asa(line, sentence, document): # add sentence after line i
    document[line] = document[line] + sentence
    return document

def ifkey(key, word, document:list): # add word before key
    for rowID in range(len(document)):
        newArr = document[rowID].copy()
        index = 0
        for colID in range(len(document[rowID])):
            thatWord = newArr[index]
            if thatWord == key:
                newArr.insert(index, word)
                index += 1
            index += 1
        document[rowID] = newArr
    return document
        

def iakey(key, word, document:list): # add word after key
    for rowID in range(len(document)):
        newArr = document[rowID].copy()
        index = 0
        for colID in range(len(document[rowID])):
            thatWord = newArr[index]
            if thatWord == key:
                newArr.insert(index+1, word)
                index += 1
            index += 1
        document[rowID] = newArr
    return document
    

def dw(line, wordIndex, document): # delete word at line, word
    # print(document)
    # print(line, wordIndex)
    document[line].pop(wordIndex)
    return document

def dl(line, document): # delete a line
    document.pop(line)
    return document

def rp(oldWord, newWord, document): # replace oldWord with newWord
    for i, row in enumerate(document):
        for j, col in enumerate(row):
            if col == oldWord:
                document[i][j] = newWord
    return document


def c(document): # count number of words in the document
    total = 0
    for i in range(1, len(document)):
        total += len(document[i]) - 1
    return total
        


def main():
    documentLineAmount, commandAmount = map(int, input().split())
    document = [[]]
    for i in range(documentLineAmount):
        document.append([""] + input().split())

    for cmdId in range(commandAmount):
        cmd = input().split()
        amount = None
        match(cmd[0]):
            case 'awf':
                document = awf(int(cmd[1]), int(cmd[2]), cmd[3], document)
            case 'awa':
                document = awa(int(cmd[1]), int(cmd[2]), cmd[3], document)
            case 'asf':
                document = asf(int(cmd[1]), cmd[2::], document)
            case 'asa':
                document = asa(int(cmd[1]), cmd[2::], document)
            case 'if':
                document = ifkey(cmd[1], cmd[2], document)
            case 'ia':
                document = iakey(cmd[1], cmd[2], document)
            case 'dw':
                document = dw(int(cmd[1]), int(cmd[2]), document)
            case 'dl':
                document = dl(int(cmd[1]), document)
            case 'rp':
                document = rp(cmd[1], cmd[2], document)
            case 'c':
                amount = c(document)

    if amount is not None:
        print(amount)            
    for i in range(1, len(document)):
        print(' '.join(document[i][1::]))
    
main()
