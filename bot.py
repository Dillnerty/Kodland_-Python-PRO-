import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="$", intents= discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hola soy un bot con 'Bot class'")

@bot.command()
async def say(ctx,*, mensaje):
    await ctx.send(f"{mensaje}")

bot.run("MTM5Mzk5ODg0MDc0MjU0NzU2Ng.G2FEoj.JCBFWYF6Hg7KFSUSoh7jSm2lqpctECKii36-yw") 


