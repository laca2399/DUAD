import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'ejercicios')))

from ej1_bubblesort import bubble_sort
from my_exercises_week6 import sum_nums, turn_around_string, count_mayus_minus, sort_words, is_prime, filter_pri


#Tests de bubble sort
def test_bubblesort_with_small_list():
    print("Running test_bubblesort_with_small_list")
    # Arrange
    list_input = [6, 3, 2]
    # Act
    result = bubble_sort(list_input)
    # Assert
    assert result == sorted(list_input)

def test_bubblesort_with_list_more_than_100_elements():
    print("Running test_bubblesort_with_list_more_than_100_elements")
    # Arrange
    list_input = [104, 52, 87, 32, 90, 12, 55, 67, 98, 44, 33, 59, 74, 61, 20, 8, 4, 56, 109, 45, 
                88, 67, 65, 42, 99, 50, 73, 33, 10, 56, 19, 91, 55, 89, 100, 27, 60, 64, 13, 11, 18, 39, 
                96, 29, 37, 48, 84, 9, 23, 84, 16, 30, 70, 46, 58, 23, 41, 66, 56, 11, 32, 44, 61, 19, 
                85, 47, 17, 5, 1, 68, 38, 59, 29, 98, 26, 55, 94, 72, 40, 39, 75, 91, 20, 97, 61, 50, 
                25, 53, 78, 76, 51, 36, 79, 22, 52, 31, 98, 63, 65, 50, 33, 49, 69, 28, 49, 14, 53, 72, 
                85, 37, 74, 80, 48, 27, 64, 71, 5, 59, 60, 45, 49, 77, 62, 41, 82, 28, 83, 69, 56, 13, 54, 1002, 1010]
    # Act
    result = bubble_sort(list_input)
    # Assert
    assert result == sorted(list_input)

def test_bubblesort_with_empty_list():
    print("Running test_bubblesort_with_empty_list")
    # Arrange
    list_input = []
    # Act
    result = bubble_sort(list_input)
    # Assert
    assert result == sorted(list_input)

def test_bubblesort_with_non_list_parameters():
    print("Running test_bubblesort_with_non_list_parameters")
    # Arrange
    list_input = "Hola"
    # Act & Assert
    with pytest.raises(ValueError):
        bubble_sort(list_input)

#Tests de week6 exercise 3
def test_sum_nums_with_small_list ():
    #Arrange
    list_input = [2,3,4]
    #Act
    result = sum_nums(list_input)
    #Assert
    assert result == 9

def test_sum_nums_with_big_and_floats_list ():
    #Arrange
    list_input = [5.5,10,20,8,9,30.7,12,8,8,7.8,5,2,4]
    #Act
    result = sum_nums(list_input)
    #Assert
    assert result == 130

def test_sum_nums_with_negative_list ():
    #Arrange
    list_input = [-2,-3,-4]
    #Act
    result = sum_nums(list_input)
    #Assert
    assert result == -9

#Tests de week6 exercise 4
def test_turn_around_string_with_one_word_only():
    #Arrange
    param = "Hello"
    #Act
    result = turn_around_string(param)
    #Assert
    assert result == "olleH"

def test_turn_around_string_with_a_sentence():
    #Arrange
    param = "Hello my name is Andres and I'm 25 years old."
    #Act
    result = turn_around_string(param)
    #Assert
    assert result == ".dlo sraey 52 m'I dna serdnA si eman ym olleH"

def test_turn_around_string_with_special_characters():
    #Arrange
    param = "#$%&="
    #Act
    result = turn_around_string(param)
    #Assert
    assert result == "=&%$#"

#Tests de week6 exercise 5
def test_count_mayus_minus_with_only_capital_letters():
    #Arrange
    string = "ABCDEF"
    #Act
    result = count_mayus_minus(string)
    #Assert
    assert result == (6, 0)

def test_count_mayus_minus_with_only_lower_letters():
    #Arrange
    string = "abcdef"
    #Act
    result = count_mayus_minus(string)
    #Assert
    assert result == (0, 6)

def test_count_mayus_minus_with_mixed_letters():
    #Arrange
    string = "AbCdeF"
    #Act
    result = count_mayus_minus(string)
    #Assert
    assert result == (3, 3)

#Tests de week6 exercise 6
def test_sort_words_with_capital_and_lower_start():
    #Arrange
    string = "table-Chair-pencil-Ring"
    #Act
    result = sort_words(string)
    #Assert
    assert result == "Chair-Ring-pencil-table"

def test_sort_words_with_duplicate_words():
    #Arrange
    string = "table-Chair-pencil-table-Chair"
    #Act
    result = sort_words(string)
    #Assert
    assert result == "Chair-Chair-pencil-table-table"

def test_sort_words_with_only_lower_start():
    #Arrange
    string = "table-chair-pencil-ring"
    #Act
    result = sort_words(string)
    #Assert
    assert result == "chair-pencil-ring-table"

#Tests de week6 exercise 7
def test_is_prime_and_filter_prime_with_a_mixed_list_of_numbers():
    #Arrange
    input_list = [1,2,4,5,7,9,11,12]
    #Act
    result = filter_pri(input_list)
    #Assert
    assert result == [2,5,7,11]

def test_is_prime_and_filter_prime_with_no_prime_numbers():
    #Arrange
    input_list = [1,4,9,12]
    #Act
    result = filter_pri(input_list)
    #Assert
    assert result == []

def test_is_prime_and_filter_prime_with_a_mixed_list_including_negative_of_numbers():
    #Arrange
    input_list = [-2,-5,-7,2,5,7,11,12]
    #Act
    result = filter_pri(input_list)
    #Assert
    assert result == [2,5,7,11]