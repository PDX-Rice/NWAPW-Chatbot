import os
import discord
from discord.ext import commands
import random

load_dotenv()
TOKEN = 'TOUR TOKEN HERE'
client = commands.Bot(command_prefix='-')


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
    greetings = ["hey!", "hi!",
                 "hello!", "yo!",
                 "wassup!", ]
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send(random.choice(greetings).title())

@client.command()
async def prefix(ctx, pre):
    client = commands.Bot(command_prefix= pre)
    await ctx.send('Successfully changed the prefix to "' + pre + '"')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
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
    await ctx.send(f'Question: ' + question + '\n' + random.choice(responses))


client.run(TOKEN)
