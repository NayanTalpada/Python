#debit credit 
def debit(balance):
        money=int(input("Enter Money U want to debit:"))#10,000
        balance=balance-money
        print("Total Ruppe u have=",balance)
def credit(balance):
        money=int(input("Enter Money U want to credit:"))#10,000
        balance=balance+money
        print("Total Ruppe u have=",balance)
def account():
    balance=int(input("Enter Your Balance:"))
    click=input("Which one 1.debit or 2.credit:-")
    if (click=="1"):
        balance = debit(balance)
    elif (click=="2"):
        balance = credit(balance)
    else:
        print("Invalid choice")
account()
