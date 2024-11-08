#Create a dictnary 
account = {1010:[123,5000],2020 :[1234,6000],3030:[None,1000]}
#Write a Withdraw function 
def withdraw():
    #Enter the Account number 
    accno = int(input("Enter the Account Number : "))
    #Verify the account number they are not in the dictnary
    if accno in account:
        #Enter the pin number
        pin = int(input("Enter the pin: "))
        #internaly to check the pin corrent or not
        if account[accno][0]==pin:
            #After the enter the Withdraw amount
            amt = int(input("Enter you Withdraw amount :"))
            #it will check the amount avalible or not 
            if account[accno][1] >=amt:
                account[accno][1] -= amt
                print("Withdraw Sucessfull")
                print("*"*50)
                print(account[accno][0],"Remaing Balance is :",account[accno][1])
                print("*"*50)
            else:
                print("*"*50)
                print("Insufficent balance")
                print("*"*50)
        else:
            print("*"*50)
            print("Invalide pin Number !..")
            print("*"*50)
    else:
        print("*"*50)
        print("Account does not exit..")
        print("*"*50)
#Create a Deposit function
def Deposit():
    accno = int(input("Enter the account number : "))
    if accno in account:
        pin = int(input("Enter the pin number : "))
        if account[accno][0]==pin:
            amt = int(input("Enter the deposit amount: "))
            account[accno][1] +=amt
            print("Deposit amount Sucessfull...")
            print("*"*50)
            print(f"Update Balance : Rs.{account[accno][1]}")
            print("*"*50)
        else:
            print("*"*50)
            print("Invalide pin number !... ")
            print("*"*50)
    else:
        print("*"*50)
        print("Account does not exit..")
        print("*"*50)
#Create a Check Balance Function
def Check_Balance():
    accno = int(input("Enter the account number : "))
    if accno in account:
        pin = int(input("Enter your pin :"))
        if account[accno][0] == pin:
            print("*"*50)
            print(f"Balance : {account[accno][1]}")
            print("*"*50)
        else:
            print("*"*50)
            print("Invalide pin Number !...")
            print("*"*50)
    else:
        print("*"*50)
        print("Account does not exit..")
        print("*"*50)
#Create a Pin_Generation Function
def Pin_Generation():
    accno = int(input("Enter the Account Number : "))
    if accno in account:
        if account[accno][0] is None:
            pin1 = input("Enter the 4 digit pin ")
            if len(pin1) == 4:
                pin2 = input("Re-enter 4 digit pin :")
                if pin1 == pin2:
                    account[accno][0] = int(pin1)
                    print("pin Generation Sucessfully ")
                    print("*"*50)
                else:
                    print("*"*50)
                    print("Confirmation Unsuessfully !")
                    print("*"*50)
            else:
                print("*"*50)
                print("Please enter 4 digit number !")
                print("*"*50)
        else:
            print("*"*50)
            print("Pin Already Generated !...")
            print("*"*50)
    else:
        print("*"*50)
        print("Account does not exit..")
        print("*"*50)

#We useing a while loop
while True:
    print("Choose Requred option :")
    print("1.Withdraw")
    print("2.Deposit")
    print("3.Check Balance")
    print("4.Pin Generation")
    print("5.Exit")
    try:
        x=int(input("Enter Option Number :"))
    except:
        print("*"*50)
        print("Choose the corrent opetion !....")
        print("*"*50)
    else:
        if x == 1:
            print("====Withdrowal===")
            withdraw()
        elif x == 2:
            print("====Deposit====")
            Deposit()
        elif x == 3:
            print("====Check Balance====")
            Check_Balance()
        elif x == 4:
            print("====Pin Generation====")
            Pin_Generation()
        elif x == 5:
            break
        else:
            print("*"*50)
            print("Choose the corrent option!...")
            print("*"*50)