import discord
import json
import random
import sys
from discord.ext import commands
from datetime import datetime
from datetime import date
from discord import user
import asyncio

command_prefix = '='
bot = commands.Bot(command_prefix)
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
async def on_member_remove(member):
    with open('data/data.json') as d:
        data = json.load(d)
    kick_msg = data['kick_messages']
    message =  member.name + ' ' + random.choice(kick_msg)
    channel = bot.get_channel(main_channel_id)
    await channel.send(message)

@bot.command()
async def userinfo(ctx, member: discord.Member = None):
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


@bot.command()
async def jenovahelp(ctx):
    embed = discord.Embed(title="JENOVA Commands", description="List of functionalities that JENOVA can do.", color=discord.Color.light_grey())
    embed.add_field(name=command_prefix + "revfact", value="JENOVA gives a random fact about the world of Revenant and its characters.")
    embed.add_field(name=command_prefix + "askjenova", value="JENOVA, 8ball style.")
    embed.add_field(name=command_prefix + "revdate", value="JENOVA gives the precise date in the world of Revenant using the real world presentation.")
    embed.add_field(name=command_prefix + "activate", value="JENOVA temporarily activates her sentience for one response. DO NOT USE THIS COMMAND EXCEPT DURING EVENTS.")
    embed.add_field(name=command_prefix + "userinfo", value="Displays the Revenant user's data or the mentioned user's data.")
    await ctx.send(embed=embed)


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

async def change_status():
    await bot.wait_until_ready()
    with open('data/data.json') as d:
        data = json.load(d)
    statuses = data['jenova_status']

    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity=discord.Game(status))
        await asyncio.sleep(10)


bot.loop.create_task(change_status())
bot.run()
