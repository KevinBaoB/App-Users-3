# Import and create your users here
from users.User import User
from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser

kevin = User("Kevin", 24, "American")
linda = FreeUser('Linda', 26, 'American')
sandy = PremiumUser('Sandy', 22, 'American')

print(kevin)
print(linda)
print(sandy)

kevin.add_post("I made a post")
kevin.add_post('Another post')
print(kevin.post)

linda.add_post('I made one too', 'Here\'s another')
print(linda.post)

sandy.add_post('I made a post')
print(sandy.post)
        
print(sandy.get_status)
print(linda.get_status)
