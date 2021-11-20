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
from aa import *


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command
    async def nlearn(self, ctx):
        await ctx.send("https://nlearn.nspira.in/")

    @commands.command
    async def chalam_sirs_channel(self, ctx):
        await ctx.send('https://www.youtube.com/channel/UCIAj6DCF7fKBzBrexwnjyAw')

    @commands.command(aliases=['t'])
    async def truth(self, ctx):
        await ctx.send(f'Truth: {random.choice(questions_for_truth)}')

    @commands.command(aliases=['d'])
    async def dare(self, ctx):
        # questions_for_dare=["add more dares to play"]
        await ctx.send(f'Dare: {random.choice(questions_for_dare)}')

    # @commands.command()
    # async def ping(self, ctx):
    #       await ctx.send(f'{round(commands.latency * 1000)}ms')

    @commands.command()
    async def list(self, ctx):
        await ctx.send(f'{random.choice(people_in_the_server)}')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question=None):
        if question == None:
            return await ctx.send("`.8ball <ur question>`")
        else:
            await ctx.send(f'Statement: {question}\nPrediction: {random.choice(responses)}')

    @commands.command(aliases=['h'])
    async def help(self, ctx):
        await ctx.send(embed=embed)


def setup(prefix):
    prefix.add_cog(Fun(prefix))