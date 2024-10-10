
#question 4

#WITI Academy is proposing a sacco to help students save their money.
#Design a platform that do the following.
#welcome to WITI Academy Sacco
# 1 Deposit money
# 2 withdraw money
# 3 check balance
# Ensure if the student select 1,money is deposited and the minimum deposit should be 1000.
#if the student selects 2 ,money should be withdrawnand a minimum withdrawal is 500.
# if the student selects 3,the account balance should be displayed 

#Answer

def saccoTransactions():
    accountBalance=0
    run=1
    while run==1:
        print("\Welcometi,WITI ACADEMY SACCO.")

        #MENU
        print("1.Deposite Money")
        print("2.Withdraw Money")
        print("3.Check Balance")

        studentchoice=int(input("Enter your selection(1,2 or 3): "))

 #perform transactions basing on the student  selection


    if studentchoice==1:
        print("\n...processing a deposit transaction...")

        depositAmount= int(input("Enter the amount to be deposited:" ))
        if depositAmount<1000:
            print("\nminimum deposit is 1000")
        else:
            accountBalance+= depositAmount
            print(f"Dear student,you have deposited {depositAmount:,} and  your new accountbalance is{accountBalance:,}")

    elif studentchoice==2:
        print("\n...processing a withdraw transaction...")

        withdrawAmount= int(input("Enter the amount to be withdrawn:" ))
    if withdrawAmount <500:
        print("minimum withdraw amount is 500")

    elif withdrawAmount>accountBalance:
        print(f"withdraw failed,insufficient funds")
    elif:
        accountBalance = accountBalance - withdrawAmount
        
            
        print(f"Dear student,you have withdrawn {withdrawAmount:,} and  your new accountbalance is{accountBalance:,}")

    elif studentchoice==3:
         print(f"Your account balance is {accountBalance:,}")


    else:
        print("You entered a wrong choice!! please select 1,2 or 3\n")

        run = int(input("Enter one to continue or any number to exit: "))

    if run!=1:
        print("Thanks for using our sacco")
        
    















