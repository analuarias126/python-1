import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def password(ctx, length: int = 10):
    pwd = gen_pass(length)
    await ctx.send(f"Tu contraseña es: `{pwd}`")

bot.run("TOKEN_AQUI")
