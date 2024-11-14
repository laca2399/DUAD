#Modifica el bubble_sort para que funcione de derecha a izquierda, 
# ordenando los números menores primero (como en la imagen de abajo).
def bubble_sort(list):
    n = len(list)

    for i in range(n):
        exchange = False

        for j in range(n - 1, i, -1): 
            #n-1: First element of range, that corresponds to the last element of list
            #i: stop value, index where loop has to stop
            #-1: Step, as it is negative, it will decrease, so from right to left

            current_element = list[j]  #saves current element used for show in print
            prev_element = list[j-1]  #saves prev element used for show in print
            print(f'-- Iteration {i}, {j}. Actual element: {current_element}, Previous element: {prev_element}')
            if list[j] < list[j - 1]:  #if current element least than prev element
                list[j], list[j-1] = list[j-1], list[j]  #switch places
                exchange = True  #as there was an exchange, it is assigned as True
                print(f'   -> Exchange made: {list}')
        
        if not exchange:
            break

unsorted_list = [25, 10, 33, 34, 2, 5, 63, 22]

print("List before bubble sort:", unsorted_list)

bubble_sort(unsorted_list)

print("List after bubble sort:", unsorted_list)