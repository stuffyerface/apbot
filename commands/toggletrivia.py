from commands.base_command  import BaseCommand
from utils                  import *
from random                 import randint
from datetime               import datetime


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command

class ToggleTrivia(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Shows mega walls legendaries of a player"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["toggle"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object
        
        if(checktrivia(message.author,message.channel)):
          if(message.channel.id != 849503309349650452):
            await message.channel.send("Wrong channel bozo")
          else:
            onOff = "off"
            if params[0].lower() == "on":
              toggle = True
              onOff = "on"
            else:
              toggle = False
            
            channel = client.get_channel(849503309349650452)
            role = message.author.guild.get_role(628594905287098388)

            
            await channel.set_permissions(role, send_messages=toggle, read_messages=toggle)
              
            await message.channel.send(f"Toggled chatting in {message.channel} {onOff}")
