Greetings = ["Hello", "hello", "hey", "Hey", "Hi", "hi", "yo", "Yo"]
Endings = ["Bye", "bye", "goodbye", "Goodbye", "See ya", "see ya", "c ya", "end", "End"]
loop = True


print("My current greetings are: " + str(Greetings))
print("My current ending words are: " + str(Endings))
print("\n")
if input("Would you like to add a greeting or an ending word? (Y/N): ") == "Y" or "y":
    if input("Greeting or ending? (G/E): ") == "G":
        Greetings.append(input("What greeting word would you like to add: "))
    else:
        Endings.append(input("What ending word would you like to add: "))

print("\n")

while loop:
    say = input("YO : ")

    if say in Greetings:
        print("Hey there thanks for the greeting")
    elif say in Endings:
        loop = False
        print("Good talk, see ya next time")
    else:
        print("Could you say something simpler please?")
        print("If you want to stop chatting please say end")


