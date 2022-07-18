import nextcord
from nextcord.ext import commands
import aiosqlite

class Utility(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  #Event
  @commands.Cog.listener()
  async def on_ready():
    setattr(self.bot, "db", await aiosqlite.connect("afk.db"))
    async with self.bot.db.cursor() as cursor:
      await cursor.execute("CREATE TABLE IF NOT EXISTS afk (user INTEGER, guild INTEGER, reason TEXT")
      
  #AFK Command
  @commands.command()
  async def afk(self, ctx, *, reason=None):
    if reason == None:
      reason = "No reason provided!"
    async with self.bot.db.cursor() as cursor:
      await cursor.execute("SELECT reason FROM afk WHERE user = ? AND guild = ?", (ctx.author.id, ctx.guild.id,))
      data = await cursor.fetchone()
      if data:
        if data[0] == reason:
          return await ctx.send("You are already AFK with the same reason!")
