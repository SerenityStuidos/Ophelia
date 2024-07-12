import discord
from discord.ext import commands
import datetime

class Community(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title="Server Information", color=0x2b2d31)
        embed.set_thumbnail(url=guild.icon.url)
        embed.add_field(name="", value=f"> **Server Name**: {guild.name}\n> **Server ID**: {guild.id}\n> **Owner**: {guild.owner}\n> **Member Count**: {guild.member_count}", inline=False)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        if member is None:
            member = ctx.author
        elif member is not None:
            member = member
        
        embed = discord.Embed(title="User Information", color=0x2b2d31)
        embed.set_thumbnail(url=member.avatar)
        embed.add_field(name="", value=f">>> **Name**: {member.name}\n**Nickname**: {member.display_name}\n**ID**: {member.id}\n**Top Role**: {member.top_role}\n**Status**: {member.status}\n**Is User?** {member.bot}\n**Creation Date**: {member.created_at.__format__("%A, %d, %B, %Y @ %H:%M:%S")}", inline=False)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        avatar_url = member.avatar.url

        embed = discord.Embed(title=f"{member.display_name}'s Avatar", color=0x2b2d31)
        embed.set_image(url=avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def time(self, ctx):
        now = datetime.datetime.now()
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value="**Time**: <t:1711131060:T>", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def date(self, ctx):
        now = datetime.datetime.now()
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value="**Date**: <t:1711131060:D>", inline=False)
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Community(client))