import discord
from discord.ext import commands
import json
import random



class Jenova(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def jenovahelp(self,ctx):
        with open('data/data.json') as d:
            data = json.load(d)
        prefix = data['prefix']

        embed = discord.Embed(title="JENOVA Commands", description="List of functionalities that JENOVA can do.", color=discord.Color.light_grey())
        embed.add_field(name=prefix + "revfact", value="JENOVA gives a random fact about the world of Revenant and its characters.",inline=False)
        embed.add_field(name=prefix + "jenova8ball", value="JENOVA, 8ball style.",inline=False)
        embed.add_field(name=prefix + "revdate", value="JENOVA gives the precise date in the world of Revenant using the real world presentation.", inline=False)
        embed.add_field(name=prefix + "jenovarobot", value="JENOVA temporarily activates her sentience for one response. DO NOT USE THIS COMMAND EXCEPT DURING EVENTS.", inline=False)
        embed.add_field(name=prefix + "userinfo", value="Displays the Revenant user's data or the mentioned user's data.", inline=False)
        embed.add_field(name=prefix+ "changeprefix <symbol>", value="Changes the prefix of JENOVA's commands. Only works for the server owner.", inline=False)
        embed.add_field(name=prefix+ "revsite", value="JENOVA sends a URL link to Revenant's official website.", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def jenova8ball(self, ctx):
        with open('data/data.json') as d:
            data = json.load(d)
        eightball = data['askjenova']
            #print(random.choice(eightball) + str(bot.user.mention) + ".")
        await ctx.send(random.choice(eightball) + ctx.message.author.mention + ".")

    @commands.command()
    async def jenovarobot(ctx):
        await ctx.send("AI Mode has been activated... Awaiting human response.")
        msg = input('> Message to send: ')
        await ctx.send(msg)
        await ctx.send("AI Mode deactivated... Reverting to Bot Mode.")

def setup(bot):
    bot.add_cog(Jenova(bot))
