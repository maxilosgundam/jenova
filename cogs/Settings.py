import discord
from discord.ext import commands
import json




async def is_guild_owner(ctx):
    return ctx.author.id == ctx.guild.owner.id

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.check(is_guild_owner)
    async def changeprefix(self, ctx,*, newprefix):
        with open('data/data.json','r') as d:
            prefixes = json.load(d)

        prefixes['prefix'] = newprefix
        #print("Prefix is " + prefix1)
        #print("New prefix is " + test)
        with open('data/data.json','w') as d:
            json.dump(prefixes, d, indent =4)

        await ctx.send(f'Prefix has been changed to: {newprefix}')

    @commands.command()
    @commands.check(is_guild_owner)
    async def reload(self,ctx, cog):
        try:
            self.bot.unload_extension(f"cogs.{cog}")
            self.bot.load_extension(f"cogs.{cog}")
            await ctx.send(f"{cog} has been reloaded.")
        except:
            print(f"{cog} can not be loaded:")
            raise e

def setup(bot):
    bot.add_cog(Settings(bot))
