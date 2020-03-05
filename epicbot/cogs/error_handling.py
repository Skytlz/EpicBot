import traceback
import sys
from discord.ext import commands
import discord

class commandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        @commands.Cog.listener()
        async def on_command_error(self, ctx, error):
            ig = (commands.CommandNotFound, commands.UserImputError)
            error = getattr(error, 'original', error)

            if isinstance(error, ig):
                return

            elif isinstance(error, commands.MissingPermissions):
                return await ctx.send('You do not have access to that command.')

def setup(bot):
    bot.add_cog(commandErrorHandler(bot))