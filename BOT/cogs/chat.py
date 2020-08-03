import discord
from discord.ext import commands
import random

#creates an event for "chatting"
class Chat(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["bruh"])
    async def hello(self, ctx):
        greetings = ["hey!", "hi!",
                    "hello!", "yo!",
                    "wassup!", ]
        await ctx.send(random.choice(greetings).title())

def setup(client):
    client.add_cog(Chat(client))