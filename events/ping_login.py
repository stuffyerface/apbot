from events.base_event      import BaseEvent
import requests
import json
from datetime               import datetime, date
from math                   import floor
import discord
import settings


# Your friendly example event
# You can name this class as you like, but make sure to set BaseEvent
# as the parent class

class ResourceUpdate(BaseEvent):

    def __init__(self):
        interval_minutes = 15  # Set the interval for this event
        super().__init__(interval_minutes)

    # Override the run() method
    # It will be called once every {interval_minutes} minutes
    
    async def run(self, client):
        apres = requests.get("https://api.hypixel.net/status?key=84cf2f1e-5328-4ebc-ae60-c0d38cae5394&uuid=61e8ad9f-cda4-4bfb-acfe-71c9009e683d")
        achres = json.loads(apres.text)
        if achres["success"] == True:
          lu = achres["session"]["online"]
          if lu != settings.OUONLINE:
            if(lu):
              oustatus = "In"
            else:
              oustatus = "Out"
            channel = client.get_channel(818611323755036702)
            await channel.send(content = f"Player Logged {oustatus}")
            settings.OUONLINE = lu
