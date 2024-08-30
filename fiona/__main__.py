import disnake

from disnake import Message
from disnake import Intents

from fiona.constants import Fiona

intents = Intents.all()
client = disnake.Client(intents=intents)



@client.event
async def on_message(message: Message):
    if message.author.id == int(Fiona.ID):
        pass
    if all([char in message.content.lower() for char in list(Fiona.SECRET)]):
        await message.reply("The secret is hidden in your message!")

client.run(Fiona.TOKEN)
