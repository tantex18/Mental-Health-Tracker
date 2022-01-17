import notifications
paysub=[]
def payments():
    subscription=False
    while(paysub==False):
        if("pay"==paysub):
          print("please enter ypur payment method")
          payment_method= input()
        if("credit/debitcard"==paysub):
            print("please enter your card details")
            details=input()
            subscription=True
            return paysub