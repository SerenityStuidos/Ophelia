import discord
from discord.ext import commands
import time
import asyncio
import datetime

class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        start_time = time.time()
        message = await ctx.send("Pinging...")
        api_latency = round((time.time() - start_time) * 1000)
        bot_latency = round(self.client.latency * 1000)

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
        await message.edit(content="", embed=embed)
    
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="<:info:1220836512586010674> - Command list", color=0x2b2d31)
        embed.add_field(name="", value=f"**Moderation**\n>>> `.ban` - Bans a member from the server.\n`.unban` - Unbans a member from the server.\n`.tempban` - Temporarily bans a member from the server.\n`.kick` - Kicks a user from the server.\n`.clear` - Clears messages from the chat.\n `.warn` - Warns a member.\n `.mute` - Mutes a member.\n `.unmute` - Removes the mute from a member.\n`.tempmute` - Temporarily mutes a member.\n`.giverole` - Gives a user a specific role.\n`.removerole` - Removes a specific role from a member.\n`.lockdown` - Lockdowns a channel.\n`.unlock` - Unlocks a previously locked channel.\n`.slowmode` - Sets a message cooldown.\n`.removeslowmode` - Removes message cooldown.\n`.setup` - Sends you the commands to set up the server.\n`.setwelcomechannel` - Channel for welcome messages.\n`.setleavechannel` - Channel for leave messages.\n`.setlogchannel` - Channel of staff logging.", inline=False)
        embed.add_field(name="", value=f"**Utility**\n>>> `.help` - Displays this embed message.\n `.ping` - Get the bot's response time.\n`.server` - Sends the Serenity Discord server invite.\n`.uptime` - Current bot uptime.\n`.version` - Get's the current discord bot version.\n`.botinfo` - Gets some more info on Serenity\n`.partners` - Displays all OFFICIAL Serenity partners.", inline=False)
        embed.add_field(name="", value=f"**Community**\n>>> `.serverinfo` - Displays some info about the server.\n`.userinfo` - Displays info about the user.\n `.avatar` - Gets the user's profile picture.\n `.time` - Gets the local time.\n `.date` - Gets the current date.", inline=False)
        embed.add_field(name="", value=f"**Fun & Games**\n>>> `.joke` - Give a random joke.\n `.facts` - Give a random fact.\n `.eightball` - Give a random response to a question.", inline=False)
        embed.add_field(name="", value=f"**Roleplay**\n>>> `.hug`- Hugs someone.\n `.pat` - Pats someone on their head.\n `.slap` - Slap someone across their cheek... ouch.\n`.kiss` - Kisses someone as their best friend... awww <3\n`.handshake` - Shakes someone's hand.\n`.highfive` - Give your besties the largest high five.\n`.cry` - Start crying... aww why you sad?\n`.scream` - Start to scream randomly... you look crazy.\n`.smile` - Smile a creepy smile... you're really scary.\n`.laugh`- Start laughing like a lunatic.\n`.sleep` - Start sleeping, take a nap.\n`.wakeup` - Done sleeping? Just wake up.\n`.sit` - Sit down in a nice comfy chair.\n`.eat` - Eat some yummy food.\n`.travel` - Travel anywhere you like, real or not.\n`.explore` - Explore real or fantasy places!\n`.attack` - Take a swing at your enemies.\n`.dodge` - Dodge an enemy attack.\n`.defend` - Defend you and your team from an attack.\n`.cast` - Cast a spell.", inline=False)
        embed.add_field(name="", value=f"**Economy**\n>>> `.beg` - Beg for money.\n`.balance` - Displays your current balance.\n`.work` - Work hard, get more money.\n`.steal` - Steals money from a member, just don't get caught.\n`.deposit` - Deposit money into your bank.\n`.withdraw` - Withdraw money from your bank.", inline=False)
        embed.set_thumbnail(url=ctx.bot.user.avatar.url)
        await ctx.send(content="", embed=embed)

    @commands.command()
    async def server(self, ctx):
        embed=discord.Embed(title="<:announcement:1220836650934997002> - Serenity", color=0x2b2d31)
        embed.add_field(name="", value=f"**Hey! I heard that you wanted to join my server!**\n>>> https://discord.gg/ZUAxmYTxqA", inline=False)
        embed.set_thumbnail(url=ctx.bot.user.avatar.url)
        await ctx.send(content="", embed=embed)
    
    @commands.command()
    async def partners(self, ctx):
        embed=discord.Embed(title="<:announcement:1220836650934997002> - Serenity Partners", color=0x2b2d31)
        embed.add_field(name="", value=f"**Check out these AMAZING Partners!**\n>>> iMerciless's Community: https://discord.gg/Awe53Pe8Yu", inline=False)
        embed.set_thumbnail(url=ctx.bot.user.avatar.url)
        await ctx.send(content="", embed=embed)

    @commands.command()
    async def rules(self, ctx):
        developer_role_id = 1221959429902303353
        if discord.utils.get(ctx.author.roles, id=developer_role_id):
            embed_rules = discord.Embed(title="", color=0x2b2d31)
            embed_rules.add_field(name="", value="**<:blank:1220847591613530222>-<:blank:1220847591613530222> Rules**\n\n>>> ﹒Follow guidelines & ToS\n﹒No advertising & hate speech\n﹒No NSFW & gore\n﹒Use common sense\n﹒Ear piercing media in VC should not be used.\n﹒No toxicity or disrespect toward other members.", inline=False)

            embed_links = discord.Embed(title="", color=0x2b2d31)
            embed_links.add_field(name="", value="﹒https://discord.com/guidelines\n﹒https://discord.com/terms\n﹒https://support.discord.com", inline=False)

            embed_reaction = discord.Embed(title="", color=0x2b2d31)
            embed_reaction.add_field(name="", value="**<:blank:1220847591613530222>-<:blank:1220847591613530222> Updates**\n>>> **React below to be pinged for updates**", inline=False)

            await ctx.send(embed=embed_rules)
            await ctx.send(embed=embed_links)
            message_reaction = await ctx.send(embed=embed_reaction)

            await message_reaction.add_reaction("<:plus:1220836569426956369>") 

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == "<:plus:1220836569426956369>" and reaction.message == message_reaction

            try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=60.0, check=check)
            except asyncio.TimeoutError:
                pass 
            else:
                role_id = 1220891389274099784
                role = discord.utils.get(ctx.guild.roles, id=role_id)
                if role:
                    if role in user.roles:
                        await user.remove_roles(role)
                    else:
                        await user.add_roles(role)
        else:
            embed = discord.Embed(title="Insufficient Permissions", description="You need to have the `developer` role to use this command.", color=0xFF0000)
            await ctx.send(embed=embed)

    start_time = datetime.datetime.now()

    @commands.command()
    async def uptime(self, ctx):
        current_time = datetime.datetime.now()
        uptime = current_time - self.start_time
        seconds = uptime.total_seconds()
        days = seconds // (24 * 3600)
        hours = (seconds % (24 * 3600)) // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        uptime_str = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:info:1220836512586010674> - Discord Bot Uptime!**\n>>> Uptime: {uptime_str}", inline=False)
        await ctx.send(content="", embed=embed)

    @commands.command()
    async def version(self, ctx):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:star:1220836693221834884> - Serenity Version!**\n>>> Version: v1.00\nThe initial release of Serenity!", inline=False)
        await ctx.send(content="", embed=embed)
    
    @commands.command()
    async def botinfo(self, ctx):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:star:1220836693221834884> - About Serenity!**\n>>> **Version**: v1.00\n**Commands**: 50+\n**Creator**: <@746808861066788895>", inline=False)
        await ctx.send(content="", embed=embed)

async def setup(client):
    await client.add_cog(Utilities(client))