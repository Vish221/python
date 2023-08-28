# name="Vishvesh"
amount=2000
pin="1234"
flag=True
while(flag):
    print("Welcome to atm")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check your balance")
    print("4. Change Your pin")
    print("5. Exit")
    
    choice=int(input("Enter your choice: "))
    if(choice==1):
        print("Please enter your Pin")
        check_pin=input("")
        if(check_pin==pin):
            print("Enter the amount you want to deposit: ")
            deposit_amount=int(input())
            amount=amount+deposit_amount
            print("Amount deposited")
        else:
            print("Wrong PIn")    
    elif(choice==2):
        print("Please enter your Pin")
        check_pin=input("")
        if(check_pin==pin):
            print("Enter the amount you want to withdraw: ")
            Withdraw_amount=int(input())
            if(Withdraw_amount<amount):
                amount=amount-Withdraw_amount
                print("Amount Withdraw")
            else:
                print("Sorry you do not have enough amount")
            
    elif(choice==3):
        print("Please enter your Pin")
        check_pin=input("")
        if(check_pin==pin):
            print("Available Balance is",amount)
            
    elif(choice==4):
        print("Please enter previous Pin")
        check_pin=input("")
        if(check_pin==pin):
            pin=input("Please enter the new pin")
    elif(choice==5):
        flag=False