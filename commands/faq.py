from commands.base_command import BaseCommand
import discord


# This is a convenient command that automatically generates a helpful
# message showing all available commands
class faq(BaseCommand):

    def __init__(self):
        description = "Answers some FAQ about Stuffy Bot"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        perm = False
        for x in message.author.roles:
          if(str(x) == 'Verified'):
            perm = True
        if(perm):
          msg = discord.Embed(
            title = f"Stuffy Bot FAQ",
            colour = discord.Colour.blue()) 

          faq = ""
          faq += "**Q**: Why is my join date wrong?\n"
          faq += "**A**: Hypixel added joindate to the API in August 2013, so any joindate before that cant be tracked\n\n"

          faq += "**Q**: Why do some mw classes not work\n"
          faq += "**A**: I havent finished them all yet\n\n"

          faq += "**Q**: Why have my stats not updated?\n"
          faq += "**A**: The hypixel api updates very infrequently. You can sometimes force it to update by changing lobbies\n\n"
          



          msg.add_field(name= "Please read before pinging or asking for help", value = f"{faq}")

          msg.set_footer(text = "AP bot by Stuffy", icon_url="https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")

          msg.set_thumbnail(url = f"https://crafatar.com/avatars/2cfc8db5-71ed-4eb3-aacd-53b8abff5ee2?size=100")


          await message.channel.send(content= "", embed = msg)
