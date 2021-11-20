import discord
from discord.ext import commands
import random
import asyncio
import youtube_dl
import aiohttp
import time
from discord.utils import get
import nacl
from async_timeout import timeout
from discord.ext import commands
import functools
import itertools
import math
import random
from aa import *

class Music(commands.Cog):
    def __init__(self, bot):
      self.bot=bot

    @commands.command()
    async def join(self,ctx):
      channel = ctx.author.voice.channel
      await channel.connect()
    @commands.command()
    async def leave(self,ctx):
      channel = ctx.author.voice.channel
      await ctx.guild.voice_client.disconnect()

def setup(prefix):
  prefix.add_cog(Music(prefix))