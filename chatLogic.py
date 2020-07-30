import json
import random

# Input knowledge arrays
wordData = []
with open('wordData.json') as json_file:
    wordData = json.load(json_file)


def findWordDef(wrd, data):
    means = ''
    for x in range(len(data)):
        if wrd in wordData[x][0]:
            means = wordData[x][1]
            break

    return means


def defineWord(data):
    yesno = input("I didn't recognize an adjective in your response,"
                  " would you like to add a word to my knowledgebase?: ").lower()
    if yesno == 'yes':
        wrd = input("What word would you like to define?: ").lower()
        means = input("Is that word positive or negative?: ").lower()
        wordData.append([wrd, means])
        with open('wordData.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
    elif yesno == 'no':
        return


# conversation loops until interrupted by user
running = True
while running:
    understands = False
    phrase = input("How are you doing?: ").lower().split()
    for word in phrase:
        meaning = findWordDef(word, wordData)
        if meaning != '':
            understands = True
            print(word + " = " + meaning)
    if not understands:
        defineWord(wordData)
