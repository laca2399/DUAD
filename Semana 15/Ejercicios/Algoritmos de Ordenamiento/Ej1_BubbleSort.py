#Function creation
def bubble_sort(list):  
    n = len(list)  #length of list and save it in variable n

    for i in range(n):  #External loop to control general iterations of algorithm
        exchange = False  #Initialize exchange as False. 
        #Exchange will indicate if there was an exchange during iteration, if not loop finishes as list is sorted

        for j in range (0, n - i - 1): #Internal loop that starts from element 0 to the before last element
            current_element = list[j]  #saves current element used for show in print
            next_element = list[j+1]  #saves next element used for show in print
            print(f'-- Iteration {i}, {j}. Actual element: {current_element}, Next element: {next_element}')
            if list[j] > list[j + 1]:  #if current element bigger than next element
                list[j], list[j+1] = list[j+1], list[j]  #switch places
                exchange = True  #As their was an exchange it is assigned as True
                print(f'   -> Exchange made: {list}')

        if not exchange:  #When no exchange
            break

unsorted_list = [25, 10, 33, 34, 2, 5, 63, 22]

print("List before bubble sort:", unsorted_list)

bubble_sort(unsorted_list)

print("List after bubble sort:", unsorted_list)