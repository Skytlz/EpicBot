from discord.ext import commands
import difflib
import discord
import asyncio
import time
import re


class skytlzPlace(commands.Cog):
   def __init__(self, bot):
       self.bot = bot

   @commands.command()
   async def role(self, ctx, r: str):
       member = ctx.message.author
       if not r:
           await ctx.send('Role not Specified')
       else:
           t = member.guild.roles
           names = re.findall("'(.*?)'", str(t))
           x = difflib.get_close_matches(r, names)
           if not x:
               await ctx.send("Role does not exist")
           else:
               print(x[0])
               y = discord.utils.get(member.guild.roles, name=x[0])
               w = discord.utils.get(member.roles, name=x[0])
               if w is y:
                   await member.remove_roles(y)
                   await ctx.send('You no longer have the `{}` role.'.format(str(y)))
               else:
                   await member.add_roles(y)
                   await ctx.send('You now have the `{}` role.'.format(str(y)))
               if(commands.MissingPermissions):
                   await ctx.send("You dont have access to this role.")

   @commands.command()
   async def remind(self, ctx):
       await ctx.send("joe")

   @commands.command()
   async def sam(self, ctx):
       await ctx.send("https://tenor.com/view/samhyde-surprised-smug-milliondollarextreme-world-gif-9838550")

   @commands.command()
   async def ping(self, ctx):
       start = time.time()
       msg = await ctx.send('pong!')
       end = time.time()
       await msg.edit(content='pong! `{}s`'.format(round(end-start,3)))

   @commands.command()
   async def pong(self, ctx):
       start = time.time()
       msg = await ctx.send('ping!')
       end = time.time()
       await msg.edit(content='ping! `{}s`'.format(round(end-start,3)))


def setup(bot):
    bot.add_cog(skytlzPlace(bot))
