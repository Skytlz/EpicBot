import discord
from discord.ext import commands
import logging
import time

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'ping' in message.content:
        start = time.time()
        await message.channel.send('pong!')
        end = time.time()
        totalT = str(end-start)
        await message.channel.edit.send('pong!' + totalT + 'ms')

    if 'pong' in message.content:
        start = time.time()
        await message.channel.send('ping!')
        end = time.time()
        totalT = str(end-start)
        await message.channel.edit('ping!' + totalT + 'ms')

client.run()
