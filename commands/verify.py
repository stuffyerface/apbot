from commands.base_command  import BaseCommand
from utils                  import *
from random                 import randint


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command

class Verify(BaseCommand):

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
        perm = False
        member = message.author
        if(message.channel.id == 818238693075976243):
          perm = True
        if(perm):
          username = params[0]
          uuid = get_uuid(username)
          if(uuid == "ERROR"):
            progress = -2
          else:
            progress = get_discord(uuid)
          
          if(progress == -2):
            msg = f"{username} was not found in Mojang API"
          elif(progress == "ERROR"):
            msg = "Make sure to link your discord in your hypixel settings and try verifying again."
          else:
            print("Ingame: "+ progress + " Actual: "+ str(member))
            if(progress == str(member)):
              try:
                await member.edit(nick= get_Name(username))
              except:
                print("Insufficient Permissions for nick change")

              roles = ['Verified'] + get_roles(username)
              print(roles)
              try:
                for x in range(len(roles)):

                  role = discord.utils.get(member.guild.roles, name=roles[x])
                  await member.add_roles(role)
              except:
                print("Insufficient Permissions for role change")


              msg = f"Successfully verified {get_Name(username)}"
            else:
              msg = "The username you entered is not linked to your discord account"



          await message.channel.send(content= msg)
