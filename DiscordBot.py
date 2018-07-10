import discord
import config
import json

client = discord.Client()

def read_regulars():
    with open('regulars.json', 'r') as infile:
        data = json.load(infile)
        print(data)
    print(data)
    return data

def write_regulars():
    print("Writing to regulars.json")
    with open('regulars.json', 'w') as outfile:
        json.dump(regulars, outfile, sort_keys = True, indent = 4, ensure_ascii = False)

regulars = read_regulars()

@client.event
async def on_message(message):
    #the bot should not reply to itself
    if message.author != client.user and message.content.startswith(config.COMMANDPREFIX):
        msg = message.content.split(" ")
        cmd = msg.pop(0)[1:].lower()

        #No parameters - looks up message owner in the regulars list and provides link
        #Paramaters can be used to look up any player
        if cmd == "stats":
            print("Displaying stats")
            prefix = "https://pubg.op.gg/user/"
            suffix = "?server=pc-na"
            if msg:
                for name in msg:
                    await client.send_message(message.channel, prefix + msg + suffix)
            elif message.author.id in regulars:
                await client.send_message(message.channel, prefix + regulars[message.author.id] + suffix)
        
        #Format command as '!addme <PUBG NAME>', adds message owner to the regulars list
        elif cmd == "addme" and msg:
            if message.author.id not in regulars:
                print("Added " + message.author.id + " to the list of regulars as " + msg[0])
                regulars[message.author.id] = msg[0]
                await client.send_message(message.channel, "Added " + message.author.id + " to the list of regulars as " + msg[0])

        elif cmd == "removeme":
            print("Removing " + message.author.id + " from list of regulars as " + regulars[message.author.id])
            del regulars[message.author.id]
            
        #responds with a link to the list of 2d match telemetry of the indicated player
        elif cmd == "2d":
            prefix = "https://pubg.sh/"
            suffix = "/pc-na"
            if msg:
                for name in msg:
                    await client.send_message(message.channel, prefix + msg + suffix)
            elif message.author.id in regulars:
                await client.send_message(message.channel, prefix + regulars[message.author.id] + suffix)

        #shutsdown the bot and saves list of regulars - only usable by the bot owner specified in the config
        elif cmd == "shutdown":
            if message.author.id == config.OWNERID:
                await client.send_message(message.channel, "Saving list of regulars and shutting down...")
                write_regulars()
                await client.logout()
            else:
                await client.send_message(message.channel, "You do not have permission to use this command.")

        #Prints out a list of regular players
        elif cmd == "regulars":
            if regulars:
                for key,value in regulars.items():
                    await client.send_message(message.channel, key + " saved as " + value)
            else:
                print("Regulars Dictionary is empty")
@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("--------")
    #regulars = read_regulars()
    #print(regulars)
    print("Reading from regulars.json")


client.run(config.TOKEN)