from events.base_event      import BaseEvent
import requests
import json
from datetime               import datetime, date
from math                   import floor
import discord
import settings
import utils


# Your friendly example event
# You can name this class as you like, but make sure to set BaseEvent
# as the parent class

class ResourceUpdate(BaseEvent):

    def __init__(self):
        interval_minutes = 1  # Set the interval for this event
        super().__init__(interval_minutes)

    # Override the run() method
    # It will be called once every {interval_minutes} minutes
    
    async def run(self, client):
        apres = requests.get("https://api.hypixel.net/resources/achievements")
        achres = json.loads(apres.text)
        if achres["success"] == True:
          lu = achres["lastUpdated"]
          if lu != settings.RESOURCE_LAST_UPDATED:
            if(settings.RESOURCE_LAST_UPDATED != 0):
              rt = datetime.utcfromtimestamp(lu/1000).strftime('%m/%d/%Y %H:%M')
              channel = client.get_channel(818611323755036702)
              await channel.send(content = f"Resources Updated: {rt}")
            settings.RESOURCE_LAST_UPDATED = lu
        gameres = requests.get("https://api.hypixel.net/resources/games")
        gmres = json.loads(gameres.text)
        if gmres["success"] == True:
          lu = gmres["lastUpdated"]
          if lu > settings.GAMES_LAST_UPDATED:
            if(settings.GAMES_LAST_UPDATED != 0):
              rt = datetime.utcfromtimestamp(lu/1000).strftime('%m/%d/%Y %H:%M')
              channel = client.get_channel(818611323755036702)
              await channel.send(content = f"Games Resources Updated: {rt}")
            settings.GAMES_LAST_UPDATED = lu
