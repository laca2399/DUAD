import pytest
from system_gui.add_transaction import add_transaction_window  

def test_add_transaction_window():
    #Arrange------------------------------------------>
    categories = ["Food", "Transport"]

    #We try with expense
    transaction_type = "Expense"

    #Act----------------------------------------------------->
    new_transaction = add_transaction_window(transaction_type, categories)

    #Assert----------------------------------------------------->
    # We verified if it adds correctly the transaction
    assert new_transaction is not None
    assert new_transaction["name"] == "Groceries" 
    assert new_transaction["amount"] == 50.85  
    assert new_transaction["category"] == "Food"  
    assert new_transaction["type"] == "Expense"  

    new_transaction = add_transaction_window(transaction_type, categories)
    assert new_transaction is None

    #Try an invalid number
    new_transaction = add_transaction_window(transaction_type, categories)
    assert new_transaction is None  
