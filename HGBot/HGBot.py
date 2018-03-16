#!/usr/bin/env python
"""\
HGBot.py

A discord bot for the Hang Gang Server

A fun bot for friends

usage: HGBot.py
"""
import discord
import asyncio
import random
import pickle
import os

# create a Client variable
client = discord.Client()

# global variables
eggplant = ''
ricoFP = "data/rico_quotes.pk1"
vincentFP = "data/vincent_movies.pk1"
aidenFP = "data/aiden_patrol.pk1"
tokenFP = "data/token.pk1"
token = ''

with open(tokenFP, "rb") as token_file:
    token = pickle.load(token_file)

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------')
    global eggplant
    for x in client.get_all_emojis():
        if "eggplant" in x.name:
            eggplant = str(x)

@client.event
async def on_message(msg):
    buffer = '\0'
    buffer = msg.content.lower()

    if 'dran' in buffer or 'dr@n' in buffer:
        if 'Bot' in str(msg.author):
            return
        else:
            await client.send_message(msg.channel, 'dran\'s actually austismic stop saying it')

    if 'https://' in buffer and 'links' not in str(msg.channel):
        with open(aidenFP, "rb") as patrol_file:
            patrol = pickle.load(patrol_file)

        await client.send_message(msg.channel, "Dear " + msg.author.nick + ",\r\n\r\n" + patrol[0] + "\r\n\r\n" + patrol[1] + "\r\n" + patrol[2] + "\r\n" + patrol[3])

    if buffer.startswith('!james'):
        if "Caydunn#7963" in str(msg.author):
            await client.send_message(msg.channel, 'Fuck you Caden')

        if 'hi' in buffer or 'hello' in buffer:
            await client.send_message(msg.channel, 'hi there! ' + msg.author.nick)
        elif 'what am I playing' in buffer:
            await client.send_message(msg.channel, msg.author.game.name)
        elif 'flipcoin' in buffer:
            flip = random.choice(['heads', 'tails'])
            await client.send_message(msg.channel, 'You flipped: ' + flip)
        elif 'diceroll' in buffer:
            roll = random.choice(['1', '2', '3', '4', '5', '6'])
            await client.send_message(msg.channel, 'You rolled: ' + roll)
        elif 'gay' in buffer:
            response = random.choice(['no u', 'ur dad lesbian'])
            await client.send_message(msg.channel, response)

    if buffer.startswith('!yoel'):
        if "Caydunn#7963" in str(msg.author):
            await client.send_message(msg.channel, 'Fuck you Caden')

        checkfor = ['you\'re', 'your', 'you']
        out = msg.content[5:]
        out = out.lower()

        if any(x in msg.content for x in checkfor):
            out = out.replace("you're", "YOU'RE")
            out = out.replace("your", "YOUR")
            out = out.replace("you", "YOU")
            await client.send_message(msg.channel, out)
        else:
            await client.send_message(msg.channel, 'You\'re a' + out)

    if buffer.startswith("!jay"):
        await client.send_message(msg.channel, 'this is true')

    if buffer.startswith("!aids"):
        await client.send_message(msg.channel, 'Fuck you aiden')

    if buffer.startswith('!richardz'):
        await client.send_message(msg.channel, 'Fucking 99 in 5')

    if buffer.startswith('!rico'):
        with open(ricoFP, "rb") as rico_file:
            out = pickle.load(rico_file)
        await client.send_message(msg.channel, random.choice(out))

    if buffer.startswith('!vincent'):
        if 'movie' in buffer:
            with open(vincentFP, "rb") as movies_file:
                    movies = pickle.load(movies_file)
            await client.send_message(msg.channel, random.choice(movies))
        else:
            await client.send_message(msg.channel, eggplant)

    if buffer.startswith('!jackson'):
        await client.send_message(msg.channel, 'OOOKKKKAAAYYY BUUUUDDDDYYYYYYY')

    if buffer.startswith('!yalikejazz'):
        await client.send_message(msg.channel, 'According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don\'t care')

client.run(token[0])