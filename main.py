# imports
import os
from bot import InstaBot
from quota_profiles import trusted_mid
from ig_profiles import buddhaland_

while True:
    instaBot = InstaBot(buddhaland_.username, 
                        buddhaland_.password, 
                        buddhaland_.targets, 
                        buddhaland_.tags, 
                        like = False, comment = True, follow = True, unfollow = True,
                        headless_browser = True, comments = comments, quota_profile = trusted_mid)

    instaBot.run()