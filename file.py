import Userclass
import login
import signup
import payandsubscription
import page_you_see_when_you_log_in


print("Welcome to our Mental Health Tracker App")
print("If you already have an account with us, type yes. If you don't have an account, type no")
response = input()
if response == "yes":
    print("Great, enter your username please")
    user = input()
    print("welcome",user,"please enter your password")
    password = input()
    success = login.verify_login(user,password)
    if success == True:
        print("Welcome, you may continue to the Main Page")
    else:
        print("Your username and/or password are incorrect, maybe try creatting your account first")
elif response == "no":
    done = False
    count = 0
    accountdatabase = []
    paymnetdetails = []
    paymentfile = open("payment.txt","a")
    databasefile = open("databasefile.txt","a")
    print("Do you want to create an account with us")
    answer = input()
    if answer == "yes":
        accountdatabase.append(signup.signupfunc())
        print("Congrats, you now have an account with us")
        print("your username is", accountdatabase[count].username)
        databasefile.write(accountdatabase[count].username)
        databasefile.write("\n")
        databasefile.write(accountdatabase[count].password)
        databasefile.write("\n")
        print("I see you live at;", accountdatabase[count].location)
        print("please enter your payment details")
        
        

    else:
        print("Ok, bye")
        done = True
    count = count + 1
    databasefile.close()

