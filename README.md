# pubg-discord-bot
Intended to access the PUBG API and record stats and match info


In config.py:

TOKEN is the Discord Bot token

APIKEY is the PUBG API Key

OWNERID is the Discord client ID of the bot owner

Go to https://discordapp.com/developers/applications
Create a new application and give a name. Then make is a bot via the Bot option in the left panel.

Once running, each player should add themselves to the userlist via the "!addme <PUBG USERNAME>" command. They can then use !sh, !2d, or !pubg.op to get links quickly to their particular pages.

#TODO: add !stats command to check for new matches via the API and display them neatly in Discord.

As the bot owner, you can cleanly shutdown the bot using the "!shutdown" command.
