import nextcord
from nextcord.ext import commands
import os

bot = commands.Bot(command_prefix="?", intents=nextcord.Intents.all())
                                            
@bot.event
async def on_ready():
	print(f"{bot.user} is online!")

bot.run(os.getenv("BOT_TOKEN"))
