if __name__ == "__main__":
    atm = ATM()

    while True:
        print("\nATM Simulator")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter the deposit amount: "))
            print(atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: "))
            print(atm.withdraw(amount))
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
