import discord
from discord.ext import commands
import json
import random
from discord.ext import commands
from datetime import datetime
from datetime import date



class Revenant(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def revdate(self,ctx):
        with open('data/data.json') as d:
            data = json.load(d)
        rev_month = data['revenant_months']
        rev_weekday = data['revenant_weekdays']
        month = datetime.today().month
        day = datetime.today().day
        year = datetime.today().year
        weekday = datetime.today().weekday()
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
        #print("Day is " + str(day) + " and month is " + str(month) + " and year is " + str(year))
        date_message = 'Today is ' + rev_weekday[weekday] + ', '+ str(day) + suffix + ' of ' + rev_month[month-1]  + ', Year ' + str(year+81)
        #print(date_message)
        await ctx.send(date_message)

    @commands.command()
    async def revfact(self,ctx):
        with open('data/data.json') as d:
            data = json.load(d)
        rfact = data['revenant_fact']
        await ctx.send(random.choice(rfact))

    @commands.command()
    async def revsite(self, ctx):
        with open('data/data.json') as d:
            data = json.load(d)
        site = data['website']
        embed = discord.Embed(url="https://sites.google.com/view/revenantrp/home")
        await ctx.send(site)



def setup(bot):
    bot.add_cog(Revenant(bot))
