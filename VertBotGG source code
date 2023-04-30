# this bot is used to play a game i call guess game (gg)
# to start the game you need to type in !guessgame in the selected channel (you can tweak the code to let it work in any channel but its kinda spammy so id recommend it)
#you can edit the code to make it less of like a dog.
#----------------------------------------------------
# SETUP:
# turn developer mode on in your discord settings (if you dont know how to google it)
# right click on a selected channel you want the code to work in
# click copy channel id
# paste it into the line that has:
# if message.channel.id != replace with your channel id:
# example on how it should look like:
# if message.channel.id != 123456789101112: (dont actually use this or it wont work, and make sure you leave the colon (:) because the next line is indented
#----------------------------------------------------
# RULES ON HOW TO PLAY:
# go to your selected channel
# type in !guessgame
# it should tell you that it selected a random number between 1-50
# in the chat of the same channel type in a number between 1-50, you have 10 tries to get it correct
# to make it easier the bot tells you if your number is greater or less than the selected number
# if you want any help contact my discord or join my server
#----------------------------------------------------
# WhoIsVerty#0383
# https://discord.com/invite/M7dG7Kp3Vy
#----------------------------------------------------

#imports

import discord
from discord.ext import commands
import random
from colorama import Fore

#connection

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



#game

@bot.event
async def on_message(message):
    if message.content.startswith('!guessgame'):
        if message.channel.id != replace with your channel id:
            await message.channel.send("THIS COMMAND ONLY WORKS IN THE CHANNEL #guessgame-vertbot STUPID!")
            return

        number = random.randint(1, 50)
        guess_count = 0
        guess_limit = 10
        await message.channel.send("MY NUMBER IS BETWEEN 1 AND 50! WOOFWOOFWOOFOWOFOFOF!")
        while guess_count < guess_limit:
            try:
                guess = await bot.wait_for('message', timeout=30.0)
                if guess.content.startswith('!exitgg'):
                    await message.channel.send(f'HAHAHAHA U QUIT! THE NUMBER WAS {number}')
                    return
                guess = int(guess.content)
            except asyncio.TimeoutError:
                await message.channel.send("YOU TOOK TOO LONG! >:(!")
                return
            except:
                await message.channel.send("ENTER A NUMBER, NOTHING ELSE!!! WOOF WOOF!")
                continue
            if guess < number:
                await message.channel.send("MY NUMBER IS GREATER! BAWRK BAWRK")
            elif guess > number:
                await message.channel.send("MY NUMBER IS LOWER! BAWRK BAWRK")
            else:
                await message.channel.send(f"YAYYYY {message.author.mention}! YOU GUESSED IT CORRECTLY! :3 ({number})!")
                return
            guess_count += 1
        await message.channel.send(f"U ran out of guesses :( the number was {number}. BAWRK")


# connect the bot

if __name__ == '__main__':
    bot.run('---') #replace with your bots token
