import discord
import settings

disclink = settings.DISC_LINK

emPremium = discord.Embed(
  title = "Oops!",
  description = f"Looks like youre trying to use an exclusive feature. These features are only available on the Stuffy Achievement Point Discord for verified members.\nIf you want access to these features, you can join the discord [here]({disclink}).\n\nYou can see all exclusive features by doing ap!exclusive",
  colour = discord.Colour.red()
)

cmds = [
  ("help","Help command"),
  ("faq","FAQ"),
  ("stats <player>","Overall hypixel stats"),
  ("spin","Gives a random game to max"),
  ("mw <player> <class>","Class skins progress"),
  ("pit <player>","Pit challenge progress"),
  ("tnt <player>","TNT Games tiered progress"),
  ("blitz <player>","Blitz Ultimates progress")
]

ehelp = ""
for x in range(len(cmds)):
  ehelp += "ap!**" + cmds[x][0] + "** → "+ cmds[x][1] + "\n"

emHelp = discord.Embed(
  title = "How to use the AP Machine",
  colour = discord.Colour.blue()
)

emHelp.add_field(
  name = "Be sure to put 'ap!' before your commands so I can recognize them!",
  value = f"{ehelp}"
)

excl = [
  ("verify <ign>", "link your discord to your account"),
  ("update <ign>", "update username and maxed games roles"),
  ("legs <player>","Mega Walls legendaries progress"),
  ("tourney <player>", "tournament stats"),
  ("status <player>","check a player's online status"),
  ("wins <player>","accurate hypixel wins counter")
]

eExclusive = ""
for x in range(len(excl)):
  eExclusive += "ap!**" + excl[x][0] + "** → "+ excl[x][1] + "\n"
eExclusive += f"\nMore features are in development. New features will exist as Beta Features on Stuffy's AP discord and some will remain exclusive.\n\nJoin Stuffy's AP discord [here]({disclink})."

emExclusive = discord.Embed(
  title = "AP commands exclusive to Stuffy's AP discord",
  colour = discord.Colour.blue()
)
emExclusive.add_field(
  name = "\u200b",
  value = f"{eExclusive}"
)
