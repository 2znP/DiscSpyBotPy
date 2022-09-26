import discord
from basicConfig import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logado com {client.user}')
    await client.change_presence(status=discord.Status.offline)

@client.event
async def on_message(message):
    arquivo = open("log.txt", "a")
    x = str(message.author) + ':' + str(message.content)
    strx = str(x)
    print(strx)
    arquivo.write(strx + "\n")
    arquivo.close()
client.run(TOKEN)
