import discord

intents = discord.Intents.default()
intents.message_content = True


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

client = discord.Client(intents=intents)
client.run('MTAyNDQ0OTc5NjkyNjM0NTIxNg.GxVWZc.E79LHNBYjHgAxrODQEikSw2M4KPdT0jwyWqLMw')