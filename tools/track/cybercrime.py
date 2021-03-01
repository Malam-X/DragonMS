from cybercrimetracker.cybercrimeTrackerAPI import cybercrimeTrackerAPI
import sys
import json
from etc.set import *

def main_track():
   query = ''
   if len(sys.argv) > 1:
      query = sys.argv[1]
   x = (json.dumps(cybercrimeTrackerAPI().search(query), indent=2))
   NAME_PATH = 'result/track_result.txt'
   with open(f'{NAME_PATH}', 'w') as f:
       f.write(x)
   print(f'{PULS} Success check /{NAME_PATH}')
