import discord
import config
import requests

client = discord.Client()

regulars = []

@client.event
async def on_message(message):
    #the bot should not reply to itself
    if message.author != client.user and message.content.startswith(config.COMMANDPREFIX):
        msg = message.content.split(" ")
        cmd = msg[0][1:].lower()
        
        #responds with a link to the pubg.op.gg profile of the indicated player
        if cmd == "stats":
            link = "https://pubg.op.gg/user/" + msg[1] + "?server=pc-na"
            await client.send_message(message.channel, link)
    
        #responds with a link to the list of 2d match telemetry of the indicated player
        elif cmd == "2d":
            link = "https://pubg.sh/" + msg[1] + "/pc-na"
            await client.send_message(message.channel, link)
        
        #shutsdown the bot - only usable by the bot owner specified in the config
        elif cmd == "shutdown":
            if message.author.id == config.OWNERID:
                await client.send_message(message.channel, "Shutting down...")
                await client.logout()
            else:
                await client.send_message(message.channel, "You do not have permission to use this command.")
    
        #adds a name to the list of regulars to query the API
        elif cmd == "add":
            await client.send_message(message.channel, "Adding " + msg[1] + " to list of regulars.")
            regulars.append(msg[1])
        
        #removes a name from the list of regulars
        elif cmd == "remove":
            await client.send_message(message.channel, "Removing " + msg[1] + " from list of regulars.")
            regulars.remove(msg[1])
        
        #prints a list of the regular players
        elif cmd == "regulars":
            if not regulars:
                await client.send_message(message.channel, "List of regulars is empty.")
            else:
                await client.send_message(message.channel, "The current list of regulars is: " + ', '.join(regulars))

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("--------")


client.run(config.TOKEN)
