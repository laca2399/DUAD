import pytest
import json
import os
from system_logic.data import load_data

#File for test
@pytest.fixture
def temp_file():
    #Arrange
    file_path = "test_finances.json"
    
    data = {
        "categories": ["Food", "Transport"],
        "transactions": [{"name": "Groceries", "amount": 50.85, "category": "Food", "type": "Expense"}]
    }
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    
    yield file_path
    
    
    os.remove(file_path)

def test_load_data(temp_file):
    
    #Act
    categories, transactions = load_data()
    
    #Assert
    #Verify loaded data is correct
    assert categories == ["Food", "Transport"]
    assert transactions == [{"name": "Groceries", "amount": 50.85, "category": "Food", "type": "Expense"}]



