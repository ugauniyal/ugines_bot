import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='^')


# Bot is Ready Confirmation
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="UGINES"))
    print('Bot is ready.')


# Rock,Paper & Scissors Game Command
@client.command()
async def game(ctx):
    option = ['rock', 'paper', 'scissors']
    await ctx.send(random.choice(option))


# Ping Command
@client.command()
async def ping(ctx):
    await ctx.send(f'Your ping is {round(client.latency * 1000)}ms')


# About Command
@client.command()
async def about(ctx):
    await ctx.send("Hello! It's a me UGINES!")


# Kick User Command
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


# Ban User Command
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


# Unban User Command
@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for banned_user in banned_users:
        user = banned_user.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            return


@client.command()
async def commands(ctx):

    embed = discord.Embed(title='Commands Help',
                            value='commands',
                            colour=discord.Colour.green(),
                            description="""
                            1. ^game - Play a rock, paper & scissors game against bot.
                            2. ^ping - Check your ping on discord.
                            3. ^about - About UGINES.
                            4. ^kick - Kick members from discord (Only for mods and admin).
                            5. ^ban - Ban members from discord (Only for mods and admin).
                            6. ^unban - Unban members from discord (Only for mods and admin).
                            7. ^commands - To get all the info about the commands.
                            """,
    )

    embed.add_field(name='UGINES', value='Thanks for support!')
    embed.set_author(name='UGINES', icon_url="https://cdn.discordapp.com/avatars/438407007448596480/553e39d500a4d047d56baa0e8b48c3d8.png?size=128")
    await ctx.send(embed=embed)


# Bot Token
client.run('BOT TOKEN')
