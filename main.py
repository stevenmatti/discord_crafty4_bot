import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

# import function to send start/stop minecraft server
from crafty_request_api import minecraft_server_commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8',mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_member_join():
    await member.send(f"Welcome to the server {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - dont use that word!")


    await bot.process_commands(message)


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")


@bot.command()
async def start(ctx): 
    result = minecraft_server_commands("start_server")
    await ctx.send(f"Minecraft Server Started!!")


@bot.command()
async def stop(ctx): 
    result = minecraft_server_commands("stop_server")
    await ctx.send(f"Minecraft Server Stopped!!")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
