import enum
import discord
from discord.ext import commands, pages 
from discord.commands import SlashCommandGroup

gameBoard = "```:zero:[1][2][3][4][5][6][7][8][9]\n[1][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[2][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[3][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[4][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[5][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[6][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[7][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[8][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[9][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n```"
gameBoard = ":cityscape::zero::one::two::three::four::five::six::seven::eight::nine:\n:zero::x::x::x::x::x::x::x::x::x::x:\n:one::x::x::x::x::x::x::x::x::x::x:\n:two::x::x::x::x::x::x::x::x::x::x:\n:three::x::x::x::x::x::x::x::x::x::x:\n:four::x::x::x::x::x::x::x::x::x::x:\n:five::x::x::x::x::x::x::x::x::x::x:\n:six::x::x::x::x::x::x::x::x::x::x:\n:seven::x::x::x::x::x::x::x::x::x::x:\n:eight::x::x::x::x::x::x::x::x::x::x:\n:nine::x::x::x::x::x::x::x::x::x::x:\n"

gameBoardEmbed = discord.Embed(title="Game Board", description=gameBoard)

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        
    def get_pages(self):
        return self.pages

    @commands.slash_command(name="ping")
    async def ping(self, msg):
        await msg.respond("pinged u buddy")

    @commands.slash_command(name="default")
    async def default(self, ctx: discord.ApplicationContext):
        await ctx.respond(embed=gameBoardEmbed)

def setup(bot):
    bot.add_cog(Utility(bot))