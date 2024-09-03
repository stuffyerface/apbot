from commands.base_command  import BaseCommand
from utils                  import *
from random                 import randint


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Pit(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Shows your progress on some pit challenge achievements"
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
        perm = True
        if(perm):
          username = params[0]
          uuid = get_uuid(username)
          if(uuid == "ERROR"):
            await message.channel.send("Mojang api broke")
            return
          else:
            progress = get_pitprogress(uuid)
          
          if(progress == "ERROR"):
            await message.channel.send("Hypixel api broke")
            return
             

          await message.channel.send(content= "", embed = progress)
