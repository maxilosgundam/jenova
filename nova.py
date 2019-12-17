import discord
import json
import random
import sys
from discord.ext import commands
from datetime import datetime
from datetime import date
from discord import user

bot = commands.Bot(command_prefix = '=')
main_channel_id = 649155422049140738
main_channel_name = 'ooc-talk'
user = discord.Client()


@bot.event
async def on_ready():
    print('Bot is ready.')
    print(f'> Logged in as: {bot.user}')
    #print(bot.user.id)
    print('-----READY----- \n')







@bot.event
async def on_member_join(member):
    with open('data/data.json') as d:
        data = json.load(d)
    join_msg = data['welcome_messages']
    message =  member.name + ' ' + random.choice(join_msg)
    channel = bot.get_channel(main_channel_id)
    await channel.send(message)

@bot.event
async def on_member_ban(member):
    with open('data/data.json') as d:
        data = json.load(d)
    ban_msg = data['ban_messages']
    message =  member.name + ' ' + random.choice(ban_msg)
    channel = bot.get_channel(main_channel_id)
    await channel.send(message)


@bot.event
async def on_member_remove(member):
    with open('data/data.json') as d:
        data = json.load(d)
    kick_msg = data['kick_messages']
    message =  member.name + ' ' + random.choice(kick_msg)
    channel = bot.get_channel(main_channel_id)
    await channel.send(message)

#@bot.command()
#async def help(ctx):
    #author = ctx.message.author
    #embed = discord.Embed(color = discord.color.orange())
    #embed.set_author(name='help')
    #embed.add_field(name='revfact')
    #await ctx.send(author, embed=embed)

@bot.command()
async def activate(ctx):
    await ctx.send("AI Mode has been activated... Awaiting human response.")
    msg = input('> Message to send: ')
    await ctx.send(msg)
    await ctx.send("AI Mode deactivated... Reverting to Bot Mode.")


@bot.command()
async def askjenova(ctx):
    with open('data/data.json') as d:
        data = json.load(d)
    eightball = data['askjenova']
        #print(random.choice(eightball) + str(bot.user.mention) + ".")
    await ctx.send(random.choice(eightball) + ctx.message.author.mention + ".")

@bot.command()
async def revfact(ctx):
    with open('data/data.json') as d:
        data = json.load(d)
    rfact = data['revenant_fact']
    channel_perms = data['allowed_channels']
    await ctx.send(random.choice(rfact))


@bot.command()
async def revdate(ctx):
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

bot.run('NjU1OTQwNzc3MzQ3NjQ1NTAx.XfbbHw.w9qhwOwByzbfeBazcmofMT4acrc')
