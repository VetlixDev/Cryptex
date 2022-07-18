import nextcord
from nextcord.ext import commands
import os

bot = commands.Bot(command_prefix=os.getenv("PREFIX"), intents=nextcord.Intents.all())
                                            
@bot.event
async def on_ready():
	print(f"{bot.user} is online!")
	
for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(os.getenv("BOT_TOKEN"))
