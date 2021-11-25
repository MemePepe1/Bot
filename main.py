import discord
import os
from requests import Session
import random
from discord.ext import commands
import asyncpraw
import aiohttp

activity = discord.Activity(type=discord.ActivityType.listening, name="Term-I")

client = discord.Client()

prefix = commands.Bot(command_prefix='.', activity=activity,
                      status=discord.Status.online)
prefix.remove_command("help")

prefix.load_extension("cogs.bfun")

reddit = asyncpraw.Reddit(client_id="kAK8l7cBbMtX4avFSj8Vkw",
                          client_secret="T5GYuGKvfHqp2HvHWuayUDtyMMcVPQ",
                          username="DiscordIs_Bad1212",
                          password="Chathere",
                          user_agent="Narayanasucks")


@prefix.command(aliases=['memes', 'm'])
async def meme(ctx):
    subreddit = await reddit.subreddit("memes")
    all_subs = []
    hot = subreddit.hot(limit=50)
    async for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    ups = random_sub.score
    link = random_sub.permalink
    comments = random_sub.num_comments
    embed = discord.Embed(
        title=name, url=f"https://reddit.com{link}", color=ctx.author.color)
    embed.set_image(url=url)
    embed.set_footer(text=f"👍{ups} 💬{comments}")
    await ctx.send(embed=embed)


@prefix.command()
async def anime(ctx):
    subreddit = await reddit.subreddit("AnimeWallpapersSFW")
    all_subs = []
    hot = subreddit.hot(limit=50)
    async for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    ups = random_sub.score
    link = random_sub.permalink
    comments = random_sub.num_comments
    embed = discord.Embed(
        title=name, url=f"https://reddit.com{link}", color=ctx.author.color)
    embed.set_image(url=url)
    embed.set_footer(text=f"👍{ups} 💬{comments}")
    await ctx.send(embed=embed)


@prefix.event
async def on_ready():
    print('I am ready to go.')


@prefix.command()
async def ping(ctx):
    await ctx.send(f'{round(prefix.latency * 1000)}ms')


prefix.run(os.environ['TOKEN'])
