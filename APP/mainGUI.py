from tkinter import *
from ..chatLogic import *
import webbrowser


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

#gets input and displays a response
def enterClick():
    enteredtext = textentry.get()
    textbox.insert(END, enteredtext, "tag-right")    #dock text to right

    print("\n")
    displayOutput(enteredtext)
    textentry.delete(0, END)  # clear
    textbox.see("end") #scroll to end

#enter key works as enter button
def enterKey(event): #bind takes one arguement
    enterClick()

def displayOutput(enteredtext):
    conversation(enteredtext)

#redirect console output (print) to tkinter
def redirectOutput(inputStr):
    textbox.insert(END, inputStr)

#redirect tkinter input to console input
def redirectInput():
    pass

#creates second help menu window
def helpMenu():
    helpWindow = Toplevel()  # creates new window
    helpWindow.geometry("250x150")
    helpWindow.title("help menu")
    helpLabel = Label(helpWindow, text="helpful links!")
    helpLabel.grid(row = 0)
    # opens the link the Github
    githubLink = Label(helpWindow, text="take me to Github!", fg="blue", cursor="hand2")
    githubLink.grid(row = 1)
    githubLink.bind("<Button-1>", lambda e: callback("https://github.com/PDX-Rice/NWAPW-Chatbot"))

#open url in browser
def callback(url):
    webbrowser.open_new(url)


#enter button
enterButton=Button(root, text='send', command=enterClick, background = "#9DA9F8", fg = "#272727",borderwidth = 0, highlightthickness = 0 )
#bind enter key
root.bind('<Return>', enterKey)  # bind enter key
enterButton.grid(row = 3)
#entry area (user input)
textentry = Entry(root, width = 20, bg = "white", background = "#272727", fg = "#f1f1f1", font = "Helvetica" ,borderwidth = 0, highlightthickness = 0)
textentry.grid(row = 4)
#help button
helpButton = Button(root, text ='help', command = helpMenu, background = "#9DA9F8", fg = "#272727" ,borderwidth = 0, highlightthickness = 0)
helpButton.grid(row = 5)

#redirect print (output) lines
sys.stdout.write = redirectOutput #whenever sys.stdout.write is called, redirector is called.

#on startup do this stuff
print(random.choice(responses['greetings']))
print("how are you")

root.mainloop()
