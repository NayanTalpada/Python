# Function to handle debit transactions
def debit(balance):
    money = int(input("Enter Money U want to debit: "))
    balance -= money
    print(f"Total Rupee u have = {balance}")
    return balance
# Function to handle credit transactions
def credit(balance):
    money = int(input("Enter Money U want to credit: "))
    balance += money
    print(f"Total Rupee u have = {balance}")
    return balance

# Main account selection logic
def account():
    # Convert input to int so we can do math
    balance = int(input("Enter Your Balance: "))
    click = input("Which one? (1 for debit or 2 for credit): ")

    if click == "1":
        balance = debit(balance)
    elif click == "2":
        balance = credit(balance)
    else:
        print("Invalid selection.")
account()
