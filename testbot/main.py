import os
import subprocess
import discord
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/python/ValheimDiscordBot/testbot')
load_dotenv(os.path.join(project_folder, '.env'))


def details():
    os.system('/home/vhserver/./vhserver dt > details')
    file = list(open("details", "r"))
    os.system('rm details')
    return file


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


def check_update_server():
    os.system('/home/vhserver/./vhserver cu')


def update_server():
    os.system('/home/vhserver/./vhserver update')


print(number_of_players())


def findIp():
    l = details()
    for r in l:
        if str(r).find('Internet IP:'):
            print(str(r))

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

    if message.content.startswith('!vhserver checkupdate'):
        check_update_server()

    if message.content.startswith('!vhserver update'):
        update_server()

    if message.content.startswith('!vhserver ip'):
        await message.channel.send('Fetching ip')
        list = details()
        await message.channel.send(len(list))
        for r in list:
            await message.channel.send(r)

client.run(os.getenv('TOKEN'))
