import discord
from discord.ext import commands
import config

async def process_vs_command(bot, msg: discord.Message):
    if msg.author.bot:
        return
    
    content = msg.content.strip()

    # must start with "vs "
    if not content.lower().startswith(config.VS_TRIGGER + " "):
        return

    parts = content.split()
    if len(parts) < 2:
        return await msg.reply("❗ Use **vs help** to see all commands.")

    # Extract command and arguments
    command = parts[1].lower()
    params = parts[2:]

    # Convert VS command to prefix command internally
    new_message = f"{config.PREFIX}{command}"

    if params:
        new_message += " " + " ".join(params)

    # Create a fake message object for prefix command processing
    fake_msg = msg
    fake_msg.content = new_message

    ctx = await bot.get_context(fake_msg)
    await bot.invoke(ctx)


def setup_vs_listener(bot: commands.Bot):
    @bot.listen("on_message")
    async def vs_listener(msg: discord.Message):
        await process_vs_command(bot, msg)
