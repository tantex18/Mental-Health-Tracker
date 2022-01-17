import main

isloggedin = False

def logins(username,password):
    checking = open("username_password_database.txt",'r')
    username = username+"\n"
    password = password+"\n"
    done = False
    while(not done):
        line = checking.readline()
        if line == username:
            database_password = checking.readline()
            if (database_password == password):
                print("welcome! we are able to log you in")
                isloggedin = True
                done = True
                return True
            else:
                print("sorry your login credentials do not match out database")
                done = True
                return False
        if(line == ""):
            print("sorry, it appears your username does not exist in our database")
            done = True
            return False 
