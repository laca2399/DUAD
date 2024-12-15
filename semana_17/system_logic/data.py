import PySimpleGUI as sg
import json

def load_data():
    try:
        with open('finances.json', 'r') as file:
            data = json.load(file)
            return data['categories'], data['transactions']
    except FileNotFoundError:
        return [], []


def save_data(categories, transactions):
    
    data = {
        "categories": categories,
        "transactions": transactions
    }
    
    with open('finances.json', 'w') as file:
        json.dump(data, file, indent=4)


