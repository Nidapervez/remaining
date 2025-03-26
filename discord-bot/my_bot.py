import os
import discord
from discord.ext import commands
from dotenv import load_dotenv  # Load environment variables

# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv("DISCORD_TOKEN")  # Read token from environment

# Ensure token is found
if not BOT_TOKEN:
    raise ValueError("⚠️ DISCORD_TOKEN is missing. Check your .env file!")

# Enable intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
intents.members = True  # Enable server members intent (if needed)
intents.presences = True  # Enable presence intent (if needed)

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name}")

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Command: Hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"👋 Hello {ctx.author.name}!")

# Command: Echo
@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

# Run the bot
bot.run(BOT_TOKEN)
