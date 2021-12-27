from os.path    import join
from os         import remove

from discord    import HTTPException
from emoji      import emojize

import discord
import requests
import settings
import json
import os
import math
import datetime
import achList
import embeds
import random


apres = requests.get("https://api.hypixel.net/resources/achievements")
achres = json.loads(apres.text)

apiKey = os.getenv('APIKEY')

emoji1 = "<:achievement:819360686290370567>"
emoji2 = "<:fail:823712673249755176>"

gamesDict = {
  "speeduhc" : "Speed UHC",
  "tntgames" : "TNT Games",
  "general" : "General",
  "arena" : "Arena Brawl",
  "copsandcrims" : "Cops and Crims",
  "paintball" : "Paintball",
  "uhc" : "UHC",
  "warlords" : "Warlords",
  "skyblock" : "Skyblock",
  "murdermystery" : "Murder Mystery",
  "duels" : "Duels",
  "walls" : "Walls",
  "christmas2017" : "Christmas",
  "arcade" : "Arcade",
  "summer" : "Summer",
  "easter" : "Easter",
  "halloween2017" : "Halloween",
  "housing" : "Housing",
  "quake" : "Quake",
  "supersmash" : "Smash Heroes",
  "blitz" : "Blitz",
  "gingerbread" : "TKR",
  "buildbattle" : "Build Battle",
  "skyclash" : "Skyclash",
  "truecombat" : "Crazy Walls",
  "walls3" : "Mega Walls",
  "skywars" : "Skywars",
  "vampirez" : "VampireZ",
  "pit" : "Pit",
  "bedwars" : "Bedwars",
  "guess" : "||Game?||"
}

# Returns a path relative to the bot directory
def get_rel_path(rel_path):
    return join(settings.BASE_DIR, rel_path)

def add_to_config(cfgID, item):
  print(cfgID)
  print(item)
  return True

# Returns an emoji as required to send it in a message
# You can pass the emoji name with or without colons
# If fail_silently is True, it will not raise an exception
# if the emoji is not found, it will return the input instead
def get_emoji(emoji_name, fail_silently=False):
    alias = emoji_name if emoji_name[0] == emoji_name[-1] == ":" \
            else f":{emoji_name}:"
    the_emoji = emojize(alias, use_aliases=True)

    if the_emoji == alias and not fail_silently:
        raise ValueError(f"Emoji {alias} not found!")

    return the_emoji

gamesAlias = {
  "suhc" : "speeduhc",
  "speeduhc" : "speeduhc",
  "tnt" : "tntgames",
  "tntgames" : "tntgames",
  "tntag" : "tntgames",
  "gen" : "general",
  "general" : "general",
  "ab" : "arena",
  "arena" : "arena",
  "arenabrawl" : "arena",
  "cvc" : "copsandcrims",
  "paintball" : "paintball",
  "pb" : "paintball",
  "paint" : "paintball",
  "uhc" : "uhc",
  "warlords" : "warlords",
  "wl" : "warlords",
  "sb" : "skyblock",
  "skyblock" : "skyblock",
  "mm" : "murdermystery",
  "murdermystery" : "murdermystery",
  "murder" : "murdermystery",
  "duels" : "duels",
  "walls" : "walls",
  "xmas" : "christmas2017",
  "christmas" : "christmas2017",
  "christmas2017" : "christmas2017",
  "holiday" : "christmas2017", 
  "arcade" : "arcade",
  "summer" : "summer",
  "easter" : "easter",
  "halloween2017" : "halloween2017",
  "halloween" : "halloween2017",
  "housing" : "housing",
  "home" : "housing",
  "house" : "housing",
  "quake" : "quake",
  "qc" : "quake",
  "quakecraft" : "quake",
  "sh" : "supersmash",
  "supersmash" : "supersmash",
  "smash" : "supersmash",
  "smashheroes" : "supersmash",
  "blitz" : "blitz",
  "bsg" : "blitz",
  "sg" : "blitz",
  "blitzsg" : "blitz",
  "blitzsurvivalgames" : "blitz",
  "tkr" : "gingerbread",
  "turbokartracers" : "gingerbread",
  "gingerbread" : "gingerbread",
  "bb" : "buildbattle",
  "buildbattle" : "buildbattle",
  "build" : "buildbattle",
  "sc" : "skyclash",
  "skyclash" : "skyclash",
  "cw" : "truecombat",
  "crazywalls" : "truecombat",
  "truecombat" : "truecombat",
  "walls3" : "walls3",
  "mw" : "walls3",
  "megawalls" : "walls3",
  "sw" : "skywars",
  "skywars" : "skywars",
  "vz" : "vampirez",
  "vamp" : "vampirez",
  "vampz" : "vampirez",
  "vampirez" : "vampirez",
  "pit" : "pit",
  "thepit" : "pit",
  "bedwars" : "bedwars",
  "bw" : "bedwars",
  "bed" : "bedwars"
}

ExcludedChars = [
  "2017","2018","2019","2020","2021","2022", " ", "+", "/", "-", "%", "#", "*", "_", "?", "!", "(", ")", ",", "'", ":", ";", ".", "&"
]
def shortAns(inputStr, num):
  shortened = inputStr.lower()
  for x in ExcludedChars:
    shortened = shortened.replace(x,"")
  if(num == 1):
    shortened = convertToAlias(shortened)
  return shortened

def longAns(inputStr):
  try:
    return gamesDict[inputStr]
  except:
    return "Error"

def convertToAlias(inputStr):
  alias = inputStr
  if inputStr in gamesAlias:
    alias = gamesAlias[inputStr]
  return alias

def apFormat(inputAP, title):
  try:
    achName = inputAP[2]['name']
  except:
    achName = "Unknown AP"
  try:
    try:
      achGame = gamesDict[inputAP[0]]
    except:
      achGame = inputAP[0]
  except:
    achGame = "Unknown Game"
  try:
    achDesc = inputAP[2]['description']
  except:
    achDesc = "Unknown Description"
  try:
    achReward = inputAP[2]['points']
  except:
    achReward = '?'
  try:
    achUnlocked = "Unlocked by " + str(round(inputAP[2]["gamePercentUnlocked"],2)) + "% of players"
  except:
    achUnlocked = "\u200b"
  
  apEm = discord.Embed(title = f"{title}")
  apEm.set_thumbnail(url="https://freepngimg.com/thumb/minecraft/11-2-minecraft-diamond-png.png")
  apEm.add_field(name=f"{achName} [{achGame}]", value=f"{achDesc}", inline=False)
  apEm.add_field(name="Reward:", value=f"+{achReward} Achievement Points {emoji1}", inline=False)
  try:
    if inputAP[2]['legacy'] == True:
      apLegacy = True
  except:
    apLegacy = False
  if(apLegacy):
    temp = "LEGACY"
  else:
    temp = "\u200b"
  
  if(apLegacy == False and achUnlocked == "\u200b"):
    pass
  else:
    apEm.add_field(name = f"{temp}", value = f"{achUnlocked}", inline = False)

  apEm.set_footer(text="AP bot by Stuffy")
  return apEm

def randomAp(type, excluded):
  aplist = achres.copy()
  if(type == "all"):
    type = random.choice(["c","t"])
  for x in excluded:
    try:
      aplist["achievements"].remove(x)
    except:
      pass
  if("legacy" in excluded):
    legacy = True
  else:
    legacy = False
  if(type == "c"):
    game = random.choice(list(aplist["achievements"].keys()).copy())
    gameap = random.choice(list(aplist["achievements"][game]["one_time"].keys()).copy())
    try:
      if aplist["achievements"][game]["one_time"][gameap]["legacy"] and legacy:
        print("Legacy detected, rerolling.")
        return randomAp(type, excluded)
    except:
      return (f"{game}", "c" , aplist["achievements"][game]["one_time"][gameap].copy())
  elif(type == "t"):
    game = random.choice(list(aplist["achievements"].keys()).copy())
    try:
      gameap = random.choice(list(aplist["achievements"][game]["tiered"].keys()).copy())
      try:
        if aplist["achievements"][game]["tiered"][gameap]["legacy"] and legacy:
          print("Legacy detected, rerolling.")
          return randomAp(type, excluded)
      except:
        return (f"{game}", "t" , aplist["achievements"][game]["tiered"][gameap].copy())
    except:
      return randomAp(type, excluded)

async def removeroles(member,roles):
  for x in member.roles:
    if str(x) in roles:
      await member.remove_roles(x)
  return

def get_status(uuid):
  response = requests.get(f"https://api.hypixel.net/status?key={apiKey}&uuid={uuid}")
  json_data = json.loads(response.text)
  if json_data["success"] == False:
    print("Error getting status for " + uuid)
    return "Error"
  else:
    if json_data["session"]["online"] == True:
      return True
    else:
      return False

def checkperm(member):
  for x in member.roles:
    if 795115422185816076 == x.id or 818283784763473952 == x.id or str(member) in ["Stuffy#1359","Caps#1000"]:
      return True
  return False

def checkspecial(member,channel):
  #Checks if the person is verified and in stuffy disc, or if they are staff in ap disc in certain channels
  for x in member.roles:
    # verified role in stuffybothome and stuffy disc
    if 795115422185816076 == x.id or 818283784763473952 == x.id or str(member) == "Stuffy#1359":
      return True
    # staff role in caps disc and trial staff role
    if 717220615861567508 == x.id or 774717930117005337 == x.id:
      return True
  return False

def checkelite(member):
  for x in member.roles:
    if 841516808976465960 == x.id:
      return True
  return False

def checkbeta(channel):
  if(channel == 844821632781516830):
    return True
  return False


def get_profile(uuid):
  response = requests.get(f"https://api.hypixel.net/player?key={apiKey}&uuid={uuid}")
  json_data = json.loads(response.text)
  if json_data["success"] == False:
    print("Error getting profile for " + uuid)
    return "Error"
  
  return json_data

def get_maxes(uuid):
  profile = get_profile(uuid)
  aplist = achList.aplist
  maxes = []
  for x in aplist:
    includelegacy = False
    apgame = x[0]
    apgamename = x[1]
    if apgame in ["skyclash", "truecombat"]:
      includelegacy = True
    tempgive = True
    for y in achres['achievements'][apgame]["one_time"]:
      apdata = apgame + "_" + y.lower()
      try:
        if achres['achievements'][apgame]["one_time"][y]["legacy"] == True:
          legacy = True
      except:
        legacy = False
      if apdata not in profile["player"]["achievementsOneTime"] and ((not legacy) or includelegacy):
        tempgive = False
        print(f"Missing {apdata}")
        break
    if(tempgive):
      for y in achres['achievements'][apgame]["tiered"]:
        apdata = apgame + "_" + y.lower()
        try:
          playerap = profile["player"]["achievements"][apdata]
        except:
          playerap = 0
        try:
          if achres['achievements'][apgame]["tiered"][y]["legacy"] == True:
            legacy = True
        except:
          legacy = False
        if playerap < achres['achievements'][apgame]["tiered"][y]["tiers"][-1]["amount"] and ((not legacy) or includelegacy):
          tempgive = False
          print("Missing " + achres['achievements'][apgame]["tiered"][y]["name"])
          break
    if(tempgive):
      maxes += [apgamename]
  return maxes


def get_roles(username):
  roles = []
  response = requests.get(f"https://api.hypixel.net/player?key={apiKey}&name={username}")
  json_data = json.loads(response.text)
  try:
    ap = json_data['player']['achievementPoints']
  except:
    ap = 0

  ap = math.floor((ap+1)/1000)
  roles += [f'{ap}K AP']
  lvl = hpLvl(json_data['player']['networkExp'])
  lv = 0
  if(lvl >= 500):
    lv = 500
  elif(lvl >= 400):
    lv = 400
  elif(lvl >= 300):
    lv = 300
  elif(lvl >= 250):
    lv = 250
  elif(lvl >= 200):
    lv = 200
  elif(lvl >= 150):
    lv = 150
  elif(lvl >= 100):
    lv = 100
  
  if(lv != 0):
    roles += [f'Level {str(lv)}+']
  
  maxes = get_maxes(get_uuid(username))
  seasonal = 0
  for x in maxes:
    if x == "Summer" or x == "Halloween" or x == "Christmas" or x == "Easter":
      seasonal += 1
    else:
      roles += ["Max " + x]
  if seasonal == 4:
    roles += ["Max Seasonal"]


  return roles

def get_uuid(player):
  response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{player}")
  try:
    uuid = json.loads(response.text)['id']
    return uuid
  except:
    return "ERROR"
  
def get_Name(player):
  response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{player}")
  player = json.loads(response.text)['name']  
  return player

def get_discord(uuid):
  response = requests.get(f"https://api.hypixel.net/player?key={apiKey}&uuid={uuid}")
  json_data = json.loads(response.text)
  if(json_data['success'] == 'false'):
    return "ERROR"
  else:
    try:
        discTag = json_data['player']['socialMedia']['links']['DISCORD']
        return discTag
    except:
      return "ERROR"

def get_tourney(uuid):
  response = requests.get(f"https://api.hypixel.net/player?key={apiKey}&uuid={uuid}")
  json_data = json.loads(response.text)
  if(json_data['success'] == 'false'):
    return "ERROR"
  else:
    tourney = discord.Embed(
      title = f"Active Tournament: Tnt Run #1",
      colour = discord.Colour.orange()
    )

    tourney.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")

    tourney.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/TNT-64.png")

    player = json_data['player']['displayname']
    try:
      new = json_data['player']['tourney']['tnt_run_0']
    except:
      new = []
    '''
    try:
      tkills = json_data['player']['stats']['MCGO']['kills_tourney_mcgo_defusal_1']
    except:
      tkills = 0
    '''
    try:
      tdeaths = json_data['player']['stats']['TNTGames']['deaths_tourney_tnt_run_0']
    except:
      tdeaths = 0

    try:
      twins = json_data['player']['stats']['TNTGames']['wins_tourney_tnt_run_0']
    except:
      twins = 0
    '''
    try:
      trwins = json_data['player']['stats']['MCGO']['round_wins_tourney_mcgo_defusal_1']
    except:
      trwins = 0
    '''
    try:
      games = new['games_played']
    except:
      games = 0

    try:
      tributes = new['tributes_earned']
    except:
      tributes = 0

    try:
      minplayed = new['playtime']
    except:
      minplayed = 0

    val = f"{player} has played **{games}/120** games so far\n"
    val += f"with **{tributes}/100** tributes earned\n"
    val += f"and **{minplayed}** minutes played!\n\n"
    val += f"Wins: {twins}, Deaths: {tdeaths}\n"

    tourney.add_field(
      name = f"\u200b",
      value = f"{val}"
    )

    return tourney

def get_tnt(uuid):
  response = requests.get(f"https://api.hypixel.net/player?key={apiKey}&uuid={uuid}")
  json_data = json.loads(response.text)
  if(json_data['success'] == 'false'):
    return "ERROR"
  else:
    
    player = json_data['player']['displayname']
    tnt = discord.Embed(
      title = f"TNT Games Progress for {player}",
      colour = discord.Colour.red()
    )

    tnt.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")

    tnt.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/TNT-64.png")

    try:
      new = json_data['player']['achievements']
    except:
      new = []

    try:
      trun = "{:,}".format(new['tntgames_tnt_run_wins'])
    except:
      trun = 0
    try:
      bran = "{:,}".format(new['tntgames_block_runner'])
    except:
      bran = 0
    try:
      prun = "{:,}".format(new['tntgames_pvp_run_wins'])
    except:
      prun = 0
    try:
      prunk = "{:,}".format(new['tntgames_pvp_run_killer'])
    except:
      prunk = 0
    try:
      twiz = "{:,}".format(new['tntgames_wizards_wins'])
    except:
      twiz = 0
    try:
      twizk = "{:,}".format(new['tntgames_tnt_wizards_kills'])
    except:
      twizk = 0
    try:
      tbow = "{:,}".format(new['tntgames_bow_spleef_wins'])
    except:
      tbow = 0
    try:
      tag = "{:,}".format(new['tntgames_tnt_tag_wins'])
    except:
      tag = 0
    try:
      ttag = "{:,}".format(new['tntgames_clinic'])
    except:
      ttag = 0


    val = f"Tnt Run Wins: {trun}/500\n"
    val += f"Blocks Ran: {bran}/750,000\n\n"
    val += f"Pvp Run Wins: {prun}/250\n"
    val += f"Pvp Run Kills: {prunk}/750\n\n"
    val += f"Wizard Wins: {twiz}/500\n"
    val += f"Wizard Kills: {twizk}/10,000\n\n"
    val += f"Bow Spleef Wins: {tbow}/500\n\n"
    val += f"Tnt Tag Wins: {tag}/150\n"
    val += f"Tnt Tag Tags: {ttag}/7,500\n"

    tnt.add_field(
      name = f"\u200b",
      value = f"{val}"
    )

    return tnt
    
def get_tkr(uuid):
  response = requests.get(f"https://api.hypixel.net/player?key={apiKey}&uuid={uuid}")
  json_data = json.loads(response.text)
  if(json_data['success'] == 'false'):
    return "ERROR"
  else:
    
    player = json_data['player']['displayname']
    tkr = discord.Embed(
      title = f"TKR Unique Golds for {player}",
      colour = discord.Colour.blue()
    )

    tkr.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")

    tkr.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/TKR-64.png")

    try:
      new = json_data['player']['stats']['GingerBread']
    except:
      new = []

    tkrTracks = [
      ('gold_trophy_canyon', 'Canyon'),
      ('gold_trophy_hypixelgp', 'Hypixel GP'),
      ('gold_trophy_olympus', 'Olympus'),
      ('gold_trophy_retro', 'Retro'),
      ('gold_trophy_junglerush', 'Jungle Rush')
    ]
    val = ""
    tkrComplete = 0
    tkrTotal = 0
    for track in tkrTracks:
      tkrTotal += 1
      activeEmoji = emoji2
      try:
        if(new[track[0]] >= 1):
          activeEmoji = emoji1
          tkrComplete += 1
      except:
        pass
      val += f"{activeEmoji} {track[1]}\n"
    

    tkr.add_field(
      name = f"{tkrComplete}/{tkrTotal}",
      value = f"{val}"
    )

    return tkr
    

def get_quests(prof):
  q = 0
  used = []
  for x in prof['quests']:
    
    for y in prof['quests'][x]:
      qs = (prof['quests'][x]).get('completions',[])
      if x not in used:
        used += [x]
        q += len(qs)

  return q

def blitz(profile):
  try:
    bz = profile['player']['stats']['HungerGames']
  except:
    return "ERROR"
  player = profile['player']['displayname']
  count = 0
  data = ""

  try:
    b1 = bz['exp_ranger']
  except:
    b1 = 0

  try:
    b2 = bz['exp_donkeytamer']
  except:
    b2 = 0
  
  try:
    b3 = bz['exp_phoenix']
  except:
    b3 = 0

  try:
    b4 = bz['exp_warrior']
  except:
    b4 = 0

  b1a = f" ({round(b1/100,2)}%)"
  b1 = "{:,}".format(b1)
  b2a = f" ({round(b2/100,2)}%)"
  b2 = "{:,}".format(b2)
  b3a = f" ({round(b3/100,2)}%)"
  b3 = "{:,}".format(b3)
  b4a = f" ({round(b4/100,2)}%)"
  b4 = "{:,}".format(b4)


  data += f"**Ranger** {b1}/10,000{b1a}\n"
  data += f"**DonkeyTamer** {b2}/10,000{b2a}\n"
  data += f"**Phoenix** {b3}/10,000{b3a}\n"
  data += f"**Warrior** {b4}/10,000{b4a}\n"

  blitz = discord.Embed(
    title = f"{player}'s Blitz Ultimate Kit Xp",
    colour = discord.Colour.orange()
  )

  blitz.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")

  blitz.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/SG-64.png")

  blitz.add_field(
    name = f"\u200b",
    value = f"{data}"
  )

  return blitz

def get_blitz(uuid):
  response = requests.get(f"https://api.hypixel.net/player?key={apiKey}&uuid={uuid}")
  json_data = json.loads(response.text)
  if(json_data['success'] == 'false'):
    return "ERROR"
  else:
    return blitz(json_data)


def legs(profile):
  try:
    ap = profile['player']['achievementsOneTime']
  except:
    return "ERROR"
  player = profile['player']['displayname']
  
  count = 0
  data = ""
  if('walls3_legendary_cow' in ap):
    count += 1
    data += f"{emoji1} Legendary Cow\n"
  else:
    data += f"{emoji2} Legendary Cow\n"

  if('walls3_legendary_hunter' in ap):
    count += 1
    data += f"{emoji1} Legendary Hunter\n"
  else:
    data += f"{emoji2} Legendary Hunter\n"

  if('walls3_legendary_shark' in ap):
    count += 1
    data += f"{emoji1} Legendary Shark\n"
  else:
    data += f"{emoji2} Legendary Shark\n"

  if('walls3_legendary_dreadlord' in ap):
    count += 1
    data += f"{emoji1} Legendary Dreadlord\n"
  else:
    data += f"{emoji2} Legendary Dreadlord\n"

  if('walls3_legendary_golem' in ap):
    count += 1
    data += f"{emoji1} Legendary Golem\n"
  else:
    data += f"{emoji2} Legendary Golem\n"

  if('walls3_legendary_herobrine' in ap):
    count += 1
    data += f"{emoji1} Legendary Herobrine\n"
  else:
    data += f"{emoji2} Legendary Herobrine\n"

  if('walls3_legendary_pigman' in ap):
    count += 1
    data += f"{emoji1} Legendary Pigman\n"
  else:
    data += f"{emoji2} Legendary Pigman\n"

  if('walls3_legendary_zombie' in ap):
    count += 1
    data += f"{emoji1} Legendary Zombie\n"
  else:
    data += f"{emoji2} Legendary Zombie\n"

  if('walls3_legendary_arcanist' in ap):
    count += 1
    data += f"{emoji1} Legendary Arcanist\n"
  else:
    data += f"{emoji2} Legendary Arcanist\n"

  if('walls3_legendary_shaman' in ap):
    count += 1
    data += f"{emoji1} Legendary Shaman\n"
  else:
    data += f"{emoji2} Legendary Shaman\n"

  if('walls3_legendary_squid' in ap):
    count += 1
    data += f"{emoji1} Legendary Squid\n"
  else:
    data += f"{emoji2} Legendary Squid\n"

  if('walls3_legendary_enderman' in ap):
    count += 1
    data += f"{emoji1} Legendary Enderman\n"
  else:
    data += f"{emoji2} Legendary Enderman\n"

  data2 = ""

  if('walls3_legendary_blaze' in ap):
    count += 1
    data2 += f"{emoji1} Legendary Blaze\n"
  else:
    data2 += f"{emoji2} Legendary Blaze\n"

  if('walls3_legendary_skeleton' in ap):
    count += 1
    data2 += f"{emoji1} Legendary Skeleton\n"
  else:
    data2 += f"{emoji2} Legendary Skeleton\n"

  if('walls3_legendary_spider' in ap):
    count += 1
    data2 += f"{emoji1} Legendary Spider\n"
  else:
    data2 += f"{emoji2} Legendary Spider\n"

  if('walls3_legendary_pirate' in ap):
    count += 1
    data2 += f"{emoji1} Legendary Pirate\n"
  else:
    data2 += f"{emoji2} Legendary Pirate\n"

  if('walls3_legendary_creeper' in ap):
    count += 1
    data2 += f"{emoji1} Legendary Creeper\n"
  else:
    data2 += f"{emoji2} Legendary Creeper\n"

  if('walls3_legendary_assassin' in ap):
    count += 1
    data2 += f"{emoji1} Legendary Assassin\n"
  else:
    data2 += f"{emoji2} Legendary Assassin\n"


  if('walls3_legendary_werewolf' in ap):
    count += 1
    data2 += f"{emoji1} Legendary Werewolf\n"
  else:
    data2 += f"{emoji2} Legendary Werewolf\n"


  if('walls3_legendary_phoenix' in ap):
    count += 1
    data2 += f"{emoji1} Legendary Phoenix\n"
  else:
    data2 += f"{emoji2} Legendary Phoenix\n"


  if('walls3_legendary_automaton' in ap):
    count += 1
    data2 += f"{emoji1} Legendary Automaton\n"
  else:
    data2 += f"{emoji2} Legendary Automaton\n"


  if('walls3_legendary_moleman' in ap):
    count += 1
    data2 += f"{emoji1} Legendary Moleman\n"
  else:
    data2 += f"{emoji2} Legendary Moleman\n"


  if('walls3_legendary_renegade' in ap):
    count += 1
    data2 += f"{emoji1} Legendary Renegade\n"
  else:
    data2 += f"{emoji2} Legendary Renegade\n"


  if('walls3_legendary_snowman' in ap):
    count += 1
    data2 += f"{emoji1} Legendary Snowman\n"
  else:
    data2 += f"{emoji2} Legendary Snowman\n"

  
  legs = discord.Embed(
    title = f"{player}'s Legendaries",
    colour = discord.Colour.orange()
  )

  legs.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")

  legs.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

  legs.add_field(
    name = f"{count}/24 Achieved ({round(100*count/24,2)}%)",
    value = f"{data}"
  )
  legs.add_field(
    name = f"\u200b",
    value = f"{data2}"
  )

  return legs

def get_legs(uuid):
  response = requests.get(f"https://api.hypixel.net/player?key={apiKey}&uuid={uuid}")
  json_data = json.loads(response.text)
  if(json_data['success'] == 'false'):
    return "ERROR"
  else:
    return legs(json_data)

def bwc(profile):
  try:
    chal = profile['player']['stats']['Bedwars']
  except:
    return "ERROR"
  player = profile['player']['displayname']
  data1 = ""
  data2 = "\u200b"
  try:
    if(chal['bw_challenge_no_team_upgrades'] >= 1):
      data1 += f"{emoji1} Renegade\n"
  except:
    data1 += f"{emoji2} Renegade\n"
  try:
    if(chal['bw_challenge_no_utilities'] >= 1):
      data1 += f"{emoji1} Warmonger\n"
  except:
    data1 += f"{emoji2} Warmonger\n"
  try:
    if(chal['bw_challenge_selfish'] >= 1):
      data1 += f"{emoji1} Selfish\n"
  except:
    data1 += f"{emoji2} Selfish\n"
  try:
    if(chal['bw_challenge_slow_generator'] >= 1):
      data1 += f"{emoji1} Minimum Wage\n"
  except:
    data1 += f"{emoji2} Minimum Wage\n"
  try:
    if(chal['bw_challenge_assassin'] >= 1):
      data1 += f"{emoji1} Assassin\n"
  except:
    data1 += f"{emoji2} Assassin\n"
  try:
    if(chal['bw_challenge_reset_armor'] >= 1):
      data1 += f"{emoji1} Regular Shopper\n"
  except:
    data1 += f"{emoji2} Regular Shopper\n"
  try:
    if(chal['bw_challenge_invisible_shop'] >= 1):
      data1 += f"{emoji1} Invisible Shop\n"
  except:
    data1 += f"{emoji2} Invisible Shop\n"
  try:
    if(chal['bw_challenge_collector'] >= 1):
      data1 += f"{emoji1} Collector\n"
  except:
    data1 += f"{emoji2} Collector\n"
  try:
    if(chal['bw_challenge_woodworker'] >= 1):
      data1 += f"{emoji1} Woodworker\n"
  except:
    data1 += f"{emoji2} Woodworker\n"
  try:
    if(chal['bw_challenge_sponge'] >= 1):
      data1 += f"{emoji1} Bridging For Dummies\n"
  except:
    data1 += f"{emoji2} Bridging For Dummies\n"
  try:
    if(chal['bw_challenge_toxic_rain'] >= 1):
      data1 += f"{emoji1} Toxic Rain\n"
  except:
    data1 += f"{emoji2} Toxic Rain\n"
  try:
    if(chal['bw_challenge_defuser'] >= 1):
      data1 += f"{emoji1} Defuser\n"
  except:
    data1 += f"{emoji2} Defuser\n"
  try:
    if(chal['bw_challenge_mining_fatigue'] >= 1):
      data1 += f"{emoji1} Lazy Miner\n"
  except:
    data1 += f"{emoji2} Lazy Miner\n"
  try:
    if(chal['bw_challenge_no_healing'] >= 1):
      data1 += f"{emoji1} Ultimate UHC\n"
  except:
    data1 += f"{emoji2} Ultimate UHC\n"
  try:
    if(chal['bw_challenge_hotbar'] >= 1):
      data1 += f"{emoji1} Sleight of Hand\n"
  except:
    data1 += f"{emoji2} Sleight of Hand\n"
  try:
    if(chal['bw_challenge_weighted_items'] >= 1):
      data2 += f"{emoji1} Weighted Items\n"
  except:
    data2 += f"{emoji2} Weighted Items\n"
  try:
    if(chal['bw_challenge_knockback_stick_only'] >= 1):
      data2 += f"{emoji1} Social Distancing\n"
  except:
    data2 += f"{emoji2} Social Distancing\n"
  try:
    if(chal['bw_challenge_no_swords'] >= 1):
      data2 += f"{emoji1} Swordless\n"
  except:
    data2 += f"{emoji2} Swordless\n"
  try:
    if(chal['bw_challenge_archer_only'] >= 1):
      data2 += f"{emoji1} Marksman\n"
  except:
    data2 += f"{emoji2} Marksman\n"
  try:
    if(chal['bw_challenge_patriot'] >= 1):
      data2 += f"{emoji1} Patriot\n"
  except:
    data2 += f"{emoji2} Patriot\n"
  try:
    if(chal['bw_challenge_stamina'] >= 1):
      data2 += f"{emoji1} Stamina\n"
  except:
    data2 += f"{emoji2} Stamina\n"
  try:
    if(chal['bw_challenge_no_sprint'] >= 1):
      data2 += f"{emoji1} Old Man\n"
  except:
    data2 += f"{emoji2} Old Man\n"
  try:
    if(chal['bw_challenge_capped_resources'] >= 1):
      data2 += f"{emoji1} Capped Resources\n"
  except:
    data2 += f"{emoji2} Capped Resources\n"
  try:
    if(chal['bw_challenge_stop_light'] >= 1):
      data2 += f"{emoji1} Red Light, Green Light\n"
  except:
    data2 += f"{emoji2} Red Light, Green Light\n"
  try:
    if(chal['bw_challenge_delayed_hitting'] >= 1):
      data2 += f"{emoji1} Slow Reflexes\n"
  except:
    data2 += f"{emoji2} Slow Reflexes\n"
  try:
    if(chal['bw_challenge_no_hitting'] >= 1):
      data2 += f"{emoji1} Pacifist\n"
  except:
    data2 += f"{emoji2} Pacifist\n"
  try:
    if(chal['bw_challenge_master_assassin'] >= 1):
      data2 += f"{emoji1} Master Assassin\n"
  except:
    data2 += f"{emoji2} Master Assassin\n"
  try:
    if(chal['bw_challenge_no_shift'] >= 1):
      data2 += f"{emoji1} Standing Tall\n"
  except:
    data2 += f"{emoji2} Standing Tall\n"
  try:
    if(chal['bw_challenge_protect_the_president'] >= 1):
      data2 += f"{emoji1} Protect the President\n"
  except:
    data2 += f"{emoji2} Protect the President\n"
  try:
    if(chal['bw_challenge_cant_touch_this'] >= 1):
      data2 += f"{emoji1} Can't Touch This\n"
  except:
    data2 += f"{emoji2} Can't Touch This\n"

  bwc = discord.Embed(
    title = f"{player}'s Bedwars Challenges",
    colour = discord.Colour.blue()
  )

  bwc.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")

  bwc.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/BedWars-64.png")

  try:
    count = chal['bw_unique_challenges_completed']
  except:
    count = 0

  bwc.add_field(
    name = f"{count}/30 Completed ({round(100*count/30,2)}%)",
    value = f"{data1}"
  )
  bwc.add_field(
    name = f"\u200b",
    value = f"{data2}"
  )

  return bwc
  

def get_bwchallenges(uuid):
  response = requests.get(f"https://api.hypixel.net/player?key={apiKey}&uuid={uuid}")
  json_data = json.loads(response.text)
  if(json_data['success'] == 'false'):
    return "ERROR"
  else:
    return bwc(json_data)

def guild(uuid):
  response = requests.get(f"https://api.hypixel.net/guild?key={apiKey}&player={uuid}")
  json_data = json.loads(response.text)
  if(json_data['success'] == False):
    return "Error"
  else:
    try:
      name = "**" + json_data['guild']['name'] + "**"
    except:
      return "None"
  return name

def hpLvl(xp):
  REVERSE_PQ_PREFIX = -(10000 - 0.5 * 2500) / 2500
  REVERSE_CONST = REVERSE_PQ_PREFIX * REVERSE_PQ_PREFIX
  GROWTH_DIVIDES_2 = 2 / 2500

  lvl = math.floor(1 + REVERSE_PQ_PREFIX + math.sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * xp))

  return lvl

def get_date(firstLogin):
  new = datetime.datetime.fromtimestamp(int(firstLogin/1000)).strftime('%m/%d/%Y %H:%M')
  return new

def get_pstats(prof,player,uuid):
  temp = requests.get(f"https://api.slothpixel.me/api/players/{uuid}")
  json_data = json.loads(temp.text)

  try:
    ap = "{:,}".format(prof["achievementPoints"])
  except:
    ap = 0
  try:
    lvl = "{:,}".format(hpLvl(prof["networkExp"]))
  except:
    lvl = 0
  try:
    reward = "{:,}".format(prof["rewardScore"])
  except:
    reward = 0
  try:
    ver = prof["mcVersionRp"]
  except:
    ver = "Unknown"
  try:
    wins = "{:,}".format(prof["achievements"]["general_wins"])
  except:
    wins = 0
  try:
    quests = "{:,}".format(get_quests(prof))
  except:
    quests = 0
  try:
    firstLogin = get_date(json_data["first_login"])
  except:
    firstLogin = "Unknown"
  gld = guild(uuid)

  data = ""
  data += f"Quests Completed: **{quests}**\n"
  # data += f"Total Wins: **{wins}**\n"
  data += f"Guild: {gld}\n\n"
  data += f"Reward Streak: **{reward}**\n"
  data += f"Playing on version **{ver}**\n"
  data += f"First Login: {firstLogin}"
  progress = discord.Embed(
      title = f"Overall Stats for player {player}",
      colour = discord.Colour.blue()
    )

  progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")

  progress.set_thumbnail(url = f"https://crafatar.com/avatars/{uuid}")

  progress.add_field(name = f"{player} is level {lvl} with {ap} ap", value = f"{data}")

  return progress

def get_stats(player):
  response = requests.get(f"https://api.hypixel.net/player?key={apiKey}&uuid={player}")
  json_data = json.loads(response.text)
  if(json_data['success'] == False):
    return "ERROR"
  else:
    ret = json_data['player']
    name = json_data['player']['displayname']
    progress = get_pstats(ret,name,player)
    return progress

def get_pitprog(prof,player):
  try:
    pres = prof['profile']['prestiges'][-1]['index']
  except:
    pres = 0
  try:

    xp = "{:,}".format(prof['profile']['xp'])
    try:
      gpu = "{:,}".format(prof['pit_stats_ptl']['ingots_picked_up'])
    except:
      gpu = 0
    try:
      ghe = "{:,}".format(prof['pit_stats_ptl']['ghead_eaten'])
    except:
      ghe = 0
    try:
      tdg = "{:,}".format(prof['pit_stats_ptl']['extra_from_trickle_down'])
    except:
      tdg = 0
    try:
      eqa = "{:,}".format(prof['pit_stats_ptl']['endless_quiver_arrows'])
    except:
      eqa = 0
    try:
      ldp = "{:,}".format(prof['pit_stats_ptl']['lucky_diamond_pieces'])
    except:
      ldp = 0
    try:
      ob = "{:,}".format(prof['pit_stats_ptl']['obsidian_broken'])
    except:
      ob = 0
    try:
      vh = "{:,}".format(prof['pit_stats_ptl']['vampire_healed_hp'])
    except:
      vh = 0
    try:
      rpe = "{:,}".format(prof['pit_stats_ptl']['rage_potatoes_eaten'])
    except:
      rpe = 0
    try:
      bhb = "{:,}".format(prof['pit_stats_ptl']['bounties_of_500g_with_bh'])
    except:
      bhb = 0
    
    progress = discord.Embed(
      title = f"Pit Stats for player {player}",
      colour = discord.Colour.orange()
    )

    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")

    progress.set_thumbnail(url = "https://hypixel.net/attachments/pit-64-png.1641549/")



    prog = ""
    prog += f" Gold Picked Up: {gpu}/2,000\n"
    prog += f" Gold Heads Eaten: {ghe}/1,000\n"
    prog += f" Trickle Down Extra Gold: {tdg}/1,000\n"
    prog += f" Endless Quiver Arrows: {eqa}/1,500\n"
    prog += f" Lucky Diamond Pieces: {ldp}/50\n"
    prog += f" Obsidian Broken: {ob}/100\n"
    prog += f" Vampirism Healing: {vh}/15,000\n"
    prog += f" Rage Potatoes Eaten: {rpe}/100\n"
    prog += f" Bounties over 500g with Bounty Hunter: {bhb}/30\n"

    progress.add_field(name = f"Prestige: {pres}, Total XP: {xp}", value= f"{prog}")
  except:
    progress = discord.Embed(
      title = "There was an issue looking at your Pit Profile",
      colour = discord.Colour.red()
    )


  return progress

def get_pitprogress(uuid):
  response = requests.get(f"https://api.hypixel.net/player?key={apiKey}&uuid={uuid}")
  json_data = json.loads(response.text)
  if(json_data['success'] == False):
    print(apiKey + uuid)
    return "ERROR"
  else:
    ret = json_data['player']['stats']['Pit']
    name = json_data['player']['displayname']
    progress = get_pitprog(ret,name)
    return progress



def get_mwprog(prof,player,kit):
  #
  # COW
  #

  if(kit == "cow"):
    progress = discord.Embed(
      title = f"Cow skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      moo_brawl = "{:,}".format(prof['cow_bucket_barriers_broken'])
    except:
      moo_brawl = 0

    try:
      greedy_louis = "{:,}".format(prof['cow_ultra_pasteurized_drank'])
    except:
      greedy_louis = 0

    try:
      bio_restore = "{:,}".format(prof['cow_players_healed'])
    except:
      bio_restore = 0
    

    prog = ""
    prog += f"Moo Brawl: {moo_brawl}/600\n"
    prog += f"Greedy Louis: {greedy_louis}/500\n"
    prog += f"Biological Restoration: {bio_restore}/2,500\n"

    progress.add_field(name = "3 tracked skins", value = f"{prog}")
  
  #
  # HUNTER
  #
  elif(kit == "hunter"):
    progress = discord.Embed(
      title = f"Hunter skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      treasure_hunter = "{:,}".format(prof['hunter_g_activations'])
    except:
      treasure_hunter = 0

    try:
      cake_hunter = "{:,}".format(prof['cakes_found'])
    except:
      cake_hunter = 0
    

    prog = ""
    prog += f"Treasure Hunter: {treasure_hunter}/300\n"
    prog += f"Cake Hunter: {cake_hunter}/150\n"

    progress.add_field(name = "2 tracked skins", value = f"{prog}")

  #
  # SHARK
  #
  elif(kit == "shark"):
    progress = discord.Embed(
      title = f"Shark skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      hammerhead = "{:,}".format(prof['shark_water_kills'])
    except:
      hammerhead = 0

    

    prog = ""
    prog += f"Hammerhead: {hammerhead}/100\n"

    progress.add_field(name = "1 tracked skin", value = f"{prog}")

  #
  # DREADLORD
  #

  elif(kit == "dreadlord"):
    progress = discord.Embed(
      title = f"Dreadlord skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      rushlord = "{:,}".format(prof['dreadlord_wither_damage'])
    except:
      rushlord = 0

    try:
      breadlord = "{:,}".format(prof['dreadlord_bread_crafted'])
    except:
      breadlord = 0

    

    prog = ""
    prog += f"Rushlord: {rushlord}/20,000\n"
    prog += f"Breadlord: {breadlord}/617\n"

    progress.add_field(name = "2 tracked skins", value = f"{prog}")

  #
  # GOLEM
  #

  elif(kit == "golem"):
    progress = discord.Embed(
      title = f"Golem skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      timber = "{:,}".format(prof['golem_wood_chopped'])
    except:
      timber = 0
    

    prog = ""
    prog += f"Timber!: {timber}/5,000\n"

    progress.add_field(name = "1 tracked skin", value = f"{prog}")

  #
  # HEROBRINE
  #

  elif(kit == "herobrine"):
    progress = discord.Embed(
      title = f"Herobrine skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      lucky_sunny = "{:,}".format(prof['herobrine_treasures_found'])
    except:
      lucky_sunny = 0

    try:
      seasons_greetings = "{:,}".format(prof['herobrine_iron_armor_gifted_december'])
    except:
      seasons_greetings = 0
    

    prog = ""
    prog += f"Chests Found: {lucky_sunny}/1,000\n"
    prog += f"Seasons Greetings: {seasons_greetings}/1,000\n"

    progress.add_field(name = "2 tracked skins", value = f"{prog}")

  
  #
  # ZOMBIE
  #

  elif(kit == "zombie"):
    progress = discord.Embed(
      title = f"Zombie skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      sleepytime = "{:,}".format(prof['zombie_beds_crafted'])
    except:
      sleepytime = 0

    prog = ""
    prog += f"Sleepytime: {sleepytime}/50\n"

    progress.add_field(name = "1 tracked skin", value = f"{prog}")

    
  #
  # ARCANIST
  #

  elif(kit == "arcanist"):
    progress = discord.Embed(
      title = f"Arcanist skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      potions_of_death = "{:,}".format(prof['arcanist_c_total_final_kills'])
    except:
      potions_of_death = 0
    try:
      hard_as_steel = "{:,}".format(prof['arcanist_a_blocks_broken'])
    except:
      hard_as_steel = 0

    prog = ""
    prog += f"Potions of death: {potions_of_death}/8\n"
    prog += f"Hard as Steel: {hard_as_steel}/5,000\n"

    progress.add_field(name = "2 tracked skins", value = f"{prog}")

  
  #
  # ENDERMAN
  #

  elif(kit == "enderman"):
    progress = discord.Embed(
      title = f"Enderman skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      surprise = "{:,}".format(prof['enderman_activations'])
    except:
      surprise = 0

    try:
      try:
        efk = prof['enderman_final_kills_melee_behind']
      except:
        efk = 0
      try:
        efa = prof['enderman_final_assists_melee_behind']
      except:
        efa = 0
      sneak_attack = "{:,}".format(efk + efa)
    except:
      sneak_attack = 0
    

    prog = ""
    prog += f"Surprise: {surprise}/2,500\n"
    prog += f"Sneak Attack: {sneak_attack}/100\n"

    progress.add_field(name = "2 tracked skins", value = f"{prog}")

  #
  # BLAZE
  #
  elif(kit == "blaze"):
    progress = discord.Embed(
      title = f"Blaze skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      high_on_ores = "{:,}".format(prof['blaze_amount_healed'])
    except:
      high_on_ores = 0
    

    prog = ""
    prog += f"High on Ores: {high_on_ores}/2,000\n"

    progress.add_field(name = "1 tracked skin", value = f"{prog}")

  #
  # Skeleton
  #
  elif(kit == "skeleton"):
    progress = discord.Embed(
      title = f"Skeleton skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      marksman = "{:,}".format(prof['skeleton_final_kills_ranged_30'])
    except:
      marksman = 0

    try:
      skele_best_friend = "{:,}".format(prof['skeleton_diamond_ore_broken'])
    except:
      skele_best_friend = 0
    

    prog = ""
    prog += f"Marksman: {marksman}/25\n"
    prog += f"Skeleton's Best Friend: {skele_best_friend}/50\n"

    progress.add_field(name = "2 tracked skins", value = f"{prog}")

  #
  # SPIDER
  #
  elif(kit == "spider"):
    progress = discord.Embed(
      title = f"Spider skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      geronimo = "{:,}".format(prof['spider_meters_fallen'])
    except:
      geronimo = 0
    

    prog = ""
    prog += f"Geronimo: {geronimo}/25,000\n"

    progress.add_field(name = "1 tracked skin", value = f"{prog}")

  
  #
  # CREEPER
  #
  elif(kit == "creeper"):
    progress = discord.Embed(
      title = f"Creeper skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    
    try:
      mass_destruction = "{:,}".format(prof['creeper_a_blocks_broken'])
    except:
      mass_destruction = 0
    

    prog = ""
    prog += f"Mass Destruction: {mass_destruction}/3,000\n"

    progress.add_field(name = "1 tracked skin", value = f"{prog}")

  #
  # ASSASSIN
  #
  elif(kit == "assassin"):
    progress = discord.Embed(
      title = f"Assassin skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    
    try:
      dont_blink = "{:,}".format(prof['assassin_enemies_hit'])
    except:
      dont_blink = 0
    try:
      alchemy_100 = "{:,}".format(prof['assassin_master_alechmy_hearts'])
    except:
      alchemy_100 = 0
    

    prog = ""
    prog += f"Don't Blink: {dont_blink}/1,200\n"
    prog += f"Alchemy 100: {alchemy_100}/1,000\n"

    progress.add_field(name = "2 tracked skins", value = f"{prog}")


  #
  # WEREWOLF
  #
  elif(kit == "werewolf"):
    progress = discord.Embed(
      title = f"Werewolf skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      dirty_dog = "{:,}".format(prof['werewolf_final_kills_below_10_hp'])
    except:
      dirty_dog = 0
    try:
      time_to_diet = "{:,}".format(prof['werewolf_steaks_eaten'])
    except:
      time_to_diet = 0
    try:
      hunting_season = "{:,}".format(prof['werewolf_meters_walked_speed'])
    except:
      hunting_season = 0
    

    prog = ""
    prog += f"Dirty Dog: {dirty_dog}/15\n"
    prog += f"Time to Diet: {time_to_diet}/750\n"
    prog += f"Hunting Season: {hunting_season}/50,000\n"

    progress.add_field(name = "3 tracked skins", value = f"{prog}")

  #
  # PHOENIX
  #
  elif(kit == "phoenix"):
    progress = discord.Embed(
      title = f"Phoenix skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      nights_rest = "{:,}".format(prof['phoenix_amount_healed'])
    except:
      nights_rest = 0
    

    prog = ""
    prog += f"Night's Rest: {nights_rest}/1,000\n"

    progress.add_field(name = "1 tracked skin", value = f"{prog}")



  #
  # AUTOMATON
  #
  elif(kit == "automaton"):
    progress = discord.Embed(
      title = f"Automaton skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      terminated_script = "{:,}".format(prof['automaton_energy_syphoned'])
    except:
      terminated_script = 0
    

    prog = ""
    prog += f"Terminated Script: {terminated_script}/3,000\n"

    progress.add_field(name = "1 tracked skin", value = f"{prog}")



  #
  # MOLEMAN
  #

  elif(kit == "moleman"):
    progress = discord.Embed(
      title = f"Moleman skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      constructor = "{:,}".format(prof['moleman_blocks_placed_preparation'])
    except:
      constructor = 0

    try:
      heavy_eater = "{:,}".format(prof['moleman_c_junk_items_eaten'])
    except:
      heavy_eater = 0
    

    prog = ""
    prog += f"Constructor: {constructor}/15,000\n"
    prog += f"Heavy Eater: {heavy_eater}/1,000\n"

    progress.add_field(name = "2 tracked skins", value = f"{prog}")


  #
  # RENEGADE
  #

  elif(kit == "renegade"):
    progress = discord.Embed(
      title = f"Renegade skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      recycling = "{:,}".format(prof['renegade_arrows_from_rend'])
    except:
      recycling = 0

    try:
      captain_combo = "{:,}".format(prof['renegade_energy_from_grappling_hook'])
    except:
      captain_combo = 0
    

    prog = ""
    prog += f"Recycling: {recycling}/3,000\n"
    prog += f"Captain Combo: {captain_combo}/20,000\n"

    progress.add_field(name = "2 tracked skins", value = f"{prog}")

  #
  # SNOWMAN
  #
  elif(kit == "snowman"):
    progress = discord.Embed(
      title = f"Snowman skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      school_cancelled = "{:,}".format(prof['snowman_blizzard_seconds_slow'])
    except:
      school_cancelled = 0

    try:
      frosty_friendship = "{:,}".format(prof['snowman_snowmen_built'])
    except:
      frosty_friendship = 0

    try:
      australian_winter = "{:,}".format(prof['snowman_snowmen_players_hit'])
    except:
      australian_winter = 0
    

    prog = ""
    prog += f"School Cancelled: {school_cancelled}/7,200\n"
    prog += f"Frosty Friendship: {frosty_friendship}/500\n"
    prog += f"Australian Winter (seasonal): {australian_winter}/500\n"

    progress.add_field(name = "3 tracked skins", value = f"{prog}")

  #
  # SHAMAN
  #
  elif(kit == "shaman"):
    progress = discord.Embed(
      title = f"Shaman skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      much_dogs = "{:,}".format(prof['shaman_c_activations'])
    except:
      much_dogs = 0

    try:
      revenge_of_the_wolves = "{:,}".format(prof['shaman_c_total_final_kills'])
    except:
      revenge_of_the_wolves = 0

    try:
      spring_hero = "{:,}".format(prof['shaman_heroism_triggers_in_dm'])
    except:
      spring_hero = 0
    

    prog = ""
    prog += f"Much Dogs: {much_dogs}/500\n"
    prog += f"Revenge of the Wolves: {revenge_of_the_wolves}/5\n"
    prog += f"Spring Hero (seasonal): {spring_hero}/100\n"

    progress.add_field(name = "3 tracked skins", value = f"{prog}")
  
  #
  # PIGMAN
  #
  elif(kit == "pigman"):
    progress = discord.Embed(
      title = f"Pigman skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      collector = "{:,}".format(prof['shaman_c_activations'])
    except:
      collector = 0

    

    prog = ""
    prog += f"Collector: {collector}/500\n"

    progress.add_field(name = "1 tracked skin", value = f"{prog}")
      
  #
  # PIRATE
  #
  elif(kit == "pirate"):
    progress = discord.Embed(
      title = f"Pirate skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      grave_robber = "{:,}".format(prof['pirate_g_activations'])
    except:
      grave_robber = 0

    try:
      death_from_above = "{:,}".format(prof['pirate_b_total_final_kills'])
    except:
      death_from_above = 0

    

    prog = ""
    prog += f"Grave Robber: {grave_robber}/100\n"
    prog += f"Death from Above: {death_from_above}/12\n"

    progress.add_field(name = "2 tracked skins", value = f"{prog}")
    
  #
  # SQUID
  #
  elif(kit == "squid"):
    progress = discord.Embed(
      title = f"Squid skin progress for player {player}",
      colour = discord.Colour.orange()
    )
    progress.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")
    progress.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/MegaWalls-64.png")

    try:
      ysnp1 = prof['squid_defender_final_kills']
    except:
      ysnp1 = 0
    try:
      ysnp2 = prof['squid_defender_final_assists']
    except:
      ysnp2 = 0
    you_shall_not_pass = "{:,}".format(ysnp1 + ysnp2)

    try:
      trust_me_im = "{:,}".format(prof['squid_a_amount_healed'])
    except:
      trust_me_im = 0

    prog = ""
    prog += f"You shall not pass: {you_shall_not_pass}/10\n"
    prog += f"Trust me I'm a doctor: {trust_me_im}/2,500\n"
    progress.add_field(name = "2 tracked skins", value = f"{prog}")



  else:
    progress = discord.Embed(
      title = f"Unsupported class '{kit}', try using one of these:",
      description = "cow, hunter, shark, dreadlord, golem, herobrine, zombie, arcanist, shaman, squid, enderman, blaze, skeleton, spider, creeper, assassin, werewolf, phoenix, automaton, moleman, renegade, pigman, pirate, or snowman",
      colour = discord.Colour.red()
    )
  return progress


def get_mw(uuid,kit):
  response = requests.get(f"https://api.hypixel.net/player?key={apiKey}&uuid={uuid}")
  json_data = json.loads(response.text)
  if(json_data['success'] == False):
    return "ERROR"
  else:
    ret = json_data['player']['stats']['Walls3']
    name = json_data['player']['displayname']
    progress = get_mwprog(ret,name,kit)
    return progress

def get_session(uuid):
  response = requests.get(f"https://api.hypixel.net/status?key={apiKey}&uuid={uuid}")
  json_data = json.loads(response.text)
  if(json_data['success'] == 'false'):
    return -1
  if(json_data['session']['online'] == True):
    return 1
  else:
    return 0
  # session = json_data['session']['online']

# A shortcut to get a channel by a certain attribute
# Uses the channel name by default
# If many matching channels are found, returns the first one
def get_channel(client, value, attribute="name"):
    channel = next((c for c in client.get_all_channels() 
                    if getattr(c, attribute).lower() == value.lower()), None)
    if not channel:
        raise ValueError("No such channel")
    return channel


# Shortcut method to send a message in a channel with a certain name
# You can pass more positional arguments to send_message
# Uses get_channel, so you should be sure that the bot has access to only
# one channel with such name
async def send_in_channel(client, channel_name, *args):
    await client.send_message(get_channel(client, channel_name), *args)


# Attempts to upload a file in a certain channel
# content refers to the additional text that can be sent alongside the file
# delete_after_send can be set to True to delete the file afterwards
async def try_upload_file(client, channel, file_path, content=None, 
                          delete_after_send=False, retries=3):
    used_retries = 0
    sent_msg = None

    while not sent_msg and used_retries < retries:
        try:
            sent_msg = await client.send_file(channel, file_path,
                                              content=content)
        except HTTPException:
            used_retries += 1

    if delete_after_send:
        remove(file_path)

    if not sent_msg:
        await client.send_message(channel,
                                 "Oops, something happened. Please try again.")

    return sent_msg
