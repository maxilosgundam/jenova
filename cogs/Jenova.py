import discord
import json
import random
from datetime import datetime
from datetime import date
from discord.ext import commands

class Jenova(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command()
        async def userinfo(self, ctx, member: discord.Member = None):
            member = ctx.author if not member else member
            roles = [role for role in member.roles]
            await ctx.send("Scanning user..")
            embed = discord.Embed(color=member.color, description="---REVENANT MEMBER DATABASE RECORD---")
            embed.set_author(name=f"{member}")
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Revenant Name: ", value=member.display_name)
            embed.add_field(name="Joined Revenant on ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"))
            embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
            embed.add_field(name="Online Status: ", value=member.status)
            await ctx.send(embed=embed)


        @commands.command()
        async def jenovahelp(self, ctx):
            embed = discord.Embed(title="JENOVA Commands", description="List of functionalities that JENOVA can do.", color=discord.Color.light_grey())
            embed.add_field(name=command_prefix + "revfact", value="JENOVA gives a random fact about the world of Revenant and its characters.")
            embed.add_field(name=command_prefix + "jenova8ball", value="JENOVA, 8ball style.")
            embed.add_field(name=command_prefix + "revdate", value="JENOVA gives the precise date in the world of Revenant using the real world presentation.")
            embed.add_field(name=command_prefix + "jenovarobot", value="JENOVA temporarily activates her sentience for one response. DO NOT USE THIS COMMAND EXCEPT DURING EVENTS.")
            embed.add_field(name=command_prefix + "userinfo", value="Displays the Revenant user's data or the mentioned user's data.")
            await ctx.send(embed=embed)


        @commands.command()
        async def jenovarobot(self, ctx):
            await ctx.send("AI Mode has been activated... Awaiting human response.")
            msg = input('> Message to send: ')
            await ctx.send(msg)
            await ctx.send("AI Mode deactivated... Reverting to Bot Mode.")


        @commands.command()
        async def jenova8ball(self, ctx):
            with open('data/data.json') as d:
                data = json.load(d)
            eightball = data['askjenova']
                #print(random.choice(eightball) + str(bot.user.mention) + ".")
            await ctx.send(random.choice(eightball) + ctx.message.author.mention + ".")


def setup(bot):
    bot.add_cog(Jenova(bot))
