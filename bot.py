from instapy import InstaPy
from instapy import smart_run

class InstaBot:
    def __init__(self, username, password, targets = [], tags = [], like = False, comment = False, 
                        follow = False, unfollow = False, headless_browser = False, comments = [] ):
        self.username = username
        self.password = password
        self.targets = targets
        self.tags = tags
        self.like = like
        self.comment = comment
        self.follow = follow
        self.unfollow = unfollow
        self.headless_browser = headless_browser
        self.comments = comments
        
        self.setup()
        
    def setup(self):
        self.session = InstaPy(username = self.username,
                                password = self.password,
                                headless_browser = self.headless_browser)
                                
        self.session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments", "follows", "unfollows", "server_calls"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes=(57, 585),
                               peak_comments=(14, 150),
                                peak_follows=(70, 850),
                                 peak_unfollows=(70, 1000),
                                  peak_server_calls=(500, 4700))
                                  
        self.session.set_blacklist(enabled=True, campaign = self.username)
        
        self.session.set_relationship_bounds(enabled=True,
				    delimit_by_numbers=True,
				     min_followers=200,
				      min_following=250,
				       min_posts=20)

    def run(self):
        while(True):
            with smart_run(self.session):
                if self.like: 
                    self.session.like_by_tags(self.tags, amount=15)
                if self.comment:
                    self.session.set_do_comment(enabled=True, percentage=25)
                    self.session.set_comments(self.comments)
                if self.follow:
                    self.session.follow_user_followers(self.targets, amount=15, randomize=True)
                if self.unfollow:
                    self.session.unfollow_users(amount=15, nonFollowers=True, unfollow_after=72*60*60, sleep_delay=655)

                
                
