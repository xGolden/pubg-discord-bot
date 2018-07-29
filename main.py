import discord
import config
import json
import player
import os

client = discord.Client()

def read_file(filename, fileformat=".json"):
    with open(filename + fileformat, 'r') as infile:
        data = json.load(infile)
    return data

def write_file(data, filename, fileformat=".json"):
    with open(filename + fileformat, 'w') as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii = False)

def save_players(dict_of_players):
    saved_players = {}
    for key in dict_of_players:
        print(key)
        saved_players[key] = {
        "DISCORDID": dict_of_players[key].id, 
        "DISCORDNAME": dict_of_players[key].name, 
        "PUBGNAME": dict_of_players[key].pname
        }
    write_file(saved_players, "saved_players")
    
def load_players():
    if os.path.isfile("saved_players.json"):
        saved_players = read_file("saved_players")
        for key in saved_players:
            players[key] = player.Player(saved_players[key]["DISCORDID"], saved_players[key]["DISCORDNAME"], saved_players[key]["PUBGNAME"])
    else:
        print("Found no save file, empty list created")

players = {}
load_players()

#for key in players:
    #print(players[key].get_DISCORDNAME())

@client.event
async def on_message(message):
    if not message.author.bot and message.author != client.user and message.content.startswith(config.COMMANDPREFIX):
        msg = message.content.split(" ")
        cmd = msg.pop(0)[1:].lower()
    
        if cmd == "addme":
            if msg and isinstance(msg, list) and message.author.id not in players:
                players[message.author.id] = player.Player(message.author.id, message.author.name, msg[0])
                save_players(players)
            elif isinstance(msg, str):
                print("PARAM ADDME IS A STRING SOMEHOW")
            elif message.author.id in players:
                await client.send_message(message.channel, "You are already logged as a player as " + players[message.author.id].get_PUBGNAME())

        elif cmd == "removeme":
            if message.author.id in players:
                del players[message.author.id]
                save_players(players)
    
        elif cmd == "stats":
            if msg:
                prefix = "https://pubg.op.gg/user/"
                suffix = "?server=pc-na"
                if isinstance(msg, list):
                    output = []
                    for name in msg:
                        output.append(prefix + name + suffix)
                    await client.send_message(message.channel, "\n".join(output))
                elif isinstance(msg, str):
                    await client.send_message(message.channel, prefix + msg + suffix)
            elif message.author.id in players:
                await client.send_message(message.channel, players[message.author.id].get_stats_link())
    
        elif cmd == "2d" or cmd == "sh":
            if msg:
                prefix = "https://pubg.sh/"
                suffix = "/pc-na"
                if isinstance(msg, list):
                    output = []
                    for name in msg:
                        output.append(prefix + name + suffix)
                    await client.send_message(message.channel, "\n".join(output))
                elif isinstance(msg, str):
                    await client.send_message(message.channel, prefix + msg + suffix)
            elif message.author.id in players:
                await client.send_message(message.channel, players[message.author.id].get_sh_link())

        elif cmd == "shutdown":
            if message.author.id == config.OWNERID:
                print("Shutting down...")
                await client.logout()
            
        elif cmd == "regulars":
            if players:
                saved_players = []
                for key in players:
                    saved_players.append(players[key].get_DISCORDNAME() + " as " + players[key].get_PUBGNAME())
                await client.send_message(message.channel, "\n".join(saved_players))
            else:
                await client.send_message(message.channel, "No saved players currently.")

@client.event 
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("--------")


client.run(config.TOKEN)