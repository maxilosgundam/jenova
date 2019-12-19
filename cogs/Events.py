import discord
from discord.ext import commands
import json
import random

main_channel_id = 649155422049140738

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        with open('data/data.json') as d:
            data = json.load(d)
        join_msg = data['welcome_messages']
        message =  member.name + ' ' + random.choice(join_msg)
        channel = self.bot.get_channel(main_channel_id)
        await channel.send(message)



    @commands.Cog.listener()
    async def on_member_remove(self,member):
        with open('data/data.json') as d:
            data = json.load(d)
        kick_msg = data['kick_messages']
        message =  member.name + ' ' + random.choice(kick_msg)
        channel = self.bot.get_channel(main_channel_id)
        await channel.send(message)

def setup(bot):
    bot.add_cog(Events(bot))
