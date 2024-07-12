import discord
from discord.ext import commands
import json

class Handlers(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.server_welcome_channels = {}
        self.server_leave_channels = {}

        # Load saved welcome and leave channel data
        self.load_welcome_channels()
        self.load_leave_channels()

    def load_welcome_channels(self):
        try:
            with open("json/welcome_channels.json", "r") as file:
                self.server_welcome_channels = json.load(file)
        except FileNotFoundError:
            self.server_welcome_channels = {}

    def load_leave_channels(self):
        try:
            with open("json/leave_channels.json", "r") as file:
                self.server_leave_channels = json.load(file)
        except FileNotFoundError:
            self.server_leave_channels = {}

    def save_welcome_channels(self):
        with open("json/welcome_channels.json", "w") as file:
            json.dump(self.server_welcome_channels, file, indent=4)

    def save_leave_channels(self):
        with open("json/leave_channels.json", "w") as file:
            json.dump(self.server_leave_channels, file, indent=4)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild_id = str(member.guild.id)
        if guild_id in self.server_welcome_channels:
            welcome_channel_id = self.server_welcome_channels[guild_id]["channel_id"]
            channel = member.guild.get_channel(welcome_channel_id)
            if channel:
                welcome_message = f"Welcome {member.mention} to our server! We're glad to have you here."
                embed = discord.Embed(title="", color=0x2b2d31)
                embed.add_field(name="", value=f"**<:welcome:1220899596642025534> Welcome in!**\n>>> {welcome_message}", inline=False)
                await channel.send(content="", embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild_id = str(member.guild.id)
        if guild_id in self.server_leave_channels:
            leave_channel_id = self.server_leave_channels[guild_id]["channel_id"]
            channel = member.guild.get_channel(leave_channel_id)
            if channel:
                leave_message = f"Goodbye **{member.name} ({member.id})**! We're sad to see you leave."
                embed = discord.Embed(title="", color=0x2b2d31)
                embed.add_field(name="", value=f"**<:leave:1220899595177955400> Goodbye!**\n>>> {leave_message}", inline=False)
                await channel.send(content="", embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def setwelcomechannel(self, ctx, channel: discord.TextChannel):
        guild_id = str(ctx.guild.id)
        self.server_welcome_channels[guild_id] = {"channel_id": channel.id, "server_name": ctx.guild.name}
        self.save_welcome_channels()

        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> Welcome channel set to {channel.mention}", inline=False)
        await ctx.send(content="", embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def setleavechannel(self, ctx, channel: discord.TextChannel):
        guild_id = str(ctx.guild.id)
        self.server_leave_channels[guild_id] = {"channel_id": channel.id, "server_name": ctx.guild.name}
        self.save_leave_channels()

        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> Leave channel set to {channel.mention}", inline=False)
        await ctx.send(content="", embed=embed)
    
    @commands.command()
    async def setup(self, ctx):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:developer:1220836690206392432> - Set up!**\n\nUse the following commands to setup your server!\n>>> **.setwelcomechannel**\n**.setleavechannel**\n**.setlogchannel**", inline=False)
        await ctx.send(content="", embed=embed)

    @setleavechannel.error
    @setwelcomechannel.error
    async def setwelcomechannel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value="**<:x_:1220836514888548462> - Error!**\n>>> **You don't have the required permissions to use this command.**", inline=False)
            await ctx.send(content="", embed=embed)

async def setup(client):
    await client.add_cog(Handlers(client))