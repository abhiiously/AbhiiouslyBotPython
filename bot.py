# bot.py
# Made by Abhishek Bhatia
# Works on Python 3.8+
# A simple Discord bot that responds to a ping command.

import os
import discord
from discord.ext import commands

# Create a new instance of the bot with a command prefix
bot = commands.Bot(command_prefix='!')

# Event handler when the bot has connected to the server
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

# Command handler for the 'ping' command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Start the bot using the token from the environment variables
bot.run(os.getenv('DISCORD_TOKEN'))
