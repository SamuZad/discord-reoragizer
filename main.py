import discord
# this allows discord to access servers members, something not enabled by default
intents = discord.Intents.default()
intents.members = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        for role in message.guild.roles:
            if message.content == role.name:
                for member in role.members:
                    await message.channel.send(member)

client = MyClient(intents=intents)
client.run('TOKEN')