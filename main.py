from lib2to3.pgen2 import token
import nextcord
from nextcord.ext import commands
import os

token = os.getenv('BOT_TOKEN')
intents = nextcord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="ng.", intents=intents)

@client.event
async def on_ready():
    print("Yo wsg bbg")

@client.command()
async def hello(ctx):
    await ctx.send("bro shut yo btch a$$ up")

client.run(token)