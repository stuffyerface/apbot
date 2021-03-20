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

          roll = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
          for x in message.author.roles:
            if(str(x) == 'Max Skyblock'):
              roll.remove(0)
            if(str(x) == 'Max Arcade'):
              roll.remove(1)
            if(str(x) == 'Max TNT Games'):
              roll.remove(2)
            if(str(x) == 'Max Blitz'):
              roll.remove(3)
            if(str(x) == 'Max Mega Walls'):
              roll.remove(4)
            if(str(x) == 'Max Cops and Crims'):
              roll.remove(5)
            if(str(x) == 'Max UHC'):
              roll.remove(6)
            if(str(x) == 'Max Warlords'):
              roll.remove(7)
            if(str(x) == 'Max SkyWars'):
              roll.remove(8)
            if(str(x) == 'Max Smash Heroes'):
              roll.remove(9)
            if(str(x) == 'Max Speed UHC'):
              roll.remove(10)
            if(str(x) == 'Max BedWars'):
              roll.remove(11)
            if(str(x) == 'Max Murder Mystery'):
              roll.remove(12)
            if(str(x) == 'Max Build Battle'):
              roll.remove(13)
            if(str(x) == 'Max Duels'):
              roll.remove(14)
            if(str(x) == 'Max Pit'):
              roll.remove(15)
            if(str(x) == 'Max Walls'):
              roll.remove(16)
            if(str(x) == 'Max Paintball'):
              roll.remove(17)
            if(str(x) == 'Max Arena Brawl'):
              roll.remove(18)
            if(str(x) == 'Max Quake'):
              roll.remove(19)
            if(str(x) == 'Max VampireZ'):
              roll.remove(20)
            if(str(x) == 'Max TKR'):
              roll.remove(21)
            

          select = random.choice(roll)
          spun = f"Your next game to max is {games[select]}!"
          spunurl = f"{imgspin[select]}"
          spin.set_thumbnail(url = f"{spunurl}")

          if(len(roll) > 0):
            spin.add_field(
              name = f"{spun}",
              value = "That's gonna be a tough one!\n\nGood Luck!"
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
          msg = message.author.mention
          await message.channel.send(content= msg, embed = spin)