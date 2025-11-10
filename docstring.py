def calculate_average(numbers):
    """
    Calculate the average of a list of numbers

    Parameters:
    numbers (list): A list of numerical values

    Returns:
    float: The average of the numbers in the list

    
    """

    
    if len(numbers) == 0:
        return None
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def find_max(numbers):
    """
    Find the maximum number in a list
    
    Parameters:
    numbers (list): A list of numerical values
    
    """
    if len(numbers) == 0:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

