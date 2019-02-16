class RelBounds:
    def __init__(self, enabled, delimit_by_numbers, min_followers, max_followers, min_following, min_posts):
        self.enabled = enabled
        self.delimit_by_numbers = delimit_by_numbers
        self.min_followers = min_followers
        self.max_followers = max_followers
        self.min_following = min_following
        self.min_following = min_following
        self.min_posts = min_posts
        
    
    
ligiapiresco_rel_bounds = RelBounds(True, True, 200, 8000, 100, 30)
buddhaland_rel_bounds = RelBounds(True, True, 120, 3000, 150, 15)
