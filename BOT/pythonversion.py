import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "-")

@client.event
async def on_ready():
    print('We READY!')

client.run('Njk5NTAyMzM4MDI4NzMyNDE2.XpVUUQ.C6pSeNhIY6k5sIX9QqDTP0eZJ5w')

