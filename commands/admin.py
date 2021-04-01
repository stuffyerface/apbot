from commands.base_command  import BaseCommand
from utils                  import *
from random                 import randint
from datetime               import datetime


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command

class Admin(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Shows mega walls legendaries of a player"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["param"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object
        
        if(str(message.author) == "Stuffy#1359"):
          param = params[0]
          retVal = ""
          if(param == "resource"):
            apres = requests.get("https://api.hypixel.net/resources/achievements")
            achres = json.loads(apres.text)
            if achres["success"] == False:
              retVal == "Error contacting resource api"
            else:
              dt = achres["lastUpdated"]
              retVal = f"Last updated: {datetime.utcfromtimestamp(dt/1000).strftime('%m/%d/%Y %H:%M')}"
          else:
            retVal = "Invalid parameter,\nAccepted parameters: resource"


          await message.channel.send(content= f"{retVal}")
        else:
          await message.channel.send(content= "", embed = embeds.emPremium)
