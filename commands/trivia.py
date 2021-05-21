from commands.base_command  import BaseCommand
from utils                  import *
from random                 import randint
import time
import settings


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command

triviadict = {
  1 : ("Guess which game this achievement is from","game","||Game?||"),
  2 : ("Guess the name of this achievement", "name", "||Achievement Name?||"),
  3 : ("Guess how many points this achievement gives", "points", "||???||")
}

class Trivia(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Gives info on the current tournament"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = []
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
          if(settings.TRIVIAACTIVE == True):
            await message.channel.send("You must wait, there is already an active trivia game.")
          else:
            progress = randomAp()
            question = random.randint(1,3)
            if(question == 1): # for AP game
              answer = progress[0]
              progress = ("guess", progress[1], progress[2])
            else: # for AP name or points
              answer = progress[2][triviadict[question][1]]
              temp = progress[2]
              temp[triviadict[question][1]] = triviadict[question][2]
              progress = (progress[0], progress[1], temp)

            print(f"Correct Answer: {answer}")
            
            progress = apFormat(progress,triviadict[question][0])
            if(settings.TRIVIAACTIVE == True):
              await message.channel.send("You must wait, there is already an active trivia game.")
              return
            await message.channel.send(content = "", embed=progress)
            settings.TRIVIAACTIVE = True
            
            # GET RESPONSE
            ans = shortAns(str(answer),question)
            if(question == 1):
              answer = longAns(answer)
            def check(m):
              if m.channel != message.channel:
                return False
              elif(shortAns(str(m.content),question) == ans):
                return True
              else:
                return False
            try:
              response = await client.wait_for("message", check = lambda m: check(m),timeout = 15)
            except:
              await message.channel.send(f"You ran out of time! The correct answer was {answer}")
              settings.TRIVIAACTIVE = False

            else:
              await message.channel.send(f"Congrats {response.author.mention}! You got it right, the answer was {answer}")
              settings.TRIVIAACTIVE = False

        else:
          await message.channel.send(content = "", embed = embeds.emPremium)
