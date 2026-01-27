MAX_LINES = 3
def get_deposit():
    while True:
        amount = input("How much you want to deposit ?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Desposit must be greater than zero.")
        else:
            print("Please enter a valid amount.")
    return amount

def get_No_of_Lines():
    while True:
        lines = input(f"How many lines would you like to bet on (1-{MAX_LINES})?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines must be within limit.")
        else:
            print("Please enter a valid number.")
    return lines 

def main():
    balance = get_deposit()
    line = get_No_of_Lines()
    print(balance,line)

main()