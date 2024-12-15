import pytest
from system_gui.add_category import add_category_window  

def test_add_category_window():

    #Arrange
    categories = ["Food", "Transport"]

    #Act
    new_category = add_category_window(categories)

    #Assert
    assert new_category == "Entertainment"  #We try with Entertainment
    assert new_category not in categories  # Category must not repeat

    #we try an empty category
    new_category = add_category_window(categories)
    assert new_category is None 

