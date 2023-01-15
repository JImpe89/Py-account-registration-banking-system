from banking_pkg import account

print("          === Automated Teller Machine ===          ")
print("LOGIN")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = str("$0")
print(name, "has registered with a starting balance of", balance, "\n")

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_validate = input("Enter name: ")
    pin_validate = input("Enter Pin: ")

    if name == name_validate and pin == pin_validate:
        print("Login successful!")
        break
    else:
        print("Invalid Credentials")
        continue

while True:

    def atm_menu(name):
        print("")
        print("          === Automated Teller Machine ===          ")
        print("User: " + name)
        print("------------------------------------------")
        print("| 1.    Balance     | 2.    Deposit      |")
        print("------------------------------------------")
        print("------------------------------------------")
        print("| 3.    Withdraw    | 4.    Logout       |")
        print("------------------------------------------")
    atm_menu(name)
    option = input("Choose an option: ")
    balance = 100
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    else:
        if option == "4":
            account.logout(name)
            break
