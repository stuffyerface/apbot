from commands.base_command import BaseCommand
import discord
import embeds


# This is a convenient command that automatically generates a helpful
# message showing all available commands
class exclusive(BaseCommand):

    def __init__(self):
        description = "Displays this help message"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        perm = True
        if(perm):
          
          msg = embeds.emExclusive


          msg.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")

          msg.set_thumbnail(url = f"https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")



          await message.channel.send(content= "", embed = msg)
