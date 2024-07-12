import discord
from discord.ext import commands, tasks
import os
import asyncio
from itertools import cycle
import time

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents)
client.remove_command("help")

statuses = cycle(["for .help", "servers", "users", "version"])

@client.event
async def on_ready():
    await client.tree.sync()
    print(f"Success: {client.user.name} is connected to Discord!")
    change_status.start()

class SelectHelpMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        web_button = discord.ui.Button(label='Official Website', style=discord.ButtonStyle.url, url='https://imerciless.com/serenity')
        server_button = discord.ui.Button(label='Official Server', style=discord.ButtonStyle.url, url='https://discord.gg/kCdmJ7g22a')
        self.add_item(web_button)
        self.add_item(server_button)

    options = [
        discord.SelectOption(label="Moderation", value="1", description="List of moderation commands."),
        discord.SelectOption(label="Utility", value="2", description="List of utility commands."),
        discord.SelectOption(label="Community", value="3", description="List of community commands."),
        discord.SelectOption(label="Fun & Games", value="4", description="List of fun & games commands."),
        discord.SelectOption(label="Roleplay", value="5", description="List of roleplay commands."),
        discord.SelectOption(label="Economy", value="6", description="List of economy commands."),
    ]

    @discord.ui.select(placeholder="Select an option", options=options)
    async def menu_callback(self, interaction: discord.Interaction, select):
        if select.values[0] == "1":
            embed=discord.Embed(title="<:info:1220836512586010674> - Moderation Commands", color=0x2b2d31)
            embed.add_field(name="", value=f"**Moderation**\n>>> `.ban` - Bans a member from the server.\n`.unban` - Unbans a member from the server.\n`.tempban` - Temporarily bans a member from the server.\n`.kick` - Kicks a user from the server.\n`.clear` - Clears messages from the chat.\n `.warn` - Warns a member.\n `.mute` - Mutes a member.\n `.unmute` - Removes the mute from a member.\n`.tempmute` - Temporarily mutes a member.\n`.giverole` - Gives a user a specific role.\n`.removerole` - Removes a specific role from a member.\n`.lockdown` - Lockdowns a channel.\n`.unlock` - Unlocks a previously locked channel.\n`.slowmode` - Sets a message cooldown.\n`.removeslowmode` - Removes message cooldown.\n`.setup` - Sends you the commands to set up the server.\n`.setwelcomechannel` - Channel for welcome messages.\n`.setleavechannel` - Channel for leave messages.\n`.setlogchannel` - Channel of staff logging.", inline=False)
            embed.set_thumbnail(url=client.user.avatar.url)
            await interaction.response.edit_message(content=None, embed=embed, view=self)
        elif select.values[0] == "2":
            embed=discord.Embed(title="<:info:1220836512586010674> - Utility Commands", color=0x2b2d31)
            embed.add_field(name="", value=f"**Utility**\n>>> `.help` - Displays this embed message.\n `.ping` - Get the bot's response time.\n`.server` - Sends the Serenity Discord server invite.\n`.uptime` - Current bot uptime.\n`.version` - Get's the current discord bot version.\n`.botinfo` - Gets some more info on Serenity\n`.partners` - Displays all OFFICIAL Serenity partners.", inline=False)
            embed.set_thumbnail(url=client.user.avatar.url)
            await interaction.response.edit_message(content=None, embed=embed, view=self)
        elif select.values[0] == "3":
            embed=discord.Embed(title="<:info:1220836512586010674> - Community Commands", color=0x2b2d31)
            embed.add_field(name="", value=f"**Community**\n>>> `.serverinfo` - Displays some info about the server.\n`.userinfo` - Displays info about the user.\n `.avatar` - Gets the user's profile picture.\n `.time` - Gets the local time.\n `.date` - Gets the current date.", inline=False)
            embed.set_thumbnail(url=client.user.avatar.url)
            await interaction.response.edit_message(content=None, embed=embed, view=self)
        elif select.values[0] == "4":
            embed=discord.Embed(title="<:info:1220836512586010674> - Fun & Games Commands", color=0x2b2d31)
            embed.add_field(name="", value=f"**Fun & Games**\n>>> `.joke` - Give a random joke.\n `.facts` - Give a random fact.\n `.eightball` - Give a random response to a question.", inline=False)
            embed.set_thumbnail(url=client.user.avatar.url)
            await interaction.response.edit_message(content=None, embed=embed, view=self)
        elif select.values[0] == "5":
            embed=discord.Embed(title="<:info:1220836512586010674> - Roleplay Commands", color=0x2b2d31)
            embed.add_field(name="", value=f"**Roleplay**\n>>> `.hug`- Hugs someone.\n `.pat` - Pats someone on their head.\n `.slap` - Slap someone across their cheek... ouch.\n`.kiss` - Kisses someone as their best friend... awww <3\n`.handshake` - Shakes someone's hand.\n`.highfive` - Give your besties the largest high five.\n`.cry` - Start crying... aww why you sad?\n`.scream` - Start to scream randomly... you look crazy.\n`.smile` - Smile a creepy smile... you're really scary.\n`.laugh`- Start laughing like a lunatic.\n`.sleep` - Start sleeping, take a nap.\n`.wakeup` - Done sleeping? Just wake up.\n`.sit` - Sit down in a nice comfy chair.\n`.eat` - Eat some yummy food.\n`.travel` - Travel anywhere you like, real or not.\n`.explore` - Explore real or fantasy places!\n`.attack` - Take a swing at your enemies.\n`.dodge` - Dodge an enemy attack.\n`.defend` - Defend you and your team from an attack.\n`.cast` - Cast a spell.", inline=False)
            embed.set_thumbnail(url=client.user.avatar.url)
            await interaction.response.edit_message(content=None, embed=embed, view=self)
        elif select.values[0] == "6":
            embed=discord.Embed(title="<:info:1220836512586010674> - Economy Commands", color=0x2b2d31)
            embed.add_field(name="", value=f"**Economy**\n>>> `.beg` - Beg for money.\n`.balance` - Displays your current balance.\n`.work` - Work hard, get more money.\n`.steal` - Steals money from a member, just don't get caught.\n`.deposit` - Deposit money into your bank.\n`.withdraw` - Withdraw money from your bank.", inline=False)
            embed.set_thumbnail(url=client.user.avatar.url)
            await interaction.response.edit_message(content=None, embed=embed, view=self)

@client.tree.command(name="help", description="Shows ALL the available commands on Serenity.")
async def help(interaction: discord.Interaction):
    embed=discord.Embed(title="", color=0x2b2d31)
    embed.add_field(name="", value=f"**<:info:1220836512586010674> - Help**\n>>> Use the drop down menu below to learn more about my commands!", inline=False)
    embed.set_thumbnail(url=client.user.avatar.url)
    await interaction.response.send_message(content=None,embed=embed, view=SelectHelpMenu())

@tasks.loop(seconds=5)
async def change_status():
    status = next(statuses)
    if status == "servers":
        total_servers = len(client.guilds)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{total_servers} total servers"))
    elif status == "users":
        total_users = sum(guild.member_count for guild in client.guilds)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{total_users} total members"))
    elif status == "version":
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="version 1.00"))
    else:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for .help"))

@client.tree.command(name="ping", description="Shows the bot's response time.")
async def ping(interaction: discord.Interaction):
    start_time = time.time()
    api_latency = round((time.time() - start_time) * 1000)
    bot_latency = round(client.latency * 1000)

    if bot_latency < 1:
        emoji_wifi = "<:wifi_0:1220836574099542046>"
    elif bot_latency >= 200:
        emoji_wifi = "<:wifi_1:1220836572950433792>"
    elif bot_latency >= 100:
        emoji_wifi = "<:wifi_2:1220836571801059458>"
    elif bot_latency >= 1:
        emoji_wifi = "<:wifi_3:1220836570349834281>"

    if api_latency < 1:
        emoji_api = "<:wifi_0:1220836574099542046>"
    elif api_latency >= 200:
        emoji_api = "<:wifi_1:1220836572950433792>"
    elif api_latency >= 100:
        emoji_api = "<:wifi_2:1220836571801059458>"
    elif api_latency >= 1:
        emoji_api = "<:wifi_3:1220836570349834281>"

    embed=discord.Embed(title="", color=0x2b2d31)
    embed.add_field(name="", value=f">>> {emoji_wifi} **Response**: {bot_latency}ms\n{emoji_api} **API**: {api_latency}ms\n<:x_:1220836514888548462> **Proxy -> Client**: `Not Implemented`", inline=False)
    await interaction.response.send_message(content="", embed=embed)

# @client.tree.command(name="help", description="Shows ALL the available commands on Serenity.")
# async def help(interaction: discord.Interaction):
#         embed=discord.Embed(title="<:info:1220836512586010674> - Command list", color=0x2b2d31)
#         embed.add_field(name="", value=f"**Moderation**\n>>> `.ban` - Bans a member from the server.\n`.unban` - Unbans a member from the server.\n`.tempban` - Temporarily bans a member from the server.\n`.kick` - Kicks a user from the server.\n`.clear` - Clears messages from the chat.\n `.warn` - Warns a member.\n `.mute` - Mutes a member.\n `.unmute` - Removes the mute from a member.\n`.tempmute` - Temporarily mutes a member.\n`.giverole` - Gives a user a specific role.\n`.removerole` - Removes a specific role from a member.\n`.lockdown` - Lockdowns a channel.\n`.unlock` - Unlocks a previously locked channel.\n`.slowmode` - Sets a message cooldown.\n`.removeslowmode` - Removes message cooldown.\n`.setup` - Sends you the commands to set up the server.\n`.setwelcomechannel` - Channel for welcome messages.\n`.setleavechannel` - Channel for leave messages.\n`.setlogchannel` - Channel of staff logging.", inline=False)
#         embed.add_field(name="", value=f"**Utility**\n>>> `.help` - Displays this embed message.\n `.ping` - Get the bot's response time.\n`.server` - Sends the Serenity Discord server invite.\n`.uptime` - Current bot uptime.\n`.version` - Get's the current discord bot version.\n`.botinfo` - Gets some more info on Serenity", inline=False)
#         embed.add_field(name="", value=f"**Community**\n>>> `.serverinfo` - Displays some info about the server.\n`.userinfo` - Displays info about the user.\n `.avatar` - Gets the user's profile picture.\n `.time` - Gets the local time.\n `.date` - Gets the current date.", inline=False)
#         embed.add_field(name="", value=f"**Fun & Games**\n>>> `.joke` - Give a random joke.\n `.facts` - Give a random fact.\n `.eightball` - Give a random response to a question.", inline=False)
#         embed.add_field(name="", value=f"**Roleplay**\n>>> `.hug`- Hugs someone.\n `.pat` - Pats someone on their head.\n `.slap` - Slap someone across their cheek... ouch.\n`.kiss` - Kisses someone as their best friend... awww <3\n`.handshake` - Shakes someone's hand.\n`.highfive` - Give your besties the largest high five.\n`.cry` - Start crying... aww why you sad?\n`.scream` - Start to scream randomly... you look crazy.\n`.smile` - Smile a creepy smile... you're really scary.\n`.laugh`- Start laughing like a lunatic.\n`.sleep` - Start sleeping, take a nap.\n`.wakeup` - Done sleeping? Just wake up.\n`.sit` - Sit down in a nice comfy chair.\n`.eat` - Eat some yummy food.\n`.travel` - Travel anywhere you like, real or not.\n`.explore` - Explore real or fantasy places!\n`.attack` - Take a swing at your enemies.\n`.dodge` - Dodge an enemy attack.\n`.defend` - Defend you and your team from an attack.\n`.cast` - Cast a spell.", inline=False)
#         embed.add_field(name="", value=f"**Economy**\n>>> `.beg` - Beg for money.\n`.balance` - Displays your current balance.\n`.work` - Work hard, get more money.\n`.steal` - Steals money from a member, just don't get caught.\n`.deposit` - Deposit money into your bank.\n`.withdraw` - Withdraw money from your bank.", inline=False)
#         embed.set_thumbnail(url=client.user.avatar.url)
#         await interaction.response.send_message(content="", embed=embed)

@client.tree.command(name="botinfo", description="Shows some info on Serenity.")
async def botinfo(interaction: discord.Interaction):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:star:1220836693221834884> - About Serenity!**\n>>> **Version**: v1.00\n**Commands**: 50+\n**Creator**: <@746808861066788895>", inline=False)
        await interaction.response.send_message(content="", embed=embed)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value="**<:x_:1220836514888548462> - Error!**\n>>> **You don't have the required permissions to use this command.**", inline=False)
        await ctx.send(content="", embed=embed)

    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value="**<:x_:1220836514888548462> - Error!**\n>>> **You are missing arguements for this command.**", inline=False)
        await ctx.send(content="", embed=embed)

    if isinstance(error, discord.Forbidden):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value="**<:x_:1220836514888548462> - Error!**\n>>> **I don't have permission to run this command.**", inline=False)
        await ctx.send(content="", embed=embed)
    
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value="**<:x_:1220836514888548462> - Error!**\n>>> **You don't have the correct role to run this command.**", inline=False)
        await ctx.send(content="", embed=embed)
    
    if isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value="**<:x_:1220836514888548462> - Error!**\n>>> **I don't have permission to run this command.**", inline=False)
        await ctx.send(content="", embed=embed)

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"Success: The cog, {filename[:-3]} has been loaded!")

async def main():
    await load()
    await client.start("BOT_TOKEN_HERE")

asyncio.run(main())
