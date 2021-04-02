from commands.base_command  import BaseCommand
from utils                  import *
from random                 import randint


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command

class DoIHaveLegoMaestrosHead(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Shows mega walls legendaries of a player"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["username"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object
        
        if(True): #checkperm(message.author):
          username = params[0]
          uuid = get_uuid(username)
          if(uuid == "ERROR"):
            progress = -2
          else:
            profile = get_profile(uuid)
          
          if(profile == -2):
            msg = f" {username} was not found in Mojang API"
          elif(profile == "ERROR"):
            msg = "An error occured talking to the API. Please try again later."
          else:
            msg = profile
          
          head = "does not"
          legosuuid = "d7127ab6-741f-477d-8dfc-a59146b3fe51"
          try:
            profile = get_profile(uuid)
            try:
              pres = profile["player"]["stats"]["SkyWars"]["head_collection"]["prestigious"]
              for x in range(len(pres)):
                #print(x)
                if(str(pres[x]["uuid"]) == legosuuid):
                    #print(pres[x])
                    head = "does"
            except:
              pass
            try:
              recent = profile["player"]["stats"]["SkyWars"]["head_collection"]["prestigious"]
              for x in range(len(recent)):
                #print(x)
                if(str(recent[x]["uuid"]) == legosuuid):
                    #print(pres[x])
                    head = "does"
            except:
              pass
          except:
            pass
          
          embed = discord.Embed(
            title = f"{get_Name(username)} {head} have Lego Maestro's head.",
            description = "You can get it by killing him in a corrupted skywars game.",
            colour = discord.Colour.blue()
          )

          await message.channel.send(content= "", embed = embed)
        else:
          await message.channel.send(content= "", embed = embeds.emPremium)
