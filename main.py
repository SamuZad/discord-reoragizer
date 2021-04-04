import discord
import os
from discord.ext import commands
# this allows discord to access servers members, something not enabled by default
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents, description="This is a bot for discord administrative help")

@bot.command(brief='Basic ping command', description='The ping command to help make sure that the bot is alive')
@commands.has_permissions(administrator=True)
async def ping(ctx):
    await ctx.send('pong')

@bot.command(brief='Adds members of named roles to another role', description='Example command: $add_role <new_role_name> TO <old_role_1> AND <old_role_2>. Any number of old roles can be given, but at least 1 must be given.')
@commands.has_permissions(administrator=True)
async def add_role(ctx, *, arg):
    new_tag = arg.split("TO")[0].strip()
    old_tags = arg.split("TO")[1].split("AND")
    await ctx.send(f"Adding {new_tag} to {old_tags}...")
    new_role_object =  discord.utils.get(ctx.message.guild.roles, name=new_tag)

    for tag in old_tags:
        for role in ctx.guild.roles:
            #.strip() removes the trailing whitespaces in order to compare strings reliably
            if tag.strip() == role.name:
                for member in role.members:
                    await member.add_roles(new_role_object)
                await ctx.send(f"Added members of {role} to {new_tag}...")

    await ctx.send("Done with all")        

bot.run(os.getenv('TOKEN'))