from commands.base_command  import BaseCommand
from utils                  import *
from random                 import randint


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command

class Wins(BaseCommand):

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
        
        if(checkspecial(message.author,message.channel)):
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
          
          wins = 0
          print
          try:
            wins += profile["player"]["achievements"]["copsandcrims_hero_terrorist"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["HungerGames"]["wins_teams"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["HungerGames"]["wins_solo_chaos"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["Walls"]["wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["MurderMystery"]["wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["Paintball"]["wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["VampireZ"]["human_wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["VampireZ"]["vampire_wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["TrueCombat"]["wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["arcade_arcade_winner"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["Quake"]["wins_teams"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["Quake"]["wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["Walls3"]["wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["Bedwars"]["wins_bedwars"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["TNTGames"]["wins_bowspleef"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["TNTGames"]["wins_tntrun"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["TNTGames"]["wins_pvprun"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["TNTGames"]["wins_capture"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["TNTGames"]["wins_tntag"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["Arena"]["wins_1v1"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["Arena"]["wins_2v2"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["Arena"]["wins_4v4"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["SpeedUHC"]["wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["UHC"]["wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["UHC"]["wins_solo"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["Battleground"]["wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["SkyWars"]["wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["GingerBread"]["gold_trophy"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["SuperSmash"]["wins_normal"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["SuperSmash"]["wins_teams"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["SuperSmash"]["wins_2v2"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["SkyClash"]["wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["BuildBattle"]["wins_solo_normal"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["BuildBattle"]["wins_teams_normal"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["BuildBattle"]["wins_guess_the_build"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["BuildBattle"]["wins_solo_pro"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["Duels"]["wins"]
          except:
            pass
          

          wins = "{:,}".format(wins)
          embed = discord.Embed(
            title = f"{get_Name(username)} has {wins} total hypixel wins.",
            description = "If you think this number is inaccurate, explain\nwhich stat you believe to be missing in <#822665659162558564>.",
            colour = discord.Colour.blue()
          )
          embed.set_thumbnail(url = f"https://crafatar.com/avatars/{uuid}?size=100")

          await message.channel.send(content= "", embed = embed)
        else:
          await message.channel.send(content= "", embed = embeds.emPremium)
