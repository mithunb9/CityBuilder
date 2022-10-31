import enum
import discord
from discord.ext import commands, pages 
from discord.commands import SlashCommandGroup

def build_map():
    for i in range(10):
        for j in range(10):
            gameBoard[i].append(":x:")
    return gameBoard

def render_map(gameBoard):
    map = ":cityscape::zero::one::two::three::four::five::six::seven::eight::nine:\n"
    number_key = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

    for i in range(len(gameBoard)):
        map += ":" + number_key.get(i) + ":"
        
        for j in range(len(gameBoard)):
            map += gameBoard[i][j]

        map += "\n"
    
    return map

# gameBoard = "```:zero:[1][2][3][4][5][6][7][8][9]\n[1][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[2][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[3][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[4][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[5][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[6][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[7][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[8][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n[9][ ][ ][ ][ ][ ][ ][ ][ ][ ]\n```"
# gameBoard = ":cityscape::zero::one::two::three::four::five::six::seven::eight::nine:\n:zero::x::x::x::x::x::x::x::x::x::x:\n:one::x::x::x::x::x::x::x::x::x::x:\n:two::x::x::x::x::x::x::x::x::x::x:\n:three::x::x::x::x::x::x::x::x::x::x:\n:four::x::x::x::x::x::x::x::x::x::x:\n:five::x::x::x::x::x::x::x::x::x::x:\n:six::x::x::x::x::x::x::x::x::x::x:\n:seven::x::x::x::x::x::x::x::x::x::x:\n:eight::x::x::x::x::x::x::x::x::x::x:\n:nine::x::x::x::x::x::x::x::x::x::x:\n"

gameBoard = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

gameBoardEmbed = discord.Embed(title="Game Board", description=render_map(build_map()))

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

