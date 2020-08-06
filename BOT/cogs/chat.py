import discord
from discord.ext import commands
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


#creates a command for "chatting"
class Chat(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["hey"])
    async def hello(self, ctx):
        #def check(m):
            #return m.author == member and m.channel == ctx.channel

        await ctx.send(random.choice(responses['greetings']).capitalize() + "!")
        # Conversation loops until interrupted by user
        running = True
        while running:
            await ctx.send("How are you?")
            understands = False
            # Checks if it's the first loop to say hello or not
            #def check(m):
                #return m.author == member and m.channel == ctx.channel
            msg = await self.client.wait_for('message')
            if msg != '':
                if(msg.author == self.client.user):
                    running = False
                    break
                await ctx.send(f'{msg.author} said {msg.content}')
                msg = (msg.content).split()
                for word in msg:
                    #word = spell.correction(word)
                    meaning = findworddef(word, wordData)
                    if meaning != '':
                        understands = True
                        print(word + " = " + meaning)
                        if meaning == 'positive':
                            await ctx.send("That's " + random.choice(responses['positive']) + " to hear!")
                        elif meaning == 'negative':
                            await ctx.send("That's " + random.choice(responses['negative']) + " to hear, I'm sorry about that.")
                        elif meaning == 'ending':
                            await ctx.send(random.choice(responses['closings']).capitalize() + "!")
                            running = False
                            break
            if not understands:
                #defineword(wordData)
                await ctx.send("Sorry, I didn't quite get that. " + random.choice(responses['closings']).capitalize() + "!")
                running = False


def setup(client):
    client.add_cog(Chat(client))