
import random

#yes
yes = ["Y", "y", "yes", "Yes"]
#no
no = ["N", "n", "No", "no"]

#positive
pos = ["pos", "Pos", "positive", "Positive", "+"]
#negative
neg = ["neg", "Neg", "negative", "Negative", "-"]

#list of greetings
greetings = ["hello", "hi"]

#list of closings
closings = ["so long", "toodles"]

#dictionary of fruits and their corresponding colors
fruitsAndColors = {"apple" : "red", "orange":"orange", "pear": "green", "cherry" :"red" , "peach" : "orange"}

#list of positive feelings
positive = ["good", "well", "great", "fantastic", ":)", "(:"]
#list of negative feelings
negative = ["bad", "terrible", "tired", "stressed", ":(", "):"]

#list of computer responses
response = ["i'm sorry, i'm afraid i don't understand what you're saying. ", "sorry, i didn't quite catch that. ","sorry, please try again later! ", "always trying my best to learn! "]

#this function registers a phrase into the dictionary
def register(type, phrase):
    type.append(phrase)
    print(type)

#conversation loops until interrupted by user
running = True
while running == True:
    # initializing dictionary and assigning values to keys (done at the start of loop to update lists and dictionaries
    d = {}
    d["greetings"] = greetings
    d["closings"] = closings
    d["fruits"] = fruitsAndColors
    print(d)
    feelings = {}
    feelings["positive"] = positive
    feelings["negative"] = negative
    print(feelings)

    print("\n")

    #asks for how user is feeling
    phrase = input("how are you doing? ") #checks in user input is a recognized feeling
    #if computer recognizes user input as a positive statement
    if phrase in feelings["positive"]:
        print("thats great to hear! ")
    #if computer recognizes user input as a negative statement
    elif phrase in feelings["negative"]:
        print("i'm sorry to hear that. ")
    #if computer does not recognize statement, ask if they would like to register the phrase
    else:
        print(random.choice(response))
        question = input("would you like to register this phrase? yes or no: ")
        #if user wants to register phrase, they categorize the phrase as a positive or negative statement
        if question in yes:
            posOrNeg = input("is this a posi"
                             "tive or negative phrase? ")
            #if phrase is positive, add it to list of positive phrases
            if posOrNeg in pos:
                register(positive,phrase)
            #if negative phrase, add it to list of negative phrases
            elif posOrNeg in neg:
                register(negative,phrase)
            #if no response detected, alert user!
            else:
                print(random.choice(response))
        #alert user if computer does not recognize input
        else:
            print(random.choice(response))
    end = input("would you like to end the conversation? yes or no: ")
    if end in yes:
        print("goodbye! ")
        running = False
    else:
        running = True




