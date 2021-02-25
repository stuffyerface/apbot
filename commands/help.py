from commands.base_command import BaseCommand
import discord


# This is a convenient command that automatically generates a helpful
# message showing all available commands
class help(BaseCommand):

    def __init__(self):
        description = "Displays this help message"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        perm = False
        for x in message.author.roles:
          if(str(x) == 'Verified'):
            perm = True
        if(perm):
          
          cmds = "example: ap!pit Stuffy"
          cmds += "\n\n"
          cmds += "**ap!faq** → Read the FAQ before dm'ing or ping'ing with questions\n"
          cmds += "**ap!help** → Displays this help message in case you forget any commands\n"
          cmds += "**ap!stats <player>** → Gives an overview of a players hypixel stats\n"
          cmds += "**ap!pit <player>** → Shows progress on some pesky challenge achievements in pit\n"
          cmds += "**ap!mw <player> <class>** → Shows progress on skins for a certain mega walls class\n"


          msg = discord.Embed(
            title = f"How to use the AP Machine",
            colour = discord.Colour.blue()) 

          
          msg.add_field(name= "Make sure you put 'ap!' before your commands so I can recognize them!", value = f"{cmds}")

          msg.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")

          msg.set_thumbnail(url = f"https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")



          await message.channel.send(content= "", embed = msg)
