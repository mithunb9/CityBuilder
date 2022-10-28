import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.slash_command(name="fuck")
    async def fuck(self, msg):
        await msg.respond("fuck u!")

def setup(bot):
    bot.add_cog(Utility(bot))