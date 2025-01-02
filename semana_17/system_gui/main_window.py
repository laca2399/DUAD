import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import PySimpleGUI as sg
from system_gui.add_category import add_category_window
from system_gui.add_transaction import add_transaction_window
from system_logic.data import load_data, save_data


categories, transactions = load_data()  #To load the current data from the json file

data = [[transaction["name"], transaction["category"], transaction["type"], transaction["amount"]] for transaction in transactions]
#This is to extract the values for each key

headers = ["Name", "Category", "Type", "Amount"]  #Columns titles of the table

layout = [
    [sg.Table(values=data, headings=headers, auto_size_columns=True, justification='center', key="TABLE")],
    [sg.Button("Add Category"), sg.Button("Add Expense"), sg.Button("Add Income")],
    [sg.Button("Exit")]]


main_window = sg.Window("Financial Management System", layout)

while True: #Infinite loop until exit or X is pressed
    event, values = main_window.read()  #read the events that are in the window
    if event in (sg.WINDOW_CLOSED, "Exit"):  #When close or exit, to save the current data and finish
        save_data(categories, transactions)
        break
    elif event == "Add Category":  #When Add Category button is pressed
        new_category = add_category_window(categories)
        if new_category:
            categories.append(new_category)
            save_data(categories, transactions)
    elif event == "Add Expense":  #When Add Expense button is pressed
        if not categories:
            sg.popup_error("Please add at least one category before adding an expense.")
        else:
            new_transaction = add_transaction_window("Expense", categories)
            if new_transaction:
                transactions.append(new_transaction)
                data.append([new_transaction["name"], new_transaction["category"], new_transaction["type"], new_transaction["amount"]])
                main_window["TABLE"].update(values=data)
                save_data(categories, transactions)
    elif event == "Add Income":  #When Add Income button is pressed
        if not categories:
            sg.popup_error("Please add at least one category before adding an income.")
        else:
            new_transaction = add_transaction_window("Income", categories)
            if new_transaction:
                transactions.append(new_transaction)
                data.append([new_transaction["name"], new_transaction["category"], new_transaction["type"], new_transaction["amount"]])
                main_window["TABLE"].update(values=data)
                save_data(categories, transactions)


main_window.close()