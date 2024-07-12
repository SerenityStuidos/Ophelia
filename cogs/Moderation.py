import discord
from discord.ext import commands
import asyncio

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        if amount <= 0:
            await ctx.send("Please provide a positive number of messages to delete.")
            return

        await ctx.channel.purge(limit=amount + 1)
        embed=discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> Deleted **{amount}** message(s).", inline=False)
        await ctx.send(content="", embed=embed)
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value="**<:x_:1220836514888548462> - Error!**\n>>> You cannot warn yourself silly.", inline=False)
            await ctx.send(content="", embed=embed)
            return
        
        if member is None:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value="**>>> Please provide a member to warn.**", inline=False)
            await ctx.send(content="", embed=embed)
            return

        if reason is None:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value="**>>> Please provide a reason for the warn.**", inline=False)
            await ctx.send(content="", embed=embed)
            return

        try:
            embed_dm = discord.Embed(title=f"You have been warned in {ctx.guild.name}", description=f"Reason: {reason}", color=discord.Color.orange())
            embed_dm.set_footer(text=f"Warned by {ctx.author}")
            
            await member.send(embed=embed_dm)
        except discord.Forbidden:
            await ctx.send(f"Failed to send a warning DM to {member.mention}. They may have DMs disabled.")
        except Exception as e:
            await ctx.send(f"An error occurred while sending a warning DM to {member.mention}: {e}")

        try:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n**{member}** has been warned for: **{reason}**", inline=False)
            
            await ctx.send(content="", embed=embed)
        except discord.Forbidden:
            await ctx.send("Failed to send a confirmation message. Please check the bot's permissions.")
        except Exception as e:
            await ctx.send(f"An error occurred while sending a confirmation message: {e}")
    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member):
        if member == ctx.author:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value="**<:x_:1220836514888548462> - Error!**\n>>> You cannot mute yourself silly.", inline=False)
            await ctx.send(content="", embed=embed)
            return
        
        if not member:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value="**<:x_:1220836514888548462> - Error!**\nPlease mention a valid member to mute.", inline=False)
            await ctx.send(content="", embed=embed)
            return

        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value="**<:x_:1220836514888548462> - Error!**\n>>> There is no 'Muted' role on this server. Please create one.", inline=False)
            await ctx.send(content="", embed=embed)
            return

        if muted_role in member.roles:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:x_:1220836514888548462> - Error!**\n>>> {member.mention} is already muted.", inline=False)
            await ctx.send(content="", embed=embed)
            return
        
        await member.add_roles(muted_role)
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> {member.mention} has been muted.", inline=False)
        await ctx.send(content="", embed=embed)
    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        if member == ctx.author:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value="**<:x_:1220836514888548462> - Error!**\n>>> You unmuted yourself... wait... if you sent the command, then how were you muted?", inline=False)
            await ctx.send(content="", embed=embed)
            return
        if not member:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value="**<:x_:1220836514888548462> - Error!**\nPlease mention a valid member to mute.", inline=False)
            await ctx.send(content="", embed=embed)
            return

        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value="**<:x_:1220836514888548462> - Error!**\n>>> There is no 'Muted' role on this server. Please create one.", inline=False)
            await ctx.send(content="", embed=embed)
            return

        if muted_role not in member.roles:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:x_:1220836514888548462> - Error!**\n>>> {member.mention} is not muted.", inline=False)
            await ctx.send(content="", embed=embed)
            return

        await member.remove_roles(muted_role)
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> {member.mention} has been unmuted.", inline=False)
        await ctx.send(content="", embed=embed)
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            await ctx.send("You cannot ban yourself.")
            return
        
        if reason is None:
            reason = "No reason provided"
        
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> {member.mention} has been banned for {reason}", inline=False)
            await ctx.send(content="", embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have permissions to ban members.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member_id):
        user = discord.Object(id=member_id)
        await ctx.guild.unban(user)
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> {member_id} has been unbanned.", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def tempban(self, ctx, member: discord.Member, duration: int, *, reason=None):
        if member == ctx.author:
            await ctx.send("You cannot ban yourself.")
            return
        
        if reason is None:
            reason = "No reason provided"

        duration_seconds = duration * 60
        
        try:
            await ctx.guild.ban(member, reason=reason)
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> {member.mention} has been temporary banned for {reason}.\nBan time: {duration} minutes", inline=False)
            await ctx.send(content="", embed=embed)
            
            await asyncio.sleep(duration_seconds)
            await ctx.guild.unban(member)
            await ctx.send(f"{member.mention} has been unbanned after {duration} minutes.")
        except discord.Forbidden:
            await ctx.send("I don't have permissions to ban members.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def tempmute(self, ctx, member: discord.Member, duration: int):
        if member == ctx.author:
            await ctx.send("You cannot mute yourself.")
            return
        
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            await ctx.send("There is no 'Muted' role on this server. Please create one.")
            return

        duration_seconds = duration * 60
        
        if muted_role in member.roles:
            await ctx.send(f"{member.mention} is already muted.")
            return
        
        try:
            await member.add_roles(muted_role)
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> {member.mention} has been temporary muted.\nMute Time: {duration} minutes", inline=False)
            await ctx.send(content="", embed=embed)

            await asyncio.sleep(duration_seconds)
            await member.remove_roles(muted_role)
            await ctx.send(f"{member.mention} has been unmuted after {duration} minutes.")
        except discord.Forbidden:
            await ctx.send("I don't have permissions to manage roles.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def giverole(self, ctx, member: discord.Member, role: discord.Role):
        if role in member.roles:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:x_:1220836514888548462> - Error!**\n>>> {member.mention} already has the {role.name} role.", inline=False)
            await ctx.send(content="", embed=embed)

        else:
            await member.add_roles(role)
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> Added the {role.name} role to {member.mention}.", inline=False)
            await ctx.send(content="", embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):
        if role not in member.roles:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:x_:1220836514888548462> - Error!**\n>>> {member.mention} doesn't have the {role.name} role.", inline=False)
            await ctx.send(content="", embed=embed)
        else:
            await member.remove_roles(role)
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> Removed the {role.name} role from {member.mention}.", inline=False)
            await ctx.send(content="", embed=embed)
    
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lockdown(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> This channel has been locked down by: {ctx.author.mention}.", inline=False)
        await ctx.send(content="", embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> This channel has been unlocked by: {ctx.author.mention}.", inline=False)
        await ctx.send(content="", embed=embed)
    
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> Slow mode set to {seconds} seconds by: {ctx.author.mention}", inline=False)
        await ctx.send(content="", embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def removeslowmode(self, ctx):
        await ctx.channel.edit(slowmode_delay=False)
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:check:1220836540108767253> - Success!**\n>>> Slow mode was removed by: {ctx.author.mention}", inline=False)
        await ctx.send(content="", embed=embed)

async def setup(client):
    await client.add_cog(Moderation(client))
