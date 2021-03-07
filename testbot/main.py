import os
import subprocess
import discord
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/python/testbot') 
load_dotenv(os.path.join(project_folder, '.env'))

def details():
    os.system('/home/vhserver/./vhserver dt')

def gamedig():
    output = subprocess.run(['gamedig', '--type', 'valheim', '127.0.0.1:2456'], stdout=subprocess.PIPE)
    return output

def number_of_players():
    details = str(gamedig())
    index = int(details.find('"maxplayers"'))
    index += 13
    maxplayers = details[index: index + 2]

    index = int(details.find('"numplayers"'))
    index += 13
    numplayers = details[index: index + 1]
    return ('Number of players online ' + numplayers + '/' + maxplayers)

def start_server():
    os.system('/home/vhserver/./vhserver start')

def stop_server():
    os.system('/home/vhserver/./vhserver stop')

def restart_server():
    os.system('/home/vhserver/./vhserver restart')

print(number_of_players())

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!vhserver details'):
        await message.channel.send(gamedig())

    if message.content.startswith('!vhserver players'):
        await message.channel.send(number_of_players())

    if message.content.startswith('!vhserver start'):
        await message.channel.send('Starting server')
        start_server()

    if message.content.startswith('!vhserver stop'):
        await message.channel.send('Stopping server')
        stop_server()

    if message.content.startswith('!vhserver restart'):
        await message.channel.send('Restarting server')
        restart_server()


client.run(os.getenv('TOKEN'))
