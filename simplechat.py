import random

Greetings = ["Hello", "hello", "hey", "Hey", "Hi", "hi", "yo", "Yo"]
Greetingsresponse = ["Hey there", "Hey", "Thanks for the greeting", "Don't forget to say an ending work to end the chat"]
Endings = ["Bye", "bye", "goodbye", "Goodbye", "See ya", "see ya", "c ya", "end", "End"]
Yes = ["yes", "Yes", "Y", "y"]
No = ["No", "no", "n", "N"]
loop = True

print("My current greetings are: " + str(Greetings))
print("My current ending words are: " + str(Endings))
print("\n")

say = input("Would you like to add a greeting or an ending word? (Y/N): ")

if say in Yes:
    say = input("Greeting or ending? (G/E): ")
    if say == "G":
        Greetings.append(input("What greeting word would you like to add: "))
    elif say == "E":
        Endings.append(input("What ending word would you like to add: "))

print("\n")

while loop:
    say = input(random.choice(Greetings).title() + ": ")

    if say in Greetings:
        print(random.choice(Greetingsresponse))
    elif say in Endings:
        loop = False
        print("Good talk, see ya next time")
    else:
        print("Could you say something simpler please?")
        print("If you want to stop chatting please say and ending word")




