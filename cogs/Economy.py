import discord
from discord.ext import commands
import json
import random

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["bal"])
    async def balance(self, ctx, member: discord.Member=None):
        with open("json/economy.json", "r") as f:
            user_eco = json.load(f)
        
        if member is None:
            member = ctx.author
        elif member is not None:
            member = member
        
        if str(member.id) not in user_eco:

            user_eco[str(member.id)] = {}
            user_eco[str(member.id)]["Balance"] = 100

            with open("json/economy.json", "w") as f:
                json.dump(user_eco, f, indent=4)
        
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:info:1220836512586010674> - Current Balance!**\n>>> **Balance**: ${user_eco[str(member.id)]['Balance']}\n**Bank**: ${user_eco[str(member.id)]['Deposited']}\n**Note**: There is a 5 minute cooldown on ALL commands!", inline=False)
        await ctx.send(content="", embed=embed)

    @commands.cooldown(1, per=300)
    @commands.command()
    async def beg(self, ctx):
        with open("json/economy.json", "r") as f:
            user_eco = json.load(f)
        
        if str(ctx.author.id) not in user_eco:

            user_eco[str(ctx.author.id)] = {}
            user_eco[str(ctx.author.id)]["Balance"] = 100

            with open("json/economy.json", "w") as f:
                json.dump(user_eco, f, indent=4)

        current_balance = user_eco[str(ctx.author.id)]["Balance"]
        amount = random.randint(-10, 30)
        new_balance = current_balance + amount

        if current_balance > new_balance:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:info:1220836512586010674> - Begged!**\n>>> Oh no! You've been robbed!\n**New Balance**: ${new_balance}.", inline=False)
            await ctx.send(content="", embed=embed)
        
            user_eco[str(ctx.author.id)]["Balance"] += amount

            with open("json/economy.json", "w") as f:
                json.dump(user_eco, f, indent=4)
        
        elif current_balance < new_balance:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:info:1220836512586010674> - Begged!**\n>>> Aww, poor homeless person. Here have some money!\n**New Balance**: ${new_balance}.", inline=False)
            await ctx.send(content="", embed=embed)
        
            user_eco[str(ctx.author.id)]["Balance"] += amount

            with open("json/economy.json", "w") as f:
                json.dump(user_eco, f, indent=4)
        
        elif current_balance == new_balance:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:info:1220836512586010674> - Begged!**\n>>> Aw man, nobody spared some change...\n**New Balance**: ${new_balance}.", inline=False)
            await ctx.send(content="", embed=embed)
    
    @commands.cooldown(1, per=300)
    @commands.command()
    async def work(self, ctx):
        with open("json/economy.json", "r") as f:
            user_eco = json.load(f)
        
        if str(ctx.author.id) not in user_eco:

            user_eco[str(ctx.author.id)] = {}
            user_eco[str(ctx.author.id)]["Balance"] = 100

            with open("json/economy.json", "w") as f:
                json.dump(user_eco, f, indent=4)

        amount = random.randint(100, 1000)        
        user_eco[str(ctx.author.id)]["Balance"] += amount

        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f"**<:info:1220836512586010674> - Worked!**\n>>> Phew... after a long shift, here's what you earned!\n**Earnings**: ${amount}\n**New Balance**: ${user_eco[str(ctx.author.id)]['Balance']}", inline=False)
        await ctx.send(content="", embed=embed)

        with open("json/economy.json", "w") as f:
            json.dump(user_eco, f, indent=4)
    
    @commands.cooldown(1, per=300)
    @commands.command()
    async def steal(self, ctx, member: discord.Member):
        with open("json/economy.json", "r") as f:
            user_eco = json.load(f)
        
        steal_probability = random.randint(0, 1)

        if steal_probability == 1:
            amount = random.randint(1, 100)

            if str(ctx.author.id) not in user_eco:

                user_eco[str(ctx.author.id)] = {}
                user_eco[str(ctx.author.id)]["Balance"] = 100

                with open("json/economy.json", "w") as f:
                    json.dump(user_eco, f, indent=4)
            
            elif str(member.id) not in user_eco:

                user_eco[str(member.id)] = {}
                user_eco[str(member.id)]["Balance"] = 100

                with open("json/economy.json", "w") as f:
                    json.dump(user_eco, f, indent=4)
            
            user_eco[str(ctx.author.id)]["Balance"] += amount
            user_eco[str(member.id)]["Balance"] -= amount

            with open("json/economy.json", "w") as f:
                json.dump(user_eco, f, indent=4)
            
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:info:1220836512586010674> - Theif!**\n>>> You just stole ${amount} from {member.mention}\n**New Balance**: ${user_eco[str(ctx.author.id)]['Balance']}", inline=False)
            await ctx.send(content="", embed=embed)
        
        elif steal_probability == 0:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:info:1220836512586010674> - Theif!**\n>>> You failed to steal ${amount} from {member.mention}... dummy...", inline=False)
            await ctx.send(content="", embed=embed)
    
    @commands.command(aliases=["dep", "bank"])
    async def deposit(self, ctx, amount: int):
        with open("json/economy.json", "r") as f:
            user_eco = json.load(f)
        
        if str(ctx.author.id) not in user_eco:

            user_eco[str(ctx.author.id)] = {}
            user_eco[str(ctx.author.id)]["Balance"] = 100
            user_eco[str(ctx.author.id)]["Deposited"] = 0

            with open("json/economy.json", "w") as f:
                json.dump(user_eco, f, indent=4)
        
        if amount > user_eco[str(ctx.author.id)]["Balance"]:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:info:1220836512586010674> - Bank!**\n>>> Cannot deposit this amount as your balance does not have the suffecient funds.", inline=False)
            await ctx.send(content="", embed=embed)
        
        else:
            user_eco[str(ctx.author.id)]["Deposited"] += amount
            user_eco[str(ctx.author.id)]["Balance"] -= amount

            with open("json/economy.json", "w") as f:
                json.dump(user_eco, f, indent=4)
            
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:info:1220836512586010674> - Bank!**\n>>> You have deposited ${amount} into your bank.", inline=False)
            await ctx.send(content="", embed=embed)
    
    @commands.command(aliases=["withdrawl", "wd"])
    async def withdraw(self, ctx, amount: int):
        with open("json/economy.json", "r") as f:
            user_eco = json.load(f)
        
        if str(ctx.author.id) not in user_eco:

            user_eco[str(ctx.author.id)] = {}
            user_eco[str(ctx.author.id)]["Balance"] = 100
            user_eco[str(ctx.author.id)]["Deposited"] = 0

            with open("json/economy.json", "w") as f:
                json.dump(user_eco, f, indent=4)
        
        if amount > user_eco[str(ctx.author.id)]["Deposited"]:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:info:1220836512586010674> - Bank!**\n>>> Cannot withdraw this amount as your bank doesn't have it.", inline=False)
            await ctx.send(content="", embed=embed)
        
        else:
            user_eco[str(ctx.author.id)]["Deposited"] -= amount
            user_eco[str(ctx.author.id)]["Balance"] += amount

            with open("json/economy.json", "w") as f:
                json.dump(user_eco, f, indent=4)
            
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=f"**<:info:1220836512586010674> - Bank!**\n>>> You have withdrawn ${amount} from your bank.", inline=False)
            await ctx.send(content="", embed=embed)

async def setup(client):
    await client.add_cog(Economy(client))