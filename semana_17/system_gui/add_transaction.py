import PySimpleGUI as sg

def add_transaction_window(transaction_type, categories):
    title = f"Add {transaction_type}"  #used to create like a dynamic title

    layout = [[sg.Text(f"Enter the name of the {transaction_type.lower()}")],
            [sg.Input(key = "TRANSACTION_NAME")],
            [sg.Text(f"Enter the amount of the {transaction_type.lower()}")],
            [sg.Input(key="TRANSACTION_AMOUNT")],
            [sg.Text("Select a Category")],
            [sg.Combo(values=categories, key="TRANSACTION_CATEGORY", readonly=True)],
            [sg.Button("Confirm"), sg.Button("Cancel")]]

    transaction_window = sg.Window(f"Add {transaction_type}", layout)

    while True:
        event, values = transaction_window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            transaction_window.close()
            return None
        elif event == "Confirm":
            transaction_name = values["TRANSACTION_NAME"].strip()

            if not transaction_name:
                sg.popup_error(f"{transaction_type} name cannot be empty, please enter a valid name")
                continue


            try:
                transaction_amount = float(values["TRANSACTION_AMOUNT"])
                if transaction_amount <= 0:
                    sg.popup_error("Amount must be greater than 0")
                    continue
            except ValueError:
                sg.popup_error("Amount must be a number.")
                continue

            transaction_category = values["TRANSACTION_CATEGORY"]
            if not transaction_category:
                sg.popup_error("Please select a category")
                continue

            transaction = {
                "name": transaction_name,
                "amount": transaction_amount,
                "category": transaction_category,
                "type": transaction_type
            }

            sg.popup(f"{transaction_type} added: {transaction}")
            transaction_window.close()
            return transaction


