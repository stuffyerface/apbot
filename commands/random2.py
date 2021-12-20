from os import execl
from commands.base_command  import BaseCommand
from utils                  import *
from random                 import randint


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command

class Random2(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Generates a random ap to hunt for"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["type","seasonal"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object
        
        if(checkspecial(message.author,message.channel)):
          if(params[0] not in ["c","t","all"]):
            await message.channel.send("Invalid parameter: '"+params[0]+"', use 'c' for challenge, 't' for tiered, or 'all' for both")
            return
          elif(params[1] not in ["none","christmas","summer","easter","halloween"]):
            await message.channel.send("Invalid parameter: '"+params[1]+"', Accepted values are: none, christmas, summer, easter, halloween")
            return
          excluded = ["christmas","summer","easter","halloween"]
          if(params[1] == "none"):
            excluded = []
          else:
            excluded.remove(params[1])
          progress = randomAp(params[0],excluded)
          progress = apFormat(progress, "Random Achievement")
          await message.channel.send(content = "", embed=progress)
        else:
          await message.channel.send(content = "", embed = embeds.emPremium)
