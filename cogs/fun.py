import discord
from discord.ext import commands
import random
import asyncio
import youtube_dl
import numpy
import aiohttp
import time
from discord.utils import get
from async_timeout import timeout
from discord.ext import commands
import functools
import itertools
import math
import random
from adatabase import *


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nlearn(self, ctx):
        await ctx.send("https://nlearn.nspira.in/")

    @commands.command(aliases=["channel", "cc"])
    async def chalam_sirs_channel(self, ctx):
        await ctx.send('https://www.youtube.com/channel/UCIAj6DCF7fKBzBrexwnjyAw')

    @commands.command(aliases=['t'])
    async def truth(self, ctx):
        await ctx.send(f'Truth: {random.choice(questions_for_truth)}')

    @commands.command(aliases=['d'])
    async def dare(self, ctx):
        await ctx.send(f'Dare: {random.choice(questions_for_dare)}')

    @commands.command()
    async def list(self, ctx):
        await ctx.send(embed=people_embed)

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question=None):
        if question is None:
            return await ctx.send("`.8ball <ur question>`")
        else:
            await ctx.send(f'Statement: {question}\nPrediction: {random.choice(responses)}')

    @commands.command(aliases=['h'])
    async def help(self, ctx):
        await ctx.send(embed=embed)

    # @commands.command(aliases=["i","info"])
    # async def whois(self, ctx,*,whois):
    #   if whois not in ids:
    #     await ctx.send("¯\_(ツ)_/¯")

    #   i=0
    #   for i in range(0,len(ids)):
    #     if whois==ids[i]:
    #       await ctx.send(names[i])
    #     i+=1
    @commands.command(aliases=["whois"])
    async def userinfo(ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author


def setup(prefix):
    prefix.add_cog(Fun(prefix))
