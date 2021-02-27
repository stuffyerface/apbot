from commands.base_command  import BaseCommand
from utils                  import *


import random


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command

class Spin(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Gives info on the current tournament"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = None
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
          spin = discord.Embed(
            title = f"You've Spun the Wheel!",
            colour = discord.Colour.purple()
          )

          spin.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")

          spin.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/footer/blue-avatar.png")

          # 0 - 21
          games = ["Skyblock", "Arcade", "TNT Games", "Blitz", "Mega Walls", "Cops and Crims", "UHC", "Warlords", "Skywars", "Smash Heroes", "Speed UHC", "Bedwars", "Murder Mystery", "Build Battle", "Duels", "The Pit", "Walls", "Paintball", "Arena Brawl", "Quakecraft", "VampireZ", "Turbo Kart Racers"]
          imgspin = [
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/SkyBlock-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/Arcade-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/TNT-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/SG-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/CVC-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/UHC-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/Warlords-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/Skywars-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/SmashHeroes-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/SpeedUHC-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/BedWars-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/MurderMystery-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/BuildBattle-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/Duels-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/Pit-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/Walls-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/Paintball-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/Arena-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/Quakecraft-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/VampireZ-64.png",
            "https://hypixel.net/styles/hypixel-v2/images/game-icons/TurboKartRacers-64.png"
          ]

          roll = []

          if(740276568781357228 not in message.author.roles):
            roll += [0]
          if(748294135974330408 not in message.author.roles):
            roll += [1]
          if(641685551325642763 not in message.author.roles):
            roll += [2]
          if(640973784643272737 not in message.author.roles):
            roll += [3]
          if(812718858262544394 not in message.author.roles):
            roll += [4]
          if(741811909069635586 not in message.author.roles):
            roll += [5]
          if(640973622336290816 not in message.author.roles):
            roll += [6]
          if(641685239839588362 not in message.author.roles):
            roll += [7]
          if(741812357029953546 not in message.author.roles):
            roll += [8]
          if(641528693122138132 not in message.author.roles):
            roll += [9]
          if(640973324393906187 not in message.author.roles):
            roll += [10]
          if(640978066151178280 not in message.author.roles):
            roll += [11]
          if(640976648971354143 not in message.author.roles):
            roll += [12]
          if(640972796846931971 not in message.author.roles):
            roll += [13]
          if(640977959360135168 not in message.author.roles):
            roll += [14]
          if(718169645713981501 not in message.author.roles):
            roll += [15]
          if(640972245292023838 not in message.author.roles):
            roll += [16]
          if(641528958491557899 not in message.author.roles):
            roll += [17]
          if(641073507987357722 not in message.author.roles):
            roll += [18]
          if(641073791958515742 not in message.author.roles):
            roll += [19]
          if(640972609525383235 not in message.author.roles):
            roll += [20]
          if(640976056127324170 not in message.author.roles):
            roll += [21]
            

          select = random.choice(roll)
          spun = f"Your next game to max is {games[select]}!"
          spunurl = f"{imgspin[select]}"
          spin.set_thumbnail(url = f"{spunurl}")

          if(len(roll) > 0):
            spin.add_field(
              name = f"{spun}",
              value = "Ping a Staff member to update your\nname in the sheet!\n\nGood Luck!"
            )
          else:
            spin = discord.Embed(
              title = "You seem to have maxed every game.",
              colour = discord.Colour.red()
            )
            spin.add_field(
              name = "Congrats? I guess? Please go outside <3",
              value = "\u200b"
            )
            spin.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/header-logo.png")

          


          await message.channel.send(content= "", embed = spin)
