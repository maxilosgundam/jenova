import discord
import json
import random
import sys
from discord.ext import commands
from datetime import datetime
from datetime import date
from discord import user
import asyncio
import os


async def get_commandprefix(client, message):
    with open('data/data.json') as d:
        data = json.load(d)
    prefix = data['prefix']
    #print("Prefix is " + str(prefix))
    return str(prefix)

bot = commands.Bot(command_prefix=get_commandprefix)
main_channel_id = 649155422049140738
#main_channel_name = 'ooc-talk'
TOKEN = open("TOKEN.txt","r").read()

@bot.event
async def on_ready():
    print('Bot is ready.')
    print(f'> Logged in as: {bot.user}')
    #print(bot.user.id)
    print('-----READY----- \n')


@bot.command()
async def changeprefix(ctx, newprefix):
    with open('data/data.json','r') as d:
        prefixes = json.load(d)

    prefixes['prefix'] = newprefix
    #print("Prefix is " + prefix1)
    #print("New prefix is " + test)
    with open('data/data.json','w') as d:
        json.dump(prefixes, d, indent =4)

    await ctx.send(f'Prefix has been changed to: {newprefix}')




async def change_status():
    await bot.wait_until_ready()
    with open('data/data.json') as d:
        data = json.load(d)
    statuses = data['jenova_status']

    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity=discord.Game(status))
        await asyncio.sleep(15)

for cog in os.listdir(".\\cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py','')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} cannot be loaded:")
            raise e

bot.loop.create_task(change_status())
bot.run(TOKEN)
