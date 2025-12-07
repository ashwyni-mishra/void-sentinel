import discord
from discord.ext import commands
import os
import config

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix=config.PREFIX,
    intents=intents,
    help_command=None  # we will make custom help later
)


# LOAD ALL COGS

@bot.event
async def on_ready():
    print(f"🔥 Void Sentinel Online as {bot.user}")

    # Load basic cogs
    await bot.load_extension("cogs.info")
    await bot.load_extension("cogs.utility")

    # Load all moderation command files
    await bot.load_extension("cogs.moderation")

    print("⚙️ All cogs loaded successfully.")


# Run Bot

TOKEN = os.getenv("BOT_TOKEN")

bot.run(TOKEN)
