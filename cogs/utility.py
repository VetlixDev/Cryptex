import nextcord
from nextcord.ext import commands
import aiosqlite
import datetime

class Utility(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  #Event
  @commands.Cog.listener()
  async def on_ready():
    setattr(self.bot, "db", await aiosqlite.connect("afk.db"))
    async with self.bot.db.cursor() as cursor:
      await cursor.execute("CREATE TABLE IF NOT EXISTS afk (user INTEGER, guild INTEGER, reason TEXT)")
      
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
          return await ctx.send("<:cross:928935677750566962> | You are already AFK with the same reason!")
        await cursor.execute("UPDATE afk SET reason = ? AND guild = ?", (ctx.author.id, ctx.guild.id,))
      else:
        await cursor.execute("INSERT INTO afk (user, guild, reason) VALUES (?, ?, ?)", (ctx.author.id, ctx.guild.id, reason,))
        AFKEmbed = nextcord.Embed(description = f"<a:verify:894696887767142462> | You are now AFK in **{ctx.guild.name}** | Reason: {reason}", color=0x63666A, 
                               title=f"{ctx.author.user} is now AFK!", timestamp = datetime.datetime.utcnow())
        AFKEmbed.set_footer(text="Cryptex AFK Command", icon_url=self.bot.user.avatar.url)
        AFKEmbed.set_thumbnail(url="https://i.imgur.com/LNwlBSh.png")
        await ctx.send(embed=AFKEmbed)
    await self.bot.db.commit()
    
def setup(bot):
  bot.add_cog(Utility(bot))
