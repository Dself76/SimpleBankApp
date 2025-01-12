

balance = 0.0

def show_balance():
    # Access the global variable
    # Use 'global' to access and update the 'count' variable from within a function, reflecting changes globally. just me getting used to using the global. 

    global balance
    print(f"Your balance as of today is ${balance:.2f}")

def deposit():
    amount = float(input("Enter your deposit amount: "))
    if amount < 0:
        print('Not a valid amount')
        return 0
    else:
        return amount

def withdrawl():
    # Access the global variable
    global balance
    amount = float(input("Amount you would like to withdraw?"))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be more than 0")
        return 0
    else:
        return amount

def main():
    # Use the global balance declared outside main
    global balance
    is_running = True

    while is_running:
        print("Bank App")
        print("1. Show my Balance")
        print('2. Deposit')
        print ("3. Withdrawl")
        print('4. Exit')

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance()
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdrawl()
        elif choice == '4':
            is_running = False
        else:
            print("Not a valid choice")

    print("Thank you for trying my custom bank app")

if __name__ =='__main__':
    main()
