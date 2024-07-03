from events.base_event      import BaseEvent
import requests
import json
from datetime               import datetime, date
from math                   import floor
import discord
import settings
import os


# Your friendly example event
# You can name this class as you like, but make sure to set BaseEvent
# as the parent class

apiKey = os.getenv('APIKEY')


class ServerStats(BaseEvent):

    def __init__(self):
        interval_minutes = 10  # Set the interval for this event
        super().__init__(interval_minutes)

    # Override the run() method
    # It will be called once every {interval_minutes} minutes
    
    async def run(self, client):
        keydata = requests.get(f"https://api.hypixel.net/key?key={apiKey}")
        keydata1 = json.loads(keydata.text)
        membersChannel = client.get_channel(823683147996332052)
        usesChannel = client.get_channel(828031117042778192)
        
        # if keydata1["success"] == True:
        #   uses = "{:,}".format(keydata1["record"]["totalQueries"])
        # else:
        #   uses = "?"
        # await usesChannel.edit(name=f"{uses} bot uses")

        try:
          memberCount = "{:,}".format(membersChannel.guild.member_count)
        except:
          memberCount = "?"

        await membersChannel.edit(name=f"{memberCount} Discord Members")

        print("Updated Server Stats")
