from events.base_event      import BaseEvent
import requests
import json
from datetime               import datetime, date
from math                   import floor
import discord
import staff
import utils
import os


# Your friendly example event
# You can name this class as you like, but make sure to set BaseEvent
# as the parent class

class OnlineCheck(BaseEvent):

    def __init__(self):
        interval_minutes = 2  # Set the interval for this event
        super().__init__(interval_minutes)

    # Override the run() method
    # It will be called once every {interval_minutes} minutes

    async def run(self, client):
       #("name","uuid","rank")
      stafflist = staff.ONLINE_LIST
      apiKey = os.getenv('APIKEY')
      # Need to parse the staff list, checking
      # if each staff has the same username and 
      # rank. If not, send that information to
      # print.
      for x in range(len(stafflist)):
        #print(x)
        info = requests.get(f"https://api.hypixel.net/skyblock/profiles?uuid={stafflist[x][0]}&key={apiKey}")
        info = json.loads(info.text)
        if(info["success"] == False):
          print(f"Failed to get info for player {stafflist[x][1]}")
          return
        if stafflist[x][2] == "{}":
          staff.ONLINE_LIST[x][2] = info
          print(f"Initialized info for player {stafflist[x][1]}")
          return
        channel = client.get_channel(953396331832021114)
        if stafflist[x][2] != info and stafflist[x][4] == False:
          print(f"{stafflist[x][1]} is active")
          await channel.send(content = f"<@!108359975536992256> {stafflist[x][1]} is active")
          staff.ONLINE_LIST[x][3] = 0
          staff.ONLINE_LIST[x][2] = info
          staff.ONLINE_LIST[x][4] = True
        else:
          #print(f"Updated info for player {stafflist[x][1]}")
          if(stafflist[x][4]):
            if stafflist[x][3] == 2:
              print(f"{stafflist[x][1]} is inactive")
              await channel.send(content = f"{stafflist[x][1]} is inactive")
              staff.ONLINE_LIST[x][3] = 0
              staff.ONLINE_LIST[x][4] = False
            if stafflist[x][3] <2:
              staff.ONLINE_LIST[x][3] = stafflist[x][3]+1
