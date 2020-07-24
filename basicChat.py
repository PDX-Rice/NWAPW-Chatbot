
import random
'''
This code is a basic conversation between the computer and user. 
Recognized words are stored in dictionaries grouped by lists. The user can add new words to lists if they're unrecognized.
Computer chooses a random response from a list to avoid repetition. 
'''
#yes
yes = [ "y", "yes",]
#no
no = ["n", "no"]

#positive
pos = ["pos",  "positive", "+"]
#negative
neg = ["neg", "negative", "-"]

#list of greetings
greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "how do you do", "nice to meet you", "yo", "whats up", "long-time no see", "what's new", "howdy"]

#list of closings
closings = ["so long", "toodles", "see you", "bye", "goodbye", "i'm off", "take care", "bye-bye", "farewell", "cheerio", "gotta go", "later", "have a good one"]

#dictionary of fruits and their corresponding colors
fruitsAndColors = {"apple" : "red", "orange":"orange", "pear": "green", "cherry" :"red" , "peach" : "orange"}

#list of positive feelings
positive = ["good", "well", "great", "fantastic", ":)", "(:", "amazing", "awesome", "happy"]
#list of negative feelings
negative = ["bad", "terrible", "tired", "stressed", ":(", "):"]

#lists of computer responses when confused
confused = ["i'm sorry, i'm afraid i don't understand what you're saying. ", "sorry, i didn't quite catch that. ","sorry, please try again later! ", "always trying my best to learn! "]
#senses
senses = ["hear", "know", "see"]

#initializing dictionaries
d= {}
feelings = {}
responses = {}

#this function registers a phrase into the dictionary
def register(type, phrase):
    type.append(phrase)
    print(type)

#this function randomly generates a happy response 
def happyResponse(positive, senses):
    print("thats " + positive + " to " + senses + "!")

#conversation loops until interrupted by user
running = True
while running == True:
    #assigning values to keys (done at the start of loop to update lists and dictionaries
    d["greetings"] = greetings
    d["closings"] = closings
    d["fruits"] = fruitsAndColors
    print(d) #show words
    feelings["positive"] = positive
    feelings["negative"] = negative
    print(feelings) #show words
    responses["confused"] = confused

    print("\n")
    #greets the user
    print(random.choice(greetings))
    #asks for how user is feeling
    phrase = input("how are you doing? ").lower() #checks in user input is a recognized feeling
    #if computer recognizes user input as a positive statement
    if phrase in feelings["positive"]:
        happyResponse(random.choice(positive), random.choice(senses)) #randomly generated response
    #if computer recognizes user input as a negative statement
    elif phrase in feelings["negative"]:
        print("i'm sorry to hear that. ")
    #if computer does not recognize statement, ask if they would like to register the phrase
    else:
        print(random.choice(confused))
        question = input("would you like to register this phrase? yes or no: ").lower()
        #if user wants to register phrase, they categorize the phrase as a positive or negative statement
        if question in yes:
            posOrNeg = input("is this a positive or negative phrase? ").lower()
            #if phrase is positive, add it to list of positive phrases
            if posOrNeg in pos:
                register(positive,phrase)
            #if negative phrase, add it to list of negative phrases
            elif posOrNeg in neg:
                register(negative,phrase)
            #if no response detected, alert user!
            else:
                print(random.choice(confused))
        #alert user if computer does not recognize input
        else:
            print(random.choice(confused))
    #asks if user wants to continue talking
    end = input("would you like to end the conversation? yes or no: ").lower()
    #end the conversation and say goodbye
    if end in yes:
        print(random.choice(closings))
        running = False
    #continue
    else:
        running = True




