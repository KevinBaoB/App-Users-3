# Your User class goes here
class User:

    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.post = []
    

    def __str__(self):
        return f"My name is {self.name}, I'm {self.age} years old and I am {self.nationality}!"
    
    @property
    def get_post(self):

        print('Getting Past Posts: ')
        return self.post
    
    # @get_post.setter
    def add_post(self, str):
        
        self.str = str
        self.post.append(str)

    def delete_post(self, index):
        self.index = index -1
        print(f"Deleting post number: {self.index + 1} ")
        del self.str
        self.post.pop(int(self.index))


# kevin = User("Kevin", 24, "American")