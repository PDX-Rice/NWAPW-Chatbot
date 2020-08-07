from tkinter import *
import webbrowser
import json
from spellchecker import SpellChecker
import random
import requests
from bs4 import BeautifulSoup

#set up web scraping
url = "https://www.worldometers.info/coronavirus/country/us/" #data source
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
usa = soup.find("tr", class_ ="total_row_usa") #data for usa
totalCases = list(usa.children)[3] #total cases in the usa
newCases = list(usa.children)[5] #todays new cases
totalDeaths = list(usa.children)[7] #total deaths
covid = ["coronavirus", "covid 19", "19", "corona", "virus", "cases", "usa", "sick", "covid"] #covid related words


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
    print("I didn't recognize an adjective in your response." + "\n" +
          "You can add new phrases with the 'add' button!")
    addMenu() #open the window to add phrases


# instead of taking console input, take input from tkinter
def conversation(enteredtext):
    understands = False
    phrase = enteredtext.lower().split()
    for word in phrase:
        word = spell.correction(word)
        meaning = findworddef(word, wordData)
        if word in covid: #if covid related term is entered
            meaning = "covid"
        if meaning != '':
            understands = True
            if meaning == 'positive':
                print("That's " + random.choice(responses['positive']) + " to hear!")
                print("how are you")
            elif meaning == 'negative':
                print("That's " + random.choice(responses['negative']) + " to hear, I'm sorry about that.")
                print("how are you")
            elif meaning == 'ending':
                print(random.choice(responses['closings']))
            elif meaning == 'covid':
                print("The USA has a total of " + totalCases.get_text() + " coronavirus cases right now.")
                print(newCases.get_text() + " of them are new cases.")
                print("There are " + totalDeaths.get_text() + " total deaths in the country.")
                print("how are you")
    if not understands:
        defineword(wordData)


# gets input and displays a response
def enterClick():
    enteredtext = textentry.get()
    textbox.insert(END, enteredtext, "tag-right")  # dock text to right

    print("\n")
    displayOutput(enteredtext)
    textentry.delete(0, END)  # clear
    textbox.see("end")  # scroll to end


# enter key works as enter button
def enterKey(event):  # bind takes one arguement
    enterClick()


def displayOutput(enteredtext):
    conversation(enteredtext)


# redirect console output (print) to tkinter
def redirectOutput(inputStr):
    textbox.insert(END, inputStr)


# redirect tkinter input to console input
def redirectInput():
    pass


# creates second help menu window
def helpMenu():
    helpWindow = Toplevel()  # creates new window
    helpWindow.geometry("250x150")
    helpWindow.title("help menu")
    helpLabel = Label(helpWindow, text="helpful links!")
    helpLabel.grid(row=0)
    # opens the link the Github
    githubLink = Label(helpWindow, text="take me to Github!", fg="blue", cursor="hand2")
    githubLink.grid(row=1)
    githubLink.bind("<Button-1>", lambda e: callback("https://github.com/PDX-Rice/NWAPW-Chatbot"))
    websiteLink = Label(helpWindow, text="take me to the website!", fg="blue", cursor="hand2")
    websiteLink.grid(row=2)
    websiteLink.bind("<Button-1>", lambda e: callback("https://pdx-rice.github.io/NWAPW-Chatbot/"))

def addMenu():
    #register word as positive
    def positivePressed(event):
        if addEntry.get() != "": #if not empty
            phrase = spell.correction(addEntry.get())
            means = "positive"
            wordData.append([phrase, means])
            with open('../wordData.json', 'w') as outfile:
                json.dump(wordData, outfile, indent=4)
            message.insert(END, phrase +" was registered as a positive phrase!" + "\n")
        else:
            message.insert(END, "You must enter something " + "\n")

    def negativePressed(event):
        if addEntry.get() != "":  # if not empty
            phrase = spell.correction(addEntry.get())
            means = "negative"
            wordData.append([phrase, means])
            with open('../wordData.json', 'w') as outfile:
                json.dump(wordData, outfile, indent=4)
            message.insert(END, phrase + " was registered as a negative phrase!" + "\n")
        else:
            message.insert(END, "You must enter something " + "\n")

    #setup toplevel
    addWindow = Toplevel()
    addWindow.geometry("250x150")
    addWindow.title("add phrases")
    #label
    addLabel = Label(addWindow, text = "What phrase would you like to define? ")
    addLabel.grid(row = 0)
    #phrase entry
    addEntry = Entry(addWindow, width=20, bg="white", background="#272727", fg="#f1f1f1", font="Helvetica", borderwidth=0,
                      highlightthickness=0)
    addEntry.grid(row=1)
    addEntry.focus()
    #label 2
    addLabel2 = Label(addWindow, text = "Is that word positive or negative? ")
    addLabel2.grid(row=2)
    #define radio buttons
    defineVar = StringVar()
    defineVar.set('') #none selected
    positiveButton = Radiobutton(addWindow, text = "positive", value = "positive", variable = defineVar)
    positiveButton.grid(row = 4)
    positiveButton.bind('<ButtonRelease-1>', positivePressed) #when selected
    negativeButton = Radiobutton(addWindow, text = "negative", value = "negative", variable = defineVar)
    negativeButton.grid(row =5)
    negativeButton.bind('<ButtonRelease-1>', negativePressed) #when selected
    # message output box
    message = Text(addWindow)
    message.configure(width=20, font="helvetica")
    message.grid(row=7)


# open url in browser
def callback(url):
    webbrowser.open_new(url)

#setup
root=Tk()
root.title("chatbot")
root.configure(background = "#121212")
label = Label(root, text="say something to the chatbot", bg = "#121212", fg = "#7c7c7c", font = "helvetica")
label.grid(row = 0, padx = 2, pady = 2)
textbox=Text(root)
textbox.configure(background = "#272727", fg = "#f1f1f1", borderwidth = 0, highlightthickness = 0, font = "helvetica")
textbox.tag_configure("tag-right", justify = "right")
textbox.grid(row = 1, padx = 2, pady = 2)


#enter button
enterButton=Button(root, text='send', command=enterClick, background = "#9DA9F8", fg = "#272727",borderwidth = 0, highlightthickness = 0 )
#bind enter key
root.bind('<Return>', enterKey)  # bind enter key
enterButton.grid(row = 3)
#entry area (user input)
textentry = Entry(root, width = 20, bg = "white", background = "#272727", fg = "#f1f1f1", font = "Helvetica" ,borderwidth = 0, highlightthickness = 0)
textentry.grid(row = 4)
textentry.focus() #automatically set focus to entry
#help button
helpButton = Button(root, text ='help', command = helpMenu, background = "#9DA9F8", fg = "#272727" ,borderwidth = 0, highlightthickness = 0)
helpButton.grid(row = 5)
#add button
addButton = Button(root, text ='add', command = addMenu, background = "#9DA9F8", fg = "#272727" ,borderwidth = 0, highlightthickness = 0)
addButton.grid(row = 6)

#main
def main():
    #redirect print (output) lines
    sys.stdout.write = redirectOutput #whenever sys.stdout.write is called, redirector is called

    #on startup do this stuff
    print(random.choice(responses['greetings']))
    print("how are you (or ask me about Covid cases!)")

    root.mainloop()

if __name__=="__main__":
    main()
