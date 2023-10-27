from commands.base_command  import BaseCommand
from utils                  import *
from random                 import randint


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command

class Update(BaseCommand):

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
        member2 = re.sub(r'#0$', '', str(member))
        emoji1 = "<:achievement:819360686290370567>"
        if(message.channel.id == 818244035277881344):
          perm = True
        if(perm):
          username = params[0]
          uuid = get_uuid(username)
          if(uuid == "ERROR"):
            progress = -2
          else:
            progress = get_discord(uuid)
          aproles = ["0K AP","1K AP","2K AP","3K AP","4K AP","5K AP","6K AP","7K AP","8K AP","9K AP","10K AP","11K AP","12K AP","13K AP","14K AP","15K AP","16K AP","17K AP","18K AP","19K AP","20K AP","21K AP","22K AP","23K AP","24K AP","25K AP","26K AP","27K AP","28K AP","29K AP","30K AP","31K AP"]
          lvlroles = ["Lvl 100+", "Level 150+", "Level 200+", "Level 250+", "Level 300+", "Level 400+", "Level 500+"]
          if(progress == -2):
            msg = f"{username} was not found in Mojang API"
          elif(progress == "ERROR"):
            msg = "Make sure to link your discord in your hypixel settings and try verifying again."
          else:
            if(progress == str(member)):
              try:
                await member.edit(nick= get_Name(username))
              except:
                print("Insufficient Permissions for nick change")

              roles = get_roles(username)
              for x in member.roles:
                if str(x) in roles:
                  roles.remove(str(x))
              for x in roles:
                if x in lvlroles:
                  await removeroles(member,lvlroles)
                if x in aproles:
                  await removeroles(member, aproles)
              print(roles)
              try:
                for x in range(len(roles)):
                  role = discord.utils.get(member.guild.roles, name=roles[x])
                  await member.add_roles(role)
              except:
                print("Insufficient Permissions for role change")
              for x in roles:
                channel = client.get_channel(818245966317748264)
                await channel.send(content = f"{emoji1} Congrats to {member.mention} for earning {x}!")


              msg = f"Successfully updated {get_Name(username)}"
            else:
              msg = f"The username you entered is not linked to your discord account\nYour ID: {str(member2)}\nLinked ID: {progress}"



          await message.channel.send(content= msg)
