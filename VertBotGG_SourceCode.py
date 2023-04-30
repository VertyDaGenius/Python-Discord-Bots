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
# if you want to exit the game in the chat type in !exitgg 
# then the bot should exit the game and tell you what the number was
# if you want any help contact my discord or join my server
#----------------------------------------------------
# WhoIsVerty#0383
# https://discord.com/invite/M7dG7Kp3Vy
#----------------------------------------------------

# IGNORE ANY ERRORS!!
# UNLESS IF IT LITERALLY DOESN'T WORK

#imports
import discord
from discord.ext import commands
import random
from colorama import Fore
import asyncio

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
current_games = {}
@bot.event
async def on_message(message):
    if message.content.startswith('!exitgg'):
        if message.author.id in current_games:
            number = current_games[message.author.id]
            del current_games[message.author.id]
            reply1 = await message.channel.send(f"HAWHAHWHAW {message.author.mention}, YOU QUIT!!! THE NUMBER WAS {number}")
            await asyncio.sleep(3)
            await message.delete()
            await reply1.delete()
            
            async for m in message.channel.history(limit=5):
                if m.author == message.author or m.author == bot.user:
                    await m.delete(delay=1.5)
        else:
            reply = await message.channel.send(f"UR NOT IN A GAME! USE THE COMMAND !guessgame TO START ONE!!!.")
            await asyncio.sleep(3)
            await message.delete()
            await reply.delete()
        return

    if message.content.startswith('!guessgame'):
        if message.author.id in current_games:
            await message.channel.send("NICE TRY BUCKAROO YOU CAN ONLY PLAY ONE GAME AT A TIME!!!")
            return

        if message.channel.id != replace with your channel id:
            await message.channel.send("THIS COMMAND ONLY WORKS IN THE #guessgame-vertbot CHANNEL! IDIOT!")
            return

        number = random.randint(1, 50)
        guess_count = 0
        guess_limit = 10
        guesser = message.author
        current_games[guesser.id] = number

        msg = await message.channel.send(f"MY NUMBER IS BETWEEN 1 AND 50! BAWRKBAWRK!! {guesser.mention}")
        
        def check(m):
            return m.author == guesser and m.content.isdigit()

        while guess_count < guess_limit:
            try:
                guess_msg = await bot.wait_for('message', check=check, timeout=15.0)
                guess = int(guess_msg.content)
                await guess_msg.delete(delay=1.5)
            except asyncio.TimeoutError:
                await msg.edit(content=f"YOU TOOK TO LONG! GAME OVER!! THE NUMBER WAS {number}, {guesser.mention}")
                break
            except:
                await message.channel.send(f"ENTER A NUMBER, NOTHING ELSE!!!! BAWRK BAWRK {guesser.mention}")
                continue
            guess_count += 1
            if guess == number:
                await msg.edit(content=f"BAWRK!! {guesser.mention}, YOU WIN!!! THE NUMBER WAS {number}")
                break
            else:
                await msg.edit(content=f"MY NUMBER IS {'GREATER' if guess < number else 'LOWER'}! BAWRK BAWRK ({guess_count}) (you guessed {guess}) {guesser.mention}")
        
        if guesser.id in current_games:
            del current_games[guesser.id]

        async for m in message.channel.history(limit=30):
            if m.author == bot.user:
                if m.content.startswith(("MY NUMBER IS", "BAWRK!!", "ENTER A NUMBER, NOTHING ELSE", "YOU TOOK TOO LONG", "UR NOT IN A GAME", "NICE TRY BUCKAROO", "THIS COMMAND ONLY WORKS IN", "HAWHAHWHAW", "UR NOT IN A GAME!")):
                    try:
                        await asyncio.sleep(3)
                        await m.delete()
                    except discord.errors.NotFound:
                        pass
            elif m.author == guesser:
                try:
                    await asyncio.sleep(1.5)
                    await m.delete()
                except discord.errors.NotFound:
                    pass

# connect the bot
if __name__ == '__main__':
    bot.run('---') #replace with your bots token
