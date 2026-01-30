import random
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3
symbol_count = {
    'A': 3,
    'B': 5,
    'C': 6,
    'D': 8
}
symbol_value = {
    'A': 15,
    'B': 12,
    'C': 8,
    'D': 5
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line + 1)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i != len(columns)-1 :
                print(column[row],end ="|")
            else:
                print(column[row])

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

def get_bet():
    while True:
        amount = input("What would you like to bet on each line?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please choose an amount between Rs.{MIN_BET} and Rs.{MAX_BET}!")
        else:
            print("Please enter a valid number.")
    return amount

def spin(balance):
    while True:
        lines = get_No_of_Lines()
        bet = get_bet()
        total_bet = lines*bet
        if total_bet > balance:
            print("You DON'T have enough balance to play this bet!")
        else:
            break
    print(f"You are betting total of Rs.{total_bet} with Rs.{bet} on each of {lines} lines.")
    slots = get_slot_machine_spin(ROWS,COLS, symbol_count)
    print_slot_machine(slots)
    winnings , winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won Rs.{winnings} .")
    print(f"You won on lines:" , *winning_lines)
    return winnings-total_bet



def main():
    balance = get_deposit()
    while True:
        print(f"Current balance is Rs.{balance}")
        answer = input("Press enter to play(q to quit game).")
        if answer == 'q':
            break
        balance += spin(balance)
    print(f"You left with Rs.{balance} .")

main()