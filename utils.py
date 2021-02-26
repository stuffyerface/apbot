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
    quests = "{:,}".format(prof["achievements"]["general_quest_master"])
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
      ba_boom = "{:,}".format(prof['hunter_new_a'])
    except:
      ba_boom = 0

    try:
      cake_hunter = "{:,}".format(prof['cakes_found'])
    except:
      cake_hunter = 0
    

    prog = ""
    prog += f"Treasure Hunter: {treasure_hunter}/300\n"
    prog += f"BA-BOOM!: {ba_boom}/5\n"
    prog += f"Cake Hunter: {cake_hunter}/150\n"

    progress.add_field(name = "3 tracked skins", value = f"{prog}")

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
      description = "cow, hunter, shark, dreadlord, golem, herobrine, enderman, blaze, spider, moleman, renegade, or snowman\n\n This feature is in beta, some classes are missing but all will be added eventually. Be Patient",
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
