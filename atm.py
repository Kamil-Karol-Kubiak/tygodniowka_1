balance = 1000
option = 1

while option != 4:
    print("===== ATM =====")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    print()
    option = int(input("Choose an option: "))
    if option == 1:
        print()
        print("Current balance:", balance)
        print()
    elif option == 2:
        print()
        deposit = int(input("How much money you want to deposit? "))
        while deposit < 0:
            print()
            print("ERROR: You cannot deposit negative amount of money.")
            print()
            deposit = int(input("How much money you want to deposit? "))
        print()
        balance += deposit
    elif option == 3:
        print()
        withdraw = int(input("How much money you want to withdraw? "))
        while withdraw > balance or withdraw < 0:
            while withdraw > balance:
                print()
                print("ERROR: Not enough money on your account.")
                print()
                withdraw = int(input("How much money you want to withdraw? "))
            while withdraw < 0:
                print()
                print("ERROR: You cannot withdraw negative amount of money.")
                print()
                withdraw = int(input("How much money you want to withdraw? "))
        print()
        balance -= withdraw
    elif option == 4:
        print()
        print("Thank you! Goodbye.")
    else:
        print()
        print("ERROR: Wrong option.")
        print()
