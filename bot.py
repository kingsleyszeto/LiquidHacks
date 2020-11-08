import discord
from discord.ext import commands
from datetime import datetime
import config
import random
import asyncio

TOKEN = config.TOKEN

intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix='--', intents=intents)
general_channel_ID = 774574690542813184 # access members in channel
guild_ID = 760560106701324390 # access to members in guild

# send a reminder from a dictionary of options
async def send_activity_reminder(time_played, member):
    # add custom reminder messages
    member_name = member.nick if member.nick else member.name
    reminders = {
        0: f"You've been playing for {time_played} hours now, {member_name}! Here's your little reminder to take a break!",
        1: f"It's been {time_played} hours since you started playing, {member_name}. How about we get a glass of water?",
        2: f"{time_played} hours have zipped by! Don't forget to stretch, {member_name}!",
        3: "ǵ̶͌o̸͛̒ ̵͋͋d̶͝͝r̴̓̎i̴̓̔n̶̿̓ḱ̵̽ ̶̐̕w̸͑̐a̶̒͌t̸̉͆e̶̐͝r̵͛̕",
        4: "ǵ̶͌o̸͛̒ ̵͋͋d̶͝͝r̴̓̎i̴̓̔n̶̿̓ḱ̵̽ ̶̐̕w̸͑̐a̶̒͌t̸̉͆e̶̐͝r̵͛̕",
        5: "ǵ̶͌o̸͛̒ ̵͋͋d̶͝͝r̴̓̎i̴̓̔n̶̿̓ḱ̵̽ ̶̐̕w̸͑̐a̶̒͌t̸̉͆e̶̐͝r̵͛̕"
    }
    rand = random.randint(0, len(reminders)-1)

    if time_played == 2 or time_played == 4 or time_played == 0:
        print(f"Sent a reminder to {member_name}")
        await member.send(reminders[rand])

# uncomment this code and comment out second member_activity_report() if you want to access all members in guild
# async def member_activity_report(guild):
#     for m in guild.members:
#         # make sure activity is valid
#         if m.activity and m.activity.type.name == "playing":
#             # make sure the game being played has a created_at object
#             if m.activity.created_at:
#                 hour = m.activity.created_at.hour
#                 date = datetime.utcnow()
#                 time_played = abs(date.hour - hour)
#                 await send_activity_reminder(time_played, m)

# if activity is valid and call send_activity_reminder() to members in channel
async def member_activity_report(channel):
    for m in channel.members:
        # make sure activity is valid
        activities = m.activities
        for activity in activities:
            if activity and activity.type.name == "playing":
                # make sure the game being played has a created_at object
                if activity.created_at:
                    hour = activity.created_at.hour
                    date = datetime.utcnow()
                    time_played = abs(date.hour - hour)
                    await send_activity_reminder(time_played, m)
                break

# every hour the bot sends reminders to members in channel/guild
async def member_activity_background_task():
    await client.wait_until_ready()
    # guild = client.get_guild(guild_ID)
    general_channel = client.get_channel(774574690542813184)

    while not client.is_closed():
        try: 
            await member_activity_report(general_channel)
            # await member_activity_report(guild) 
            await asyncio.sleep(60 * 60)
        except Exception as e:
            print(str(e))
            await asyncio.sleep(300)

# returns version #
@client.command(name='version')
async def version(context):
    myEmbed = discord.Embed(title="Current Version", description="The bot is Version 1.1", color=0x00ff00)
    myEmbed.add_field(name="Version Code:", value="v1.1.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="November 6th, 2020", inline=False)
    myEmbed.set_footer(text="Prototype")
    myEmbed.set_author(name="James N")

    await context.message.channel.send(embed=myEmbed)

# initializes bot
@client.event
async def on_ready():
    general_channel = client.get_channel(general_channel_ID)

    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('owo'))
    await general_channel.send("I'm online!")

@client.event
async def on_message(message):
    general_channel = client.get_channel(general_channel_ID)
    # guild = client.get_guild(guild_ID) 

    # for fun messages
    if message.content.lower().startswith('trump'):
        await general_channel.send('Bye den!')
    
    if message.content.lower().startswith('pur'):
        await general_channel.send('Okur!')

    if "i ain't never seen" in message.content.lower():
        await general_channel.send('two pretty best friends  :women_with_bunny_ears_partying:')

    # tells the user how long they've been playing for
    if "how long?" in message.content.lower():
        if message.author.activity and message.author.activity.created_at:
            hour = message.author.activity.created_at.hour
            minute = message.author.activity.created_at.minute
            date = datetime.utcnow()
            time_played_hours = abs(date.hour - hour)
            time_played_minutes = abs(date.minute - minute)

            if message.author.activity and time_played_hours:
                await general_channel.send(f"You've been playing {message.author.activity} for {time_played_minutes} "
                                            "minutes.")
            elif message.author.activity:
                await general_channel.send(f"You've been playing {message.author.activity} for {time_played_hours} "
                                            f"hours and {time_played_minutes} minutes.")
        else:
            await general_channel.send("You aren't playing anything.")
    
    # manually call the reminders for gamers
    if "activity report" in message.content.lower():
        await member_activity_report(general_channel)

    await client.process_commands(message)

# for fun message on delete
@client.event
async def on_message_delete(message):
    general_channel = client.get_channel(general_channel_ID)
    await general_channel.send(f'I saw that, {message.author.display_name}  :eyes:')

# provides info to terminal
@client.event
async def on_member_join(member):
    print(f"{member} has joined a server")

# provides info to terminal
@client.event
async def on_member_remove(member):
    print(f"{member} has left a server")

# Run the client on the server
client.loop.create_task(member_activity_background_task())
client.run(TOKEN)
