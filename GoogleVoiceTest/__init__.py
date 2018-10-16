from googlevoice import Voice
import discord
import asyncio

client = discord.Client()
voice = Voice()

numbers = {
        "Name" : 1234567897
    }

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    for person, number in numbers.items():
        if message.author.nick is None:
            voice.send_sms(number, message.author.name + ': ' + message.content)
        else:
            voice.send_sms(number, message.author.nick + '(' + message.author.name + ')' + ': ' + message.content)

def init_googlevoice():
    voice.login()

init_googlevoice()
client.run('token')
