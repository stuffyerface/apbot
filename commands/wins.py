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
          debug = False
          try:
            w_cvc = profile["player"]["achievements"]["copsandcrims_hero_terrorist"]
          except:
            w_cvc = 0
          try:
            w_bsg = profile["player"]["stats"]["HungerGames"]["wins_teams"]
          except:
            w_bsg = 0
          try:
            w_bsg2 = profile["player"]["stats"]["HungerGames"]["wins_solo_chaos"]
          except:
            w_bsg2 = 0
          try:
            w_bsg += profile["player"]["stats"]["HungerGames"]["wins"]
          except:
            pass
          try:
            w_walls = profile["player"]["stats"]["Walls"]["wins"]
          except:
            w_walls = 0
          try:
            w_mm = profile["player"]["stats"]["MurderMystery"]["wins"]
          except:
            w_mm = 0
          try:
            w_pb = profile["player"]["stats"]["Paintball"]["wins"]
          except:
            w_pb = 0
          try:
            w_vz = profile["player"]["stats"]["VampireZ"]["human_wins"]
          except:
            w_vz = 0
          try:
            w_vz += profile["player"]["stats"]["VampireZ"]["vampire_wins"]
          except:
            pass
          try:
            w_cw = profile["player"]["stats"]["TrueCombat"]["wins"]
          except:
            w_cw = 0
          try:
            w_arcade = profile["player"]["achievements"]["arcade_arcade_winner"]
          except:
            w_arcade = 0
          try:
            w_quake = profile["player"]["stats"]["Quake"]["wins_teams"]
          except:
            w_quake = 0
          try:
            w_quake += profile["player"]["stats"]["Quake"]["wins"]
          except:
            pass
          try:
            w_mw = profile["player"]["stats"]["Walls3"]["wins"]
          except:
            w_mw = 0
          try:
            w_bw = profile["player"]["stats"]["Bedwars"]["wins_bedwars"]
          except:
            w_bw = 0
          try:
            w_tnt = profile["player"]["stats"]["TNTGames"]["wins_bowspleef"]
          except:
            w_tnt = 0
          try:
            w_tnt += profile["player"]["stats"]["TNTGames"]["wins_tntrun"]
          except:
            pass
          try:
            w_tnt += profile["player"]["stats"]["TNTGames"]["wins_pvprun"]
          except:
            pass
          try:
            w_tnt += profile["player"]["stats"]["TNTGames"]["wins_capture"]
          except:
            pass
          try:
            w_tnt += profile["player"]["stats"]["TNTGames"]["wins_tntag"]
          except:
            pass
          try:
            w_ab = profile["player"]["stats"]["Arena"]["wins_1v1"]
          except:
            w_ab = 0
          try:
            w_ab += profile["player"]["stats"]["Arena"]["wins_2v2"]
          except:
            pass
          try:
            w_ab += profile["player"]["stats"]["Arena"]["wins_4v4"]
          except:
            pass
          try:
            w_suhc = profile["player"]["stats"]["SpeedUHC"]["wins"]
          except:
            w_suhc = 0
          try:
            w_uhc = profile["player"]["stats"]["UHC"]["wins"]
          except:
            w_uhc = 0
          try:
            w_uhc += profile["player"]["stats"]["UHC"]["wins_solo"]
          except:
            pass
          try:
            w_uhc += profile["player"]["stats"]["UHC"]["wins_red vs blue"]
          except:
            pass
          try:
            w_uhc += profile["player"]["stats"]["UHC"]["wins_no diamonds"]
          except:
            pass
          try:
            w_uhc += profile["player"]["stats"]["UHC"]["wins_vanilla doubles"]
          except:
            pass
          try:
            w_uhc += profile["player"]["stats"]["UHC"]["wins_brawl"]
          except:
            pass
          try:
            w_uhc += profile["player"]["stats"]["UHC"]["wins_solo_brawl"]
          except:
            pass
          try:
            w_uhc += profile["player"]["stats"]["UHC"]["wins_duo brawl"]
          except:
            pass
          try:
            w_wl = profile["player"]["stats"]["Battleground"]["wins"]
          except:
            w_wl = 0
          try:
            w_sw = profile["player"]["stats"]["SkyWars"]["wins"]
          except:
            w_sw = 0
          try:
            w_tkr = profile["player"]["stats"]["GingerBread"]["gold_trophy"]
          except:
            w_tkr = 0
          try:
            w_sh = profile["player"]["stats"]["SuperSmash"]["wins_normal"]
          except:
            w_sh = 0
          try:
            w_sh += profile["player"]["stats"]["SuperSmash"]["wins_teams"]
          except:
            pass
          try:
            w_sh += profile["player"]["stats"]["SuperSmash"]["wins_2v2"]
          except:
            pass
          try:
            w_sc = profile["player"]["stats"]["SkyClash"]["wins"]
          except:
            w_sc = 0
          try:
            w_bb = profile["player"]["stats"]["BuildBattle"]["wins_solo_normal"]
          except:
            w_bb = 0
          try:
            w_bb += profile["player"]["stats"]["BuildBattle"]["wins_teams_normal"]
          except:
            pass
          try:
            w_bb += profile["player"]["stats"]["BuildBattle"]["wins_guess_the_build"]
          except:
            pass
          try:
            w_bb += profile["player"]["stats"]["BuildBattle"]["wins_solo_pro"]
          except:
            pass
          try:
            w_bb += profile["player"]["stats"]["BuildBattle"]["wins_halloween"]
          except:
            pass
          try:
            w_d = profile["player"]["stats"]["Duels"]["wins"]
          except:
            w_d = 0
          try:
            w_ww = profile["player"]["stats"]["WoolGames"]["wool_wars"]["wins"]
          except:
            w_ww = 0
          
          print(wins)
          wins = w_arcade + w_ab + w_bw + w_bsg + w_bsg2 + w_bb + w_cvc + w_cw + w_d + w_mw + w_mm + w_pb + w_quake + w_sc + w_sw + w_sh + w_suhc + w_tnt + w_tkr + w_uhc + w_vz + w_walls + w_wl + w_ww
          wins = math.trunc(wins)
          if(debug):
            print(f" Arcade: {w_arcade} Arena: {w_ab} Bedwars: {w_bw}\n Blitz: {w_bsg + w_bsg2} Build Battle: {w_bb} CvC: {w_cvc} \n Crazy Walls: {w_cw} Duels: {w_d} Mega Walls: {w_mw}\n Murder Mystery: {w_mm} Paintball: {w_pb} Quake: {w_quake}\n Skyclash: {w_sc} Skywars: {w_sw} Smash Heroes: {w_sh}\n Speed UHC: {w_suhc} Tnt Games: {w_tnt} TKR: {w_tkr}\n UHC: {w_uhc} VampireZ: {w_vz} Walls: {w_walls}\n Warlords: {w_wl}")
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
