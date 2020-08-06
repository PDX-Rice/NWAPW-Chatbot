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


#creates a command for "chatting"
class Chat(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["hey"])
    async def hello(self, ctx):

        # await ctx.send(random.choice(responses['greetings']).capitalize() + "!")
        # Conversation loops until interrupted by user
        firstLoop = True
        running = True
        while running:
            # Checks if it's the first loop to say hello or not
            if firstLoop:
                await ctx.send(random.choice(responses['greetings']).capitalize() + ", how are you?")
            understands = False
            userMood = ''
            msg = await self.client.wait_for('message')
            if msg != '':
                if msg.author == self.client.user:
                    print('Bot tried talking to istelf...')
                    running = False
                    break
                # await ctx.send(f'{msg.author} said {msg.content}')  # Repeats what user said back to user
                msg = msg.content.lower().split()
                for word in msg:
                    word = spell.correction(word)
                    meaning = findworddef(word, wordData)
                    if meaning == 'ending':
                        await ctx.send(random.choice(responses['closings']).capitalize() + "!")
                        running = False
                        break
                    elif meaning != '':
                        understands = True
                        print(word + " = " + meaning)
                        userMood = meaning
                        if meaning == 'positive':
                            await ctx.send("That's " + random.choice(responses['positive']) + " to hear!")
                        elif meaning == 'negative':
                            await ctx.send("That's " + random.choice(responses['negative']) + " to hear, I'm sorry about that.")
                        elif meaning == 'ending':
                            await ctx.send(random.choice(responses['closings']).capitalize() + "!")
                            running = False
                            break
            if understands:
                await ctx.send("Would you like to tell me more about your day?")
                msg = await self.client.wait_for('message')
                msg = msg.content.lower().split()
                for word in msg:
                    word = spell.correction(word)
                    meaning = findworddef(word, wordData)
                    if 'y' in word or word == 'sure':
                        await ctx.send(random.choice(responses['positive']) + ", let's hear it.")
                        msg = await self.client.wait_for('message')
                        if userMood == 'positive':
                            await ctx.send("That sounds like a " + random.choice(responses['positive']) + " day,"
                            " it was " + random.choice(responses['positive']) + " talking to you, " + random.choice(responses['closings']) + "!")
                        elif userMood == 'negative':
                            await ctx.send("That sounds " + random.choice(responses['negative']) + ". I hope your day get's better,"
                            " but it was " + random.choice(responses['positive']) + " talking to you, " + random.choice(responses['closings']) + "!")
                        running = False
                        break
                    elif 'n' in word:
                        await  ctx.send("Ok, well it was " + random.choice(responses['positive']) + "talking to you, " + random.choice(responses['closings']) + "!")
                        running = False
                        break
                    else:
                        understands = False
                        break
            if not understands and running:
                await ctx.send("I didn't recognize an adjective in your response,"
                               " would you like to add a word to my knowledgebase?")
                msg = await self.client.wait_for('message')
                if msg.content.lower() == "yes":
                    await ctx.send("What word would you like to define? (Pick 1 word)")
                    wrd = await self.client.wait_for('message')
                    await ctx.send("Is that word positive or negative?")
                    means = await self.client.wait_for('message')
                    wordData.append([wrd.content.lower(), means.conetent.lower()])
                else:
                    await ctx.send("Alright then, " + random.choice(responses['closings']).capitalize() + "!")
                    running = False
                    break


def setup(client):
    client.add_cog(Chat(client))