import time
from typing import Iterable, Any


def divide_and_conquer_algo(array:Iterable, index:int, length_of_array:int, _max:bool=True) -> Any:
    
    """Function to find out the maximum value
    in the an array.

    Args:
        array (Iterable): array
        index (int): index of the value to start
        _max (bool, optional): `True` for max `False` for min. Defaults to True.

    Returns:
        Any: Returns maximum value in an array if an argument `max` is `True`
        else minimum value
    """
    
    max_or_min = -1 if _max else 0
    value_1 = array[index]
    value_2 = array[index + 1]
    
    if index.__ge__(length_of_array - 2):
        if _max:
            return value_1 if value_1.__gt__(value_2) else value_2
        else:
            return value_1 if value_1.__lt__(value_2) else value_2
    
    # Recursive function call to find out the maximum value in an array
    max_or_min = divide_and_conquer_algo(array, index + 1, length_of_array, _max)
    
    if _max:
        return value_1 if value_1.__gt__(max_or_min) else max_or_min
    else:
        return value_1 if value_1.__lt__(max_or_min) else max_or_min
    
def linear_time_algo(array:Iterable, _max:bool=True) -> Any:
    min_or_max = array[0]
    
    for element in array:
        if _max:
            if min_or_max < element:
                min_or_max = element
        else:
            if min_or_max > element:
                min_or_max = element
    return min_or_max
            
if __name__ == "__main__":
    # Reading an array from input file
    with open('inputPS5.txt', 'r') as input_file:
        array = list(
            map(lambda x: int(x.rstrip().split('/')[-1]), input_file.readlines())
        )
    
    # Using Divide and Conquer Algo
    start_time = time.time()
    min_value = divide_and_conquer_algo(array, 0, len(array), False)
    idx_min_value = array.index(min_value)
    
    max_value = divide_and_conquer_algo(array, idx_min_value, len(array))
    end_time = time.time()
    idx_max_value = array.index(max_value)
    
    profit = abs(max_value - min_value)
    
    
    output = f"""Maximum Profit(Divide & Conquer): {profit}
Day to buy:  {idx_min_value}
Day to sell: {idx_max_value}"""

    # Using Linear-time Algo 
    min_value = linear_time_algo(array, False)
    idx_min_value = array.index(min_value)
    
    max_value = linear_time_algo(array[idx_min_value:])
    idx_max_value = array.index(max_value)
    
    profit = abs(max_value - min_value)    
    
    output += f"""
Maximum Profit(Iterative Solution): {profit}
Day to buy:  {idx_min_value}
Day to sell: {idx_max_value}"""

    with open('outputPS5.txt', 'w') as output_file:
        output_file.write(output)
    
    print("For Divid and Conquer")
    print(f'Time Complexity: {time.strftime("%H:%M:%S", time.gmtime(end_time - start_time))} seconds')
        
    