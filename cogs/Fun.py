import discord
from discord.ext import commands
import random
import requests

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def joke(self, ctx):
        random_number = random.randint(1, 1000)
        
        if random_number == 1:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value="**uh... I guess your life**", inline=False)
            await ctx.send(embed=embed)
        elif random_number == 2:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value="**The only joke is iMerciless...**", inline=False)
            await ctx.send(embed=embed)
        else:
            try:
                response = requests.get("https://v2.jokeapi.dev/joke/Any")
                if response.status_code == 200:
                    joke_data = response.json()
                    if joke_data["type"] == "single":
                        embed = discord.Embed(title="", color=0x2b2d31)
                        embed.add_field(name="", value=f"**{joke_data["joke"]}**", inline=False)
                        await ctx.send(embed=embed)
                    elif joke_data["type"] == "twopart":
                        embed = discord.Embed(title="", color=0x2b2d31)
                        embed.add_field(name="", value=f"**{joke_data['setup']}\n{joke_data['delivery']}**", inline=False)
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title="", color=0x2b2d31)
                        embed.add_field(name="", value="**Oops! Couldn't fetch a joke right now. Try again later.**", inline=False)
                        await ctx.send(embed=embed)                        
                        await ctx.send("Oops! Couldn't fetch a joke right now. Try again later.")
                else:
                    embed = discord.Embed(title="", color=0x2b2d31)
                    embed.add_field(name="", value="**Oops! Couldn't fetch a joke right now. Try again later.**", inline=False)
                    await ctx.send(embed=embed)
            except Exception as e:
                await ctx.send(f"An error occurred: {e}")
    
    @commands.command()
    async def facts(self, ctx):
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        if response.status_code == 200:
            fact_data = response.json()
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value=fact_data["text"], inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="", color=0x2b2d31)
            embed.add_field(name="", value="**Oops! Couldn't fetch a joke right now. Try again later.**", inline=False)
            await ctx.send(embed=embed)
    
    @commands.command()
    async def eightball(self, ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        response = random.choice(responses)
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> **Question: {question}\nAnswer: {response}**", inline=False)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} hugs {member.mention}!", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} pats {member.mention} gently.", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} slaps {member.mention} playfully.", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} kisses {member.mention} as a friend.", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def handshake(self, ctx, member: discord.Member):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} firmly shakes {member.mention}'s hand.", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def highfive(self, ctx, member: discord.Member):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} high fives {member.mention}.", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def cry(self, ctx):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} starts to cry.", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def scream(self, ctx):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} starts to scream for no reason.", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def smile(self, ctx):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} starts to smile like a maniac.", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def laugh(self, ctx):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} starts to laugh like a lunatic.", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def sleep(self, ctx):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} fell into a deep sleep.", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def sit(self, ctx):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} sits down in a chair.", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def wakeup(self, ctx):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} woke up from their deep slumber.", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def eat(self, ctx, *, food: str):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} eats a large bowl of {food}", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def travel(self, ctx, *, destination: str):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} travels to {destination}.", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def explore(self, ctx, *, area: str):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} explores {area} and finds nothing.", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def attack(self, ctx, member: discord.Member):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} attacks {member} but it doesn't go so well and ends up with a broken arm.", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def dodge(self, ctx):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} dodges a large attack from the enemies.", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def defend(self, ctx):
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} defends their comrades from a large spell from the enemies.", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def cast(self, ctx, *, spell: str):
        spell_level = random.randint(1, 100)
        embed = discord.Embed(title="", color=0x2b2d31)
        embed.add_field(name="", value=f">>> {ctx.author.mention} casts a level {spell_level} {spell}. It's super effective!", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(fun(client))