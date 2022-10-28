import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.command()
async def ping(ctx):
    await ctx.respond('pong')

load_dotenv()
bot.run(os.getenv('BOT_TOKEN'))
