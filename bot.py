import nextcord
from nextcord.ext import commands
import os
from dotenv load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix=os.getenv("PREFIX), intents=nextcord.Intents.all())
                                            
@bot.event
async def on_ready():
	print(f"{bot.user} is online!")

bot.run(os.getenv("BOT_TOKEN"))
