import discord
from discord.ext import commands
import json
import random




class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self,member):
        with open('data/data.json') as d:
            data = json.load(d)
        join_msg = data['welcome_messages']
        main_channel_id = data['main_channel_id']
        message =  member.name + ' ' + random.choice(join_msg)
        channel = self.bot.get_channel(main_channel_id)
        await channel.send(message)



    @commands.Cog.listener()
    async def on_member_remove(self,member):
        with open('data/data.json') as d:
            data = json.load(d)
        kick_msg = data['kick_messages']
        main_channel_id = data['main_channel_id']
        message =  member.name + ' ' + random.choice(kick_msg)
        channel = self.bot.get_channel(main_channel_id)
        await channel.send(message)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You do not have the permission.")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Invalid command.")

        raise error

def setup(bot):
    bot.add_cog(Events(bot))
