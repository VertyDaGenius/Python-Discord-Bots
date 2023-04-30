# the "if p_message == 'hello vert':" is a "command" in any channel
# the response = '' is what the bot responds to the command

# example: 
# (in the chat the user says) 
# hello vert
# (then the bot replys with
# HELLO!! BAWRK BAWRK BAWRK! CHECK OUT MY COMMANDS IN THE VERTBOT COMMANDS CHANNEL
#----------------------------------------------------
# in any channel too you can type in !ping <ip address>
# so then using socket the bot pings the ip address and replys with if its up or down
#----------------------------------------------------
# example: 
# (the user says)
# ping 8.8.8.8
# (then the bot replys with)
# 8.8.8.8 IS UP! WOOF WOOF! <then tags the user>
#----------------------------------------------------
# if you need help with setting up your first bot check out the readme file
# if you still ahve issues contact my discord or join my server for help:
#----------------------------------------------------
# WhoIsVerty#0383
# https://discord.com/invite/M7dG7Kp3Vy
#----------------------------------------------------

#imports
import discord
from discord.ext import commands
import random
import socket
from colorama import Fore

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    try:
        print(Fore.GREEN + f'{bot.user.name} has connected to Discord!')
    except:
        print(Fore.RED + 'Bot failed to connect!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    p_message = message.content.lower()
    if p_message == 'hello vert':
        response = 'HELLO!! BAWRK BAWRK BAWRK! CHECK OUT MY COMMANDS IN THE VERTBOT COMMANDS CHANNEL'
        
    elif message.content.startswith("!dice"):
        up , down = (int(message.content.split()[1]), int(message.content.split()[2]))
        if up < 0:
            await message.channel.send("no negative number.. GRRRRR.. BAWRK BAWRK!")
            return
        response = str(random.randint(up,down))

    elif p_message == 'woof':
        response = '**WOOF WOOF WOOF BAWRK BAWRK!!!!!!!**'
    elif p_message == 'github':
        response = 'https://github.com/AndrewTheSkid'
    elif p_message == 'uwu':
        response = 'NO E GIRLS.. GRRRR.. BARK BARK BARK'
    elif p_message == 'owo':
        response = 'w-woof?.. BARK BARK BARK! NO FURRIES'
    elif p_message == '-w-':
        response = 'NO FEMBOYS!!! GRRRR.. BARK BARK BARK'
    elif p_message == 'ily':
        response = 'NO ONLINE DATING!! (unless if its with me)'
    elif p_message == 'good boy':
        response = 'ok'
    elif p_message == 'furry':
        response = 'IM NOT A FURRY IM A DOG BOT!!! GRRR.. WOOF WOOF WOOF!!'

    elif message.content.startswith("!ping"):
        ip_address = message.content.split(" ")[1]
        try:
            socket.inet_aton(ip_address)
        except socket.error:
            response = f"{ip_address} IS NOT A VALID IP ADDRESS!! BAWRK BAWRK"
            await message.channel.send(response)
            return
        try:
            host_name = socket.gethostbyaddr(ip_address)[0]
            response = f"{ip_address} IS UP! WOOF WOOF! - {message.author.mention}"
        except socket.herror:
            response = f"{message.author.mention} {ip_address} IS DOWN! **CRIES** - {message.author.mention}"
    else:
        return
    await message.channel.send(response)

# connect the bot
if __name__ == '__main__':
    bot.run('---') #replace with your bots token
