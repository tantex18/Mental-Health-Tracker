import Userclass
users = []

def create_account():
   print("Hello there! welcome. what is your name?")
   name= input()
   print("Please enter you age")
   age= input()
   print("What is your location?")
   location= input()
   print("Enter an email address")
   email= input()
   print("create a username for your account")
   username= input()
   print("create a PASSWORD")
   password= input()
   newuser = Userclass.User(name,username,email,password,age,location)
   users.append(newuser)

def append_to_database(object):
   write = open("username_password_database.txt","a")
   write.write(object.username)
   write.write("\n")
   write.write(object.password)
   write.write("\n")
   write.close()

def append_all_info(object):
   write = open("user_database.txt","a")
   write.write("New User \n")
   write.write(object.name)
   write.write("\n")
   write.write(object.username)
   write.write("\n")
   write.write(object.email)
   write.write("\n")
   write.write(object.password)
   write.write("\n")
   write.write(object.age)
   write.write("\n")
   write.write(object.location)
   write.write("\n")
   write.close()
   