class User:

    def __init__(self,name,username,email,password,age,location):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.age = age
        self.location = location

    def __str__(self) -> str:
        print("my name is ",self.name)
        
    def coolguy(self):
        print("I am cool")


