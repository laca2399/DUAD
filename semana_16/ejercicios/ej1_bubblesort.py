def bubble_sort(list_to_sort):  
    if not isinstance(list_to_sort, list):
        raise ValueError("Input must be a list")
	
    for outer_index in range(0, len(list_to_sort) - 1): 
    
        has_made_changes = False 
	
        for index in range(0, len(list_to_sort) - 1 - outer_index): 

            current_element = list_to_sort[index] 
            next_element = list_to_sort[index + 1] 

            print(f'-- Iteration {outer_index}, {index}. Current element: {current_element}, Next element: {next_element}')
            

            if current_element > next_element:  
                print('The current element is bigger than the next one. Exchanging them...')  
                list_to_sort[index] = next_element 
                list_to_sort[index + 1] = current_element 
                has_made_changes = True 

        if not has_made_changes:
            break
    return list_to_sort 
