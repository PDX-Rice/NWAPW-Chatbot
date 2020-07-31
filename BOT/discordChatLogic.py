import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import json
from spellchecker import SpellChecker
import random

load_dotenv()
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


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
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


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    rspns = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f'Question: ' + question + '\n' + random.choice(rspns))


client.run(TOKEN)
