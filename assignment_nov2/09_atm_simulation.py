balance = 1000.0

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Your current balance is:", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        else:
            balance = balance + amount
            print("Deposit successful. New balance:", balance)

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance = balance - amount
            print("Withdrawal successful. New balance:", balance)

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
