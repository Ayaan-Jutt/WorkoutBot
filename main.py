
import discord
import random

tokenD = ''
guildD = 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

async def difficulty(message, workout):
    await message.channel.send("Select a difficulty:\n"
          "1. Easy\n"
          "2. Medium\n"
          "3. Hard\n"
          "4. Randomize it")
    if message.content == '1':
        await message.channel.send("Do 5" + workout + ".")
    if message.content == '2':
        await message.channel.send("Do 10" + workout + ".")
    if message.content == '3':
        await message.channel.send("Do 25" + workout + ".")
    if message.content == '4':
        amount = str(random.randint(25, 100))
        await message.channel.send("Do"+amount+" "+ workout +".")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.endswith('too much'):
        await message.channel.send('10 push ups right now.')
    if message.content == "!workout":
        workouts = ['pushups', 'squats', 'situps', 'jumping jacks', 'high knees']
        await message.channel.send("Select an exercise:\n"
                                   "1. Pushups"
                                   "\n2. Squats"
                                   "\n3. Situps"
                                   "\n4. Jumping Jacks"
                                   "\n5. High Knees")
        try:
            select = int(message.content) + 1
            if select > 5 or select < 0:
                raise Exception
            else:

                await message.channel.send("Select a difficulty for "+workouts[select - 1]+"\n1. Easy\n2. Medium\n3. Hard\n4. Randomize it")
        except:
            pass





client.run(tokenD)
