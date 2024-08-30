import disnake

from disnake import Message
from disnake import Intents

from fiona.constants import Fiona

intents = Intents.all()
client = disnake.Client(intents=intents)



@client.event
async def on_message(message: Message):
    if message.author.id == Fiona.ID:
        pass
    if all([char in message.content.lower() for char in list("aadil")]):
        await message.reply("There's aadil in there.")

client.run(Fiona.TOKEN)
