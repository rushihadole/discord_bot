import discord
import random
import jokescrapper



intents = discord.Intents.default()
intents.members = True

def read_token(i):
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[i].strip()

token = read_token(0)
token_turu = read_token(1)
client = discord.Client(intents=intents)


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            embed = discord.Embed(title="WELCOME O' LORD!",
                                  description=f"Welcome to the Society of Stupid Shits {member.mention}, now you are one of us!")
            embed.add_field(name='Joke', value='Also, if you want me to tell you a joke just ask for it.')
            await channel.send(content=None, embed=embed)


@client.event
async def on_message(message):
    id = client.get_guild(767068103896465409)
    channels = ["test", "general"]
    hello_response = ["Heyy Dum Dum!", "What do you want now?", f"Are you really expecting a response or are you just lonely {message.author}?", "I'm not going to respond to that.",
                      "It was a wonderful day, until this very moment.", f"Was it really necessary for you to do that {message.author}?", f"I'm so glad I can't see your face {message.author}."
                      ]
    jokes = []
    with open('jokes.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            jokes.append(line)

    with open('joke.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            jokes.append(line)

    r = random.randint(0, len(hello_response)-1)
    rj = random.randint(0, len(jokes)-1)

    if str(message.channel) == channels[1] and str(message.author) != 'Dad it\'s Bad#1888':
        if message.content.lower().find("hello") != -1 or message.content.lower().find("hey") != -1 or message.content.lower() == "hi":
            await message.channel.send(hello_response[r])

        elif message.content.lower().find("joke") != -1:
            await message.channel.send(jokes[rj])


client.run(token_turu)




