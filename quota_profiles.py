class QuotaProfile:
    def __init__(self, peak_likes = [], peak_comments = [], peak_follows = [], peak_unfollows = [], peak_server_calls = []):
        self.peak_likes = peak_likes
        self.peak_comments = peak_comments
        self.peak_follows = peak_follows
        self.peak_unfollows = peak_unfollows
        self.peak_server_calls = peak_server_calls

trusted_mid = QuotaProfile(
    peak_likes= [57, 585],
    peak_comments = [15, 150],
    peak_follows =  [70, 850],
    peak_unfollows = [100, 1000],
    peak_server_calls = [700, 4700],
)

fresh_mid = QuotaProfile(
    peak_likes= [57, 500],
    peak_comments = [15, 150],
    peak_follows =  [70, 500],
    peak_unfollows = [100, 500],
    peak_server_calls = [700, 4700],
)