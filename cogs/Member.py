import discord
from discord.ext import commands
import json






class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def userinfo(self,ctx, member: discord.Member = None):
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

def setup(bot):
    bot.add_cog(Member(bot))
