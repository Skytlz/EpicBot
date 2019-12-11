import discord
from discord.ext import commands
import logging
from logging.handlers import RotatingFileHandler
import time

LOG_CONST = {
    'LOGFILE': 'C:/Users/%USERPROFILE%/source/repos/epicbot/epicbot/discord.log'
    }
def getLogConst(constant):
    return LOG_CONST.get(constant, False)

LOGFILE = getLogConst('LOGFILE')
handler = logging.FileHandler(filename=LOGFILE, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
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
        msg = await message.channel.send('pong!')
        end = time.time()
        await msg.edit(content="pong! `{} s`".format(round(end-start, 3)))

    if 'pong' in message.content:
        start = time.time()
        msg = await message.channel.send('ping!')
        end = time.time()
        await msg.edit(content="pong! `{} s`".format(round(end-start, 3)))


client.run('')
