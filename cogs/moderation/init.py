from discord.ext import commands
import os

async def setup(bot: commands.Bot):
    base = os.path.dirname(__file__)

    for file in os.listdir(base):
        if file.endswith(".py") and file != "__init__.py":
            module = f"cogs.moderation.{file[:-3]}"
            await bot.load_extension(module)
            print(f"⚔️ Loaded moderation command: {file}")
