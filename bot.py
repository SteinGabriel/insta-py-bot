from instapy import InstaPy
from instapy import smart_run

class InstaBot:
    def __init__(self, username, password, targets = [], tags = [], like = False, comment = False,
                        follow = False, unfollow = False, headless_browser = False, comments = [], quota_profile = {} ):
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
        self.quota_profile = quota_profile
        self.setup()

    def setup(self):

        self.session = InstaPy(username = self.username,
                                password = self.password,
                                headless_browser = self.headless_browser)

        self.session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments", "follows", "unfollows", "server_calls"],
                            sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes=(self.quota_profile.peak_likes),
                               peak_comments=(self.quota_profile.peak_comments),
                                peak_follows=(self.quota_profile.peak_follows),
                                 peak_unfollows=(self.quota_profile.peak_unfollows),
                                  peak_server_calls=(self.quota_profile.peak_server_calls))

        self.session.set_blacklist(enabled=True, campaign = self.username)
        self.session.set_relationship_bounds(enabled=True,
				    delimit_by_numbers=True,
				     min_followers=120,
				     max_followers=3000,
				      min_following=150,
				       min_posts=15)

    def run(self):
        with smart_run(self.session):
            if self.like:
                self.session.like_by_tags(self.tags, amount=15)
            if self.comment:
                self.session.set_comments(self.comments)
                self.session.set_do_comment(enabled=True, percentage=25)
                self.session.interact_user_followers(self.targets, amount=30, randomize=True)
            if self.follow:
                self.session.follow_user_followers(self.targets, amount=30, randomize=True)
            if self.unfollow:
                self.session.unfollow_users(amount=45, nonFollowers=True, unfollow_after=72*60*60, sleep_delay=350)



