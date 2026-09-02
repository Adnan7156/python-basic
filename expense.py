balance = 0

while balance == 0:
    print("Initial balance is 0")
    income1 = input("You want to add income ? yes or no: ")

    if income1 == "no":
        print("Current balance is", balance)

    else:
        while True:
            change_type = input("Enter the change type expense or income or exit: ")
            print("change type is", change_type)

            if change_type == "exit":
                break

            if change_type not in ("expense", "income"):
                print(
                    "Invalid change type. Please enter 'expense', 'income', or 'exit'.😊"
                )
                continue

            taka = float(input("Enter the amount of change: "))
            print("amount of change is", taka)

            if change_type == "expense":
                balance -= taka
            else:
                balance += taka

            print("Current balance is", balance)
