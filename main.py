import discord
import os
from discord.ext import commands
# this allows discord to access servers members, something not enabled by default
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents, description="This is a bot for discord administrative help")

@bot.command()
@commands.has_permissions(administrator=True)
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
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