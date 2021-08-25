name='Shahab Mustafa'
age=19
balance=0
print("Name",name)
print("Your Account BAlance:",balance)

def deposit(deposit_amount,balance):
    new_balance=deposit_amount + balance
    return new_balance


# Bank Account
    
deposit_amount=int(input("How  mush do you want to deposit:"))

balance=deposit(deposit_amount,balance)
print("the new balance:", balance)


def withdraw(w_amount,balance):
    if balance<w_amount:
        print("the withdraw is not avalible")
        return balance
    else:
        new_balance=balance-w_amount
        return new_balance
    
w_amount=int(input("How mush do you want to withdraw:"))

balance=withdraw(w_amount,balance)
print("the new balance:", balance)

