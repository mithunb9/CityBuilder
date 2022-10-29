import discord
import os
from discord import client
from discord.ext import commands
import asyncio
from dotenv import load_dotenv

bot = commands.Bot(intents=discord.Intents.all())

def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user}")

load()
load_dotenv(".env")

bot.run(os.getenv("BOT_TOKEN"))