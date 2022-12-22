
import discord
import random

tokenD = ''
guildD = 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
@client.event
async def on_message(message):

    if message.content == "!motivation":
        choices = ["Consistency is key", "You'll feel better after it"]
        select = random.randint(0, len(choices) - 1)
        await message.channel.send(choices[select])
        
    if message.content.endswith('j too much') or message.content.endswith("just too much") or message.content.endswith("too much"):
        await message.channel.send('10 push ups right now.')
    
    if "sad" in message.content or "depressed" in message.content:
        jim = "⣿⣿⣿⣿⠏⠌⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠸⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⠃⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⡿⠃⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⠃⠀⠀⣾⣿⣿⣿⣿⣿⣦⠀⠈⠻⣿⣿⣿⣿\n⣿⠀⠀⠀⣿⣿⣿⠟⠉⠉⠉⢃⣤⠀⠈⢿⣿⣿\n⣿⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⢹⣿⣧⠀⠀⠙⣿\n⣿⡆⠀⠀⠈⠻⡅⠀⠀⠀⠀⣸⣿⠿⠇⠀⠀⢸\n⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠔⠛⠁⠀⠀⠀⣠⣿\n⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿\n⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿\n⣿⣿⡇⠀We Go Jim ⣠⣿⣿⣿⣿⣿⣿\n⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿\n⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿\n⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿"
        await message.channel.send(jim)
    
    if message.content == "!workout":
        workouts = ['pushups', 'squats', 'situps', 'jumping jacks', 'high knees']
        await message.channel.send("Select an exercise:\n"
                                   "1. Pushups"
                                   "\n2. Squats"
                                   "\n3. Situps"
                                   "\n4. Jumping Jacks"
                                   "\n5. High Knees")

        def check(m):
            return (m.content == '1' or m.content == '2' or m.content == '3'or m.content == '4' or m.content == '5') and m.channel == message.channel
        msg = await client.wait_for('message', check=check)
        select = workouts[int(msg.content) - 1]

        await message.channel.send("Select a difficulty for "+select+ "\n1. Easy\n2. Medium\n3. Hard\n4. Randomize it")

        def check2(m):
            return (m.content == '1' or m.content == '2' or m.content == '3' or m.content == '4') and m.channel == message.channel
        msg = await client.wait_for('message', check=check2)
        if msg.content == '1':
            await message.channel.send("Do 5" + select + ".")
        elif msg.content == '2':
            await message.channel.send("Do 10" + select + ".")
        elif msg.content == '3':
            await message.channel.send("Do 25" + select + ".")
        elif msg.content == '4':
            amount = str(random.randint(25, 100))
            await message.channel.send("Do "+amount+" "+ select +".")





client.run(tokenD)
