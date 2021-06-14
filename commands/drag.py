from commands.base_command  import BaseCommand
from utils                  import *
from random                 import randint
from datetime               import datetime


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command

class Drag(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Shows mega walls legendaries of a player"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["eyes","mf","petluck"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object
        
        if(message.channel.id == 818927807719407686):
          eyes = int(params[0])
          mf = int(params[1])
          pl =  int(params[2])

          drops = {
            "Dragon Horn" : 0.00,
            "Dragon Claw" : 0.00,
            "AOTD" : 0.00,
            "Epic Pet" : 0.00,
            "Leg Pet" : 0.00,
            "Chestplate" : 0.00,
            "Leggings" : 0.00,
            "Dragon Scale" : 0.00,
            "Helmet" : 0.00,
            "Boots" : 0.00,
            "Travel Scroll" : 0.00,
            "Fragged" : 1.00
          }

          weight = 150 + eyes * 100
          remaining = drops["Fragged"]
          if(remaining >= 0 and weight >= 450):
            chance = min(0.96, 0.96 * (mf+100)/100 * .02 * eyes)
            drops["Fragged"] -= chance*remaining
            drops["Dragon Claw"] += chance*remaining
          
          remaining = drops["Fragged"]
          if(remaining >= .04001 and weight >= 450):
            chance = min(0.96, 0.96 * (mf+100)/100 * .03 * eyes)
            drops["Fragged"] -= chance*remaining
            drops["AOTD"] += chance*remaining
          
          # 4% to get superior
          remaining = drops["Fragged"]
          if(remaining >= 0 and weight >= 450):
            chance = min(0.04, 0.04 * (mf+100)/100 * 0.30)
            drops["Fragged"] -= chance
            drops["Dragon Horn"] += chance

          remaining = drops["Fragged"]
          if(remaining >= 0 and weight >= 450):
            chance = min(1.00, (pl+mf+100)/100 * 0.0005 * eyes)
            drops["Fragged"] -= chance*remaining
            drops["Epic Pet"] += chance*remaining

          remaining = drops["Fragged"]
          if(remaining >= 0 and weight >= 450):
            chance = min(1.00, (pl+mf+100)/100 * 0.0001 * eyes)
            drops["Fragged"] -= chance*remaining
            drops["Leg Pet"] += chance*remaining

          remaining = drops["Fragged"]
          if(remaining >= 0 and weight >= 410):
            chance = min(1.00, (mf+100)/100 * 0.30)
            drops["Fragged"] -= chance*remaining
            drops["Chestplate"] += chance*remaining

          remaining = drops["Fragged"]
          if(remaining >= 0 and weight >= 360):
            chance = min(1.00, (mf+100)/100 * .30)
            drops["Fragged"] -= chance*remaining
            drops["Leggings"] += chance*remaining

          remaining = drops["Fragged"]
          if(remaining >= 0 and weight >= 300):
            chance = min(1.00,0.16 * (mf+100)/100 * .30)
            drops["Fragged"] -= chance*remaining
            drops["Dragon Scale"] += chance*remaining

          remaining = drops["Fragged"]
          if(remaining >= 0 and weight >= 295):
            chance = min(1.00, (mf+100)/100 * .30)
            drops["Fragged"] -= chance*remaining
            drops["Helmet"] += chance*remaining

          remaining = drops["Fragged"]
          if(remaining >= 0 and weight >= 290):
            chance = min(1.00, (mf+100)/100 * .30)
            drops["Fragged"] -= chance*remaining
            drops["Boots"] += chance*remaining

          remaining = drops["Fragged"]
          if(remaining >= 0 and weight >= 250):
            chance = min(1.00,0.16 * (mf+100)/100 * 0.35 * eyes)
            drops["Fragged"] -= chance*remaining
            drops["Travel Scroll"] += chance*remaining
          if(drops["Fragged"] <= 0):
            drops["Fragged"] = 0
          
          r1 = str(round(drops["Dragon Horn"] * 100, 3))
          r2 = str(round(drops["Dragon Claw"] * 100, 3))
          r3 = str(round(drops["AOTD"] * 100, 3))
          r4 = str(round(drops["Epic Pet"] * 100, 3))
          r5 = str(round(drops["Leg Pet"] * 100, 3))
          r6 = str(round(drops["Chestplate"] * 100, 3))
          r7 = str(round(drops["Leggings"] * 100, 3))
          r8 = str(round(drops["Dragon Scale"] * 100, 3))
          r9 = str(round(drops["Helmet"] * 100, 3))
          r10 = str(round(drops["Boots"] * 100, 3))
          r11 = str(round(drops["Travel Scroll"] * 100, 3))
          r12 = str(round(drops["Fragged"] * 100, 3))
          retVal = f"Drops with\n**{eyes}** Eyes, **{mf}** Magic Find, **{pl}** Pet Luck\n\nDragon Horn: {r1}% \nDragon Claw: {r2}% \nAOTD: {r3}% \nEpic Pet: {r4}% \nLeg Pet: {r5}% \nChestplate: {r6}% \nLeggings: {r7}% \nDragon Scale: {r8}% \nHelmet: {r9}% \nBoots: {r10}% \nTravel Scroll: {r11}% \nFragged: {r12}% "




          await message.channel.send(content= f"{retVal}")
