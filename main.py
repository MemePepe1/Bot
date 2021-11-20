import discord
from discord.ext import commands
import random
import asyncio
import youtube_dl
import aiohttp
import time
from discord.utils import get
from async_timeout import timeout
from discord.ext import commands
import functools
import itertools
import math
import random

activity = discord.Activity(type=discord.ActivityType.playing, name="Minecraft")

client = discord.Client()
client = commands.Bot

prefix = commands.Bot(command_prefix='.', activity=activity, status=discord.Status.online)
prefix.remove_command("help")

prefix.load_extension("cogs.fun")
prefix.load_extension("cogs.music")


@prefix.event
async def on_ready():
    print('I am ready to go.')


@prefix.command()
async def ping(ctx):
    await ctx.send(f'{round(prefix.latency * 1000)}ms')


prefix.run('OTA5ODI3NDI5NjU1MjY5NDY2.YZJ80w.fA4VEAgnH84wxzxkfjNZ-DhWJ5o')
