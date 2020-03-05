import discord
from discord.ext import tasks, commands
from discord.utils import get
import logging
from logging.handlers import RotatingFileHandler
import time

LOG_CONST = {
    'LOGFILE': 'C:/Users/NAME/source/repos/epicbot/epicbot/discord.log'
    }
def getLogConst(constant):
    return LOG_CONST.get(constant, True)

LOGFILE = getLogConst('LOGFILE')
handler = logging.FileHandler(filename=LOGFILE, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

initial_extensions = ('cogs.skytlzplace',
                      'cogs.error_handling')
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run('MzM2MzU1MDcwMTQ2NzcyOTkz.XdK-AA.D2MdsCZzDMdii0jE05EvzIzJ12Q')
