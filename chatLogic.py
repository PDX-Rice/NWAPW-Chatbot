import json
from spellchecker import SpellChecker
import random

# Sets up spellchecker
spell = SpellChecker()

# Import input arrays
with open('../wordData.json') as json_file:
    wordData = json.load(json_file)

# Import response dictionary
with open('../responseData.json') as json_file:
    responses = json.load(json_file)


# Searches knowledge arrays for word and returns logged meaning tag
def findworddef(wrd, data):
    means = ''
    for x in range(len(data)):
        if wrd == wordData[x][0]:
            means = wordData[x][1]
            break

    return means


# Adds a new word to knowledge arrays and saves the addition to JSON file
# Needs to be reworked to accept edgecases
def defineword(data):
    yesno = input("I didn't recognize an adjective in your response,"
                  " would you like to add a word to my knowledgebase?").lower()
    if 'y' in yesno:
        wrd = input("What word would you like to define?").lower()
        means = spell.correction(input("Is that word positive or negative?").lower())
        wordData.append([wrd, means])
        with open('../wordData.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
    elif 'n' in yesno:
        return
    else:
        defineword(data)

def main():
    # Conversation loops until interrupted by user
    firstLoop = True
    running = True
    while running:
        understands = False
        phrase = ''
        # Checks if it's the first loop to say hello or not
        if firstLoop:
            phrase = input(random.choice(responses['greetings']) + ", how are you doing?").lower().split()
            firstLoop = False
        else:
            phrase = input("How are you doing?").lower().split()

        for word in phrase:
            word = spell.correction(word)
            meaning = findworddef(word, wordData)
            if meaning != '':
                understands = True
                # print(word + " = " + meaning)
                if meaning == 'positive':
                    print("That's " + random.choice(responses['positive']) + " to hear!")
                elif meaning == 'negative':
                    print("That's " + random.choice(responses['negative']) + " to hear, I'm sorry about that.")
                elif meaning == 'ending':
                    print(random.choice(responses['closings']))
                    running = False
                    break
        if not understands:
            defineword(wordData)

if __name__=="__main__":
    main()

#instead of taking console input, take input from tkinter
def conversation(enteredtext):
    phrase = enteredtext.lower().split()
    for word in phrase:
        word = spell.correction(word)
        meaning = findworddef(word, wordData)
        if meaning != '':
            # print(word + " = " + meaning)
            if meaning == 'positive':
                print("That's " + random.choice(responses['positive']) + " to hear!")
                print("how are you")
            elif meaning == 'negative':
                print("That's " + random.choice(responses['negative']) + " to hear, I'm sorry about that.")
                print("how are you")
            elif meaning == 'ending':
                print(random.choice(responses['closings']))
