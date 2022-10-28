import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.slash_command(name="ping")
    async def ping(self, msg):
        await msg.respond("pinged u buddy")

def setup(bot):
    bot.add_cog(Utility(bot))