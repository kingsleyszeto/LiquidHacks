import discord
from discord.ext import commands
import datetime
import config

TOKEN = config.TOKEN

intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix='--', intents=intents)

@client.command(name='version')
async def version(context):
    myEmbed = discord.Embed(title="Current Version", description="The bot is Version 1.0", color=0x00ff00)
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="November 6th, 2020", inline=False)
    myEmbed.set_footer(text="Prototype")
    myEmbed.set_author(name="James N")

    await context.message.channel.send(embed=myEmbed)

#@client.event
#async def on_member_update(before, after):
    #general_channel = client.get_channel(774535857566122035)
    #await general_channel.send(f"{before.activity.created_at} is when you started doing {before.activity}")

@client.event
async def on_ready():
    general_channel = client.get_channel(774574690542813184)
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('owo'))
    await general_channel.send('Hayyyyy')

@client.event
async def on_message(message):
    general_channel = client.get_channel(774574690542813184)
    main_channel = client.get_channel(748890672546840692)
    if message.content == 'Where am I?':
        await general_channel.send(f"you're in {message.author.guild}")

    if message.content == 'What am I playing?':
        await general_channel.send(f"you're playing {message.author.activity}")

    if message.content.startswith('trump'):
        await general_channel.send('chile anyway')
    
    if message.content.startswith('pur'):
        await general_channel.send('okur!!')

    if message.content == ("I ain't never seen"):
        await general_channel.send('two pretty best friends')
        await main_channel.send('two pretty best friends')

    if message.content == ('send a DM'):
        await message.author.send("This is a DM. Have a good day!")

    if message.content == "How long?":
        await general_channel.send(f"{message.author.activity.created_at} is when you started playing {message.author.activity}")

    await client.process_commands(message)

@client.event
async def on_message_delete(message):
    general_channel = client.get_channel(774574690542813184)
    await general_channel.send(f'{message.author.display_name}, you sus as hale!')

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server")

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server")

# Run the client on the server
client.run(TOKEN)