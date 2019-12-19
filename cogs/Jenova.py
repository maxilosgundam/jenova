import discord
from discord.ext import commands
import json
import random

main_channel_id = 649155422049140738

class Jenova(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def jenovahelp(self,ctx):
        embed = discord.Embed(title="JENOVA Commands", description="List of functionalities that JENOVA can do.", color=discord.Color.light_grey())
        embed.add_field(name=command_prefix + "revfact", value="JENOVA gives a random fact about the world of Revenant and its characters.")
        embed.add_field(name=command_prefix + "jenova8ball", value="JENOVA, 8ball style.")
        embed.add_field(name=command_prefix + "revdate", value="JENOVA gives the precise date in the world of Revenant using the real world presentation.")
        embed.add_field(name=command_prefix + "jenovarobot", value="JENOVA temporarily activates her sentience for one response. DO NOT USE THIS COMMAND EXCEPT DURING EVENTS.")
        embed.add_field(name=command_prefix + "userinfo", value="Displays the Revenant user's data or the mentioned user's data.")
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
