from cmd import PROMPT
from User import User

class FreeUser(User):
    def __init__(self, name, age, nationality, status = 'Free'):
        super().__init__(name, age, nationality)
        self.post = []
        self.status = status


    @property
    def get_status(self):
        return self.status

    def add_post(self, posted):
        self.posted = posted

        if len(self.post) < 2 :
            self.post.append(self.posted)
            print(len(self.post))
        elif len(self.post) == 2:
            print('No more posts')

    
fred = FreeUser("Fred", 23, "American")
print(fred)
fred.add_post('hi')
fred.get_post
fred.add_post('Bye')
fred.get_post
fred.add_post('rt')
