import json
import pytest
from system_logic.data import save_data  

temp_file = 'test_finances.json'  #temporal file test

def test_save_data():
    #Arrange-------------------------------->
    #Test data
    categories = ["Food", "Transport"]
    transactions = [{"name": "Groceries", "amount": 50.85, "category": "Food", "type": "Expense"}]

    #Act------------------------------------->
    #Save data in temporary file
    save_data(categories, transactions, temp_file)

    #Verify if data saved correctly
    with open(temp_file, 'r') as f:
        data = json.load(f)

    #Assert------------------------------------->
    #Verify data match
    assert data["categories"] == categories
    assert data["transactions"] == transactions

    #Arrange------------------------------------->
    #Adds new
    categories.append("Salary")
    transactions.append({
        "name": "Salary Payment",
        "amount": 1500,
        "category": "Salary",
        "type": "Income"
    })

    #Act------------------------------------->
    #Save again
    save_data(categories, transactions, temp_file)

    with open(temp_file, 'r') as f:
        data = json.load(f)

    #Assert----------------------------------------->
    #Verify category added correctly
    assert "Salary" in data["categories"]
    assert len(data["transactions"]) == 2  # Verify that transaction added
