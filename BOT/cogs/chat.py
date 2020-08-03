import discord
from discord.ext import commands
import random

#creates an event for "chatting"
class Chat(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        greetings = ["hey!", "hi!",
                    "hello!", "yo!",
                    "wassup!", ]

        if message.author == self.client.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send(random.choice(greetings).title())

def setup(client):
    client.add_cog(Chat(client))