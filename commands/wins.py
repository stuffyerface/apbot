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
        
        if(checkperm(message.author)):
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
            wins += profile["player"]["achievements"]["blitz_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["paintball_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["quake_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["tnt_games_bow_spleef_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["tnt_games_tnt_run_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["tnt_games_tnt_wizards_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["vampirez_survivor_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["walls_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["skywars_wins_solo"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["skywars_wins_team"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["warlords_ctf_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["warlords_dom_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["skywars_wins_mega"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["skyclash_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["warlords_tdm_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["tnt_games_tnt_tag_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["tnt_games_pvp_run_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["bedwars_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["blitz_wins_teams"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["walls3_wins"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["skywars_wins_lab"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["arena_bossed"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["uhc_champion"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["supersmash_smash_winner"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["copsandcrims_hero_terrorist"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["arcade_arcade_winner"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["gingerbread_winner"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["truecombat_team_winner"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["truecombat_solo_winner"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["speeduhc_uhc_master"]
          except:
            pass
          try:
            wins += profile["player"]["achievements"]["duels_duels_winner"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["BuildBattle"]["wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["MurderMystery"]["wins"]
          except:
            pass
          try:
            wins += profile["player"]["stats"]["VampireZ"]["vampire_wins"]
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