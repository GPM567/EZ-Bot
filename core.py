import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
import re


client = commands.Bot(command_prefix = 'c.')

status = cycle(['NACL LLC', 'Developing with saltcube'])

@client.event
async def on_ready():
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.online,activity=discord.Game(next(status)))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Reloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('TOKEN HERE')