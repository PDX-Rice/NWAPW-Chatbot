import discord
from discord.ext import commands
import json
from spellchecker import SpellChecker
import random

#load_dotenv()
TOKEN = 'TOKEN'
client = commands.Bot(command_prefix='-')

# Sets up spellchecker
spell = SpellChecker()

# Import input arrays
with open('wordData.json') as json_file:
    wordData = json.load(json_file)

# Import response dictionary
with open('responseData.json') as json_file:
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
        with open('wordData.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
    elif 'n' in yesno:
        return
    else:
        defineword(data)


#creates an event for "chatting"
class Chat(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=responses['greetings'])
    async def hello(self, ctx):
        await ctx.send(random.choice(responses['greetings']).title() + "!")


def setup(client):
    client.add_cog(Chat(client))