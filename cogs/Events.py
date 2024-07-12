import discord
from discord.ext import commands
import json

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.log_channels = {}
        self.load_log_channels()

    def load_log_channels(self):
        try:
            with open("json/log_channels.json", "r") as file:
                self.log_channels = json.load(file)
        except FileNotFoundError:
            self.log_channels = {}

    def save_log_channels(self):
        with open("json/log_channels.json", "w") as file:
            json.dump(self.log_channels, file, indent=4)

    async def log_to_channel(self, guild_id, log_content):
        if guild_id in self.log_channels:
            log_channel_id = self.log_channels[guild_id]
            log_channel = self.client.get_channel(log_channel_id)
            if log_channel:
                embed = discord.Embed(title="", color=0x2b2d31)
                embed.add_field(name="", value=f"**<:code:1220836688952168529> - Logged!**\n>>> {log_content}", inline=False)
                await log_channel.send(content="", embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setlogchannel(self, ctx, channel: discord.TextChannel):
        self.log_channels[str(ctx.guild.id)] = channel.id
        self.save_log_channels()
        await ctx.send(f"Log channel set to {channel.mention}.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        log_content = f"**Member Joined:** {member.mention}"
        await self.log_to_channel(str(member.guild.id), log_content)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        log_content = f"**Member Left:** {member.mention}"
        await self.log_to_channel(str(member.guild.id), log_content)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        log_content = f"**Member Banned:** {user.mention}"
        await self.log_to_channel(str(guild.id), log_content)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        log_content = f"**Member Unbanned:** {user.mention}"
        await self.log_to_channel(str(guild.id), log_content)

    @commands.Cog.listener()
    async def on_member_mute(self, member):
        log_content = f"**Member Muted:** {member.mention}"
        await self.log_to_channel(str(member.guild.id), log_content)

    @commands.Cog.listener()
    async def on_member_unmute(self, member):
        log_content = f"**Member Unmuted:** {member.mention}"
        await self.log_to_channel(str(member.guild.id), log_content)

    @commands.Cog.listener()
    async def on_member_warn(self, member):
        log_content = f"**Member Warned:** {member.mention}"
        await self.log_to_channel(str(member.guild.id), log_content)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.content == after.content:
            return

        log_content = f"**Message Edited:** [Jump to message]({after.jump_url})"
        await self.log_to_channel(str(before.guild.id), log_content)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.channel.id in self.log_channels.values():  # Check if message is deleted in a log channel
            return
        
        log_content = f"**Message Deleted:** {message.content}"
        await self.log_to_channel(str(message.guild.id), log_content)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.roles != after.roles:
            added_roles = set(after.roles) - set(before.roles)
            removed_roles = set(before.roles) - set(after.roles)
            if added_roles:
                role_change_str = ', '.join(role.mention for role in added_roles)
                log_content = f"**Roles Added:** {after.mention} now has {role_change_str}."
                await self.log_to_channel(str(after.guild.id), log_content)
            if removed_roles:
                role_change_str = ', '.join(role.mention for role in removed_roles)
                log_content = f"**Roles Removed:** {after.mention} no longer has {role_change_str}."
                await self.log_to_channel(str(after.guild.id), log_content)


async def setup(client):
    await client.add_cog(Events(client))
