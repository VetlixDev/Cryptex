import nextcord
from nextcord.ext import commands

class Information(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  #Ping Command
  @commands.command()
  async def ping(self, ctx):
    await ctx.send("<a:checkmark:934196489935278090> Pong! | Latency: **{round(self.bot.latency * 1000)}**ms!")
    
def setup(bot):
  bot.add_cog(Information(bot))
