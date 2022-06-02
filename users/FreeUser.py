from users.User import User

class FreeUser(User):
    def __init__(self, name, age, nationality, status = 'Free'):
        super().__init__(name, age, nationality)
        self.status = status
    
    @property
    def get_status(self):
        return self.status

    def add_post(self, post_1, post_2):
        self.post_1 = post_1
        self.post_2 = post_2
        self.post.append(post_1)
        self.post.append(post_2)
    
