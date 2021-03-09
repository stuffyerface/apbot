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

apiKey = os.getenv('APIKEY')

# Returns a path relative to the bot directory
def get_rel_path(rel_path):
    return join(settings.BASE_DIR, rel_path)


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

def removeroles(member,roles):
  for x in member.roles:
    if str(x) in roles:
      await member.remove_roles(x)
  return


def get_roles(username):
  roles = []
  response = requests.get(f"https://api.hypixel.net/player?key={apiKey}&name={username}")
  json_data = json.loads(response.text)
  try:
    ap = json_data['player']['achievementPoints']
  except:
    ap = 0

  
  
  ap = math.floor(ap/1000)
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
  
  achs = achList.achs
  for x in range(len(achs)):
    giveR = True
    for y in achs[x][0]:
      if y in json_data['player']['achievementsOneTime']:
        pass
      else:
        giveR = False
        break
    if(giveR):
      for y in achs[x][1]:
        if json_data['player']['achievements'][y[0]] < y[1]:
          giveR= False
          break
        else:
          continue
    if(giveR):
       roles += [achs[x][2]]

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
      title = f"Active Tournament: CVC Defusal #2",
      colour = discord.Colour.orange()
    )

    tourney.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")

    tourney.set_thumbnail(url = "https://hypixel.net/styles/hypixel-v2/images/game-icons/CVC-64.png")

    player = json_data['player']['displayname']
    try:
      new = json_data['player']['tourney']['mcgo_defusal_1']
    except:
      new = []

    try:
      tkills = json_data['player']['stats']['MCGO']['kills_tourney_mcgo_defusal_1']
    except:
      tkills = 0

    try:
      tdeaths = json_data['player']['stats']['MCGO']['deaths_tourney_mcgo_defusal_1']
    except:
      tdeaths = 0

    try:
      twins = json_data['player']['stats']['MCGO']['game_wins_tourney_mcgo_defusal_1']
    except:
      twins = 0

    try:
      trwins = json_data['player']['stats']['MCGO']['round_wins_tourney_mcgo_defusal_1']
    except:
      trwins = 0

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

    val = f"{player} has played **{games}/40** games so far\n"
    val += f"with **{tributes}/100** tributes earned\n"
    val += f"and **{minplayed}** minutes played!\n\n"
    val += f"Kills: {tkills}, Deaths: {tdeaths}\n"
    val += f"Round Wins: {trwins}, Wins: {twins}\n"

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
    data += ":gem: Legendary Cow\n"
  else:
    data += ":x: Legendary Cow\n"

  if('walls3_legendary_hunter' in ap):
    count += 1
    data += ":gem: Legendary Hunter\n"
  else:
    data += ":x: Legendary Hunter\n"

  if('walls3_legendary_shark' in ap):
    count += 1
    data += ":gem: Legendary Shark\n"
  else:
    data += ":x: Legendary Shark\n"

  if('walls3_legendary_dreadlord' in ap):
    count += 1
    data += ":gem: Legendary Dreadlord\n"
  else:
    data += ":x: Legendary Dreadlord\n"

  if('walls3_legendary_golem' in ap):
    count += 1
    data += ":gem: Legendary Golem\n"
  else:
    data += ":x: Legendary Golem\n"

  if('walls3_legendary_herobrine' in ap):
    count += 1
    data += ":gem: Legendary Herobrine\n"
  else:
    data += ":x: Legendary Herobrine\n"

  if('walls3_legendary_pigman' in ap):
    count += 1
    data += ":gem: Legendary Pigman\n"
  else:
    data += ":x: Legendary Pigman\n"

  if('walls3_legendary_zombie' in ap):
    count += 1
    data += ":gem: Legendary Zombie\n"
  else:
    data += ":x: Legendary Zombie\n"

  if('walls3_legendary_arcanist' in ap):
    count += 1
    data += ":gem: Legendary Arcanist\n"
  else:
    data += ":x: Legendary Arcanist\n"

  if('walls3_legendary_shaman' in ap):
    count += 1
    data += ":gem: Legendary Shaman\n"
  else:
    data += ":x: Legendary Shaman\n"

  if('walls3_legendary_squid' in ap):
    count += 1
    data += ":gem: Legendary Squid\n"
  else:
    data += ":x: Legendary Squid\n"

  if('walls3_legendary_enderman' in ap):
    count += 1
    data += ":gem: Legendary Enderman\n"
  else:
    data += ":x: Legendary Enderman\n"

  data2 = ""

  if('walls3_legendary_blaze' in ap):
    count += 1
    data2 += ":gem: Legendary Blaze\n"
  else:
    data2 += ":x: Legendary Blaze\n"

  if('walls3_legendary_skeleton' in ap):
    count += 1
    data2 += ":gem: Legendary Skeleton\n"
  else:
    data2 += ":x: Legendary Skeleton\n"

  if('walls3_legendary_spider' in ap):
    count += 1
    data2 += ":gem: Legendary Spider\n"
  else:
    data2 += ":x: Legendary Spider\n"

  if('walls3_legendary_pirate' in ap):
    count += 1
    data2 += ":gem: Legendary Pirate\n"
  else:
    data2 += ":x: Legendary Pirate\n"

  if('walls3_legendary_creeper' in ap):
    count += 1
    data2 += ":gem: Legendary Creeper\n"
  else:
    data2 += ":x: Legendary Creeper\n"

  if('walls3_legendary_assassin' in ap):
    count += 1
    data2 += ":gem: Legendary Assassin\n"
  else:
    data2 += ":x: Legendary Assassin\n"


  if('walls3_legendary_werewolf' in ap):
    count += 1
    data2 += ":gem: Legendary Werewolf\n"
  else:
    data2 += ":x: Legendary Werewolf\n"


  if('walls3_legendary_phoenix' in ap):
    count += 1
    data2 += ":gem: Legendary Phoenix\n"
  else:
    data2 += ":x: Legendary Phoenix\n"


  if('walls3_legendary_automaton' in ap):
    count += 1
    data2 += ":gem: Legendary Automaton\n"
  else:
    data2 += ":x: Legendary Automaton\n"


  if('walls3_legendary_moleman' in ap):
    count += 1
    data2 += ":gem: Legendary Moleman\n"
  else:
    data2 += ":x: Legendary Moleman\n"


  if('walls3_legendary_renegade' in ap):
    count += 1
    data2 += ":gem: Legendary Renegade\n"
  else:
    data2 += ":x: Legendary Renegade\n"


  if('walls3_legendary_snowman' in ap):
    count += 1
    data2 += ":gem: Legendary Snowman\n"
  else:
    data2 += ":x: Legendary Snowman\n"

  
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
  
  get_date(prof["firstLogin"])


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
    firstLogin = get_date(prof["firstLogin"])
  except:
    firstLogin = "Unknown"
  gld = guild(uuid)

  data = ""
  data += f"Quests Completed: **{quests}**\n"
  data += f"Total Wins: **{wins}**\n"
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
    prog += f"Timer!: {timber}/5,000\n"

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



  else:
    progress = discord.Embed(
      title = f"Unsupported class '{kit}', try using one of these:",
      description = "cow, hunter, shark, dreadlord, golem, herobrine, zombie, enderman, blaze, skeleton, spider, creeper, assassin, werewolf, phoenix, moleman, renegade, or snowman\n\n This feature is in beta, some classes are missing but all will be added eventually. Be Patient",
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
