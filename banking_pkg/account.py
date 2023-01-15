def show_balance(balance):
    print("You have the balance of: ", float(balance))


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return (float(balance)) + (float(amount))


def withdraw(balance):
    amount = input("Enter amount to withdraw")
    return (float(amount)) - (float(balance))


def logout(name):
    print("Goodbye", name)
