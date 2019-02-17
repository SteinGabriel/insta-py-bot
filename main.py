# imports
import os
import sys
from ig_profiles import buddhaland_, matchalovers, ligiapiresco, _steinjack

def create_bot_profile():
    if len(sys.argv) == 1:
        print('Error ==> Missing profile argument.')
        quit()
    
    ig_profile = sys.argv[1]
    
    if ig_profile == 'buddhaland_':
        return buddhaland_.get_bot_profile()
    if ig_profile == 'ligiapiresco':
        return ligiapiresco.get_bot_profile()
    if ig_profile == 'matchalovers':
        return matchalovers.get_bot_profile()
    if ig_profile == '_steinjack':
        return _steinjack.get_bot_profile()
        
while True:
    instaBot = create_bot_profile()
    instaBot.run()