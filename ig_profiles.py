
#imports
import os
from bot import InstaBot
from targets import buddhaland_targets, matchalovers_targets, ligiapiresco_targets
from tags import buddhaland_tags, matchalovers_tags, ligiapiresco_tags
from quota_profiles import trusted_mid, fresh_mid
from rel_bounds import ligiapiresco_rel_bounds, buddhaland_rel_bounds
from comments import buddhaland_comments

class InstagramProfile:
    def __init__(self, username, password, targets, tags, comments,
                like = False, comment = False, follow = False, unfollow = False,
                headless_browser = True, quota_profile = {}, rel_bounds = {}):
        self.username = username
        self.password = password
        self.targets = targets
        self.tags = tags
        self.comments = comments
        self.like = like
        self.comment = comment
        self.follow = follow
        self.unfollow = unfollow
        self.headless_browser = headless_browser
        self.quota_profile = quota_profile
        self.rel_bounds = rel_bounds
        
    def get_bot_profile(self):
        return InstaBot(self.username, 
                        self.password, 
                        self.targets, 
                        self.tags, 
                        self.like, self.comment, self.follow, self.unfollow,
                        self.headless_browser, self.comments, self.quota_profile, 
                        self.rel_bounds)
        
comments = []
        
        
buddhaland_ = InstagramProfile('buddhaland_', os.environ['buddhaland_pass'], buddhaland_targets, buddhaland_tags, buddhaland_comments,
                                like = True, comment = False, follow = True, unfollow = True, headless_browser = True, 
                                quota_profile = trusted_mid, rel_bounds = buddhaland_rel_bounds)
                                
matchalovers = InstagramProfile('__matchalovers__', os.environ['matchalovers_pass'], matchalovers_targets, matchalovers_tags, comments)
ligiapiresco = InstagramProfile('ligiapiresco', os.environ['ligiapiresco_pass'], ligiapiresco_targets, ligiapiresco_tags, comments,
                                like = True, comment = False, follow = True, unfollow = True, headless_browser = True, 
                                quota_profile = fresh_mid, rel_bounds = ligiapiresco_rel_bounds)