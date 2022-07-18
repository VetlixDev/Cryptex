import nextcord
from nextcord.ext import commands
import os

bot = commands.Bot(command_prefix=os.getenv("PREFIX"), intents=nextcord.Intents.all())
                                            
@bot.event
async def on_ready():
	print(f"{bot.user} is online!")
	
if __name__ == "__main__":
	for filename in os.listdir("./cogs"):
		if filename.endswith(".py"):
			extension = filename[:-3]
			try:
				bot.load_extension(f"✅ | **cogs.{extension}** has been loaded!")
			except Exception as e:
				exception = f"{type(e), __name__}: {e}"
				print(f"❌ | {extension.capitalize()}!")

bot.run(os.getenv("BOT_TOKEN"))
