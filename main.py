# imports
import os
from bot import InstaBot

username = 'buddhaland_' 
password = os.environ['buddhaland_pass'] 
targets = ['buddhism__', 'buddhaquotes_', 'buddhist_poetry']
tags = ['buddha', 'enlightenment', 'buddhism', 'meditation', 'yoga'] 
comments = [u'Amazing page 😍😍 Check my page too! ', u'Thank you for sharing! 🙏 Take a look at my account :)']

instaBot = InstaBot(username, 
                    password, 
                    targets, 
                    tags, 
                    like = True, comment = True, follow = True, unfollow = True,
                    headless_browser = True, comments = comments)

instaBot.run()