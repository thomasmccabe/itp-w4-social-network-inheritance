
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []

    def add_post(self, post):
        post.set_user(self)

    def get_timeline(self):
        timeline = []
        for people_being_followed in self.following:
            for post in people_being_followed.posts:
                timeline.append(post)
                timeline.sort(key=lambda r: r.timestamp)    
        return timeline


    def follow(self, other):
        self.following.append(other)
