# Your PremiumUser class goes here
from User import User

class PremiumUser(User):
    def __init__(self, name, age, nationality, status = 'Premium'):
        super().__init__(name, age, nationality)
        self.status = status

    @property
    def get_status(self):
        return self.status