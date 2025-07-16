import discord
from discord.ext import commands
import random

def motivations():
    motiv = ["El único límite entre tú y tus sueños es la voluntad de intentarlo y la fe en que es posible.", "Cada paso, por pequeño que sea, te acerca más a la meta. No subestimes el poder del avance constante.", "Cuando caigas, recuerda que levantarte es la prueba de tu fuerza; cada tropiezo te hace más resistente.", "No esperes el momento perfecto: créalo con tu actitud, tu esfuerzo y tu determinación.", "Tu actitud hoy define tu futuro mañana. Elige la perseverancia y verás cómo florecen tus logros."]
    moti = random.randint(1,5)
    if moti == 1:
        return motiv[0]
    elif moti == 2:
        return motiv[1]
    elif moti == 3:
        return motiv[2]
    elif moti == 4:
        return motiv[3]
    else:
        return motiv[4]
    
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

@bot.command()
async def motive(ctx):
    await ctx.send("Qué tal: " + motivations())

bot.run("MTM5MzM5MTYwNDY5MzQ3MTMxMg.GXPPDm.3kaDVMheV_SwlzmZwmWC6WsN_1rNSzMTRLIvPw") # Corre el código

