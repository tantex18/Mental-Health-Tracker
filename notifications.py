import time 
notify=[]
def reminder():
    notifynow=False
    while(notifynow==False):
        if("medicationtime"==notifynow):
          print("please take your medication,progress begins with you")
        if("sessiontime"==notifynow):
            print("please attend your session to pave your healing journey!")
            notifynow=True
            return notify
        

