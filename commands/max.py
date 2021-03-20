from commands.base_command  import BaseCommand
from utils                  import *
from random                 import randint


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
emoji1 = "<:achievement:819360686290370567>"
class Max(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Gives info on the current tournament"
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
        
        if(checkperm(message.author)):
          username = params[0]
          uuid = get_uuid(username)
          if(uuid == "ERROR"):
            progress = -2
          else:
            progress = get_maxes(uuid)
          
          if(progress == -2):
            msg = f" {username} was not found in Mojang API"
          elif(progress == "ERROR"):
            msg = "An error occured talking to the API. Please try again later."
          else:
            msg = progress

          maxes = ""
          for x in progress:
            maxes += f"{emoji1} " + x + "\n"
          em = discord.Embed(
            title = f"{get_Name(username)} has {len(progress)} max games",
            description = f"{maxes}",
            colour = discord.Colour.purple()
          )
          em.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
          em.set_thumbnail(url = f"https://crafatar.com/avatars/{uuid}")

          await message.channel.send(content = "", embed = em)
        else:
          await message.channel.send(content = "", embed = embeds.emPremium)