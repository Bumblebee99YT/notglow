import nextcord
from nextcord.ext import commands

intents = nextcord.Intents().all()
client = commands.Bot(command_prefix="ng.", intents=intents)

@client.event
async def on_ready():
    print("Yo wsg bbg")

@client.command()
async def hello(ctx):
    await ctx.send("bro shut yo btch a$$ up")

client.run("")