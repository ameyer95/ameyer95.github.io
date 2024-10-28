# Exercises for CS 111: Intro CS at Carleton College
# Recursion

## Exercise 0

def is_palindrome(str):
    return False


## Exercise 1

def triangular(n):
    return 0

# Test cases (uncomment these when you're ready to test your code)
# print(triangular(0)) # 0
# print(triangular(1)) # 1
# print(triangular(2)) # 3
# print(triangular(5)) # 15
# print(triangular(10)) # 55

## Exercise 2

def reverse_string(str):
    return ""

# Test cases (uncomment these when you're ready to test your code)
# print(reverse_string("a")) # "a"
# print(reverse_string("hello")) # "olleh"
# print(reverse_string("world")) # "dlrow"
# print(reverse_string("racecar")) # "racecar"
# print(reverse_string("This is a very long string compared to the others")) # "srehto eht ot deretne si gnirts gnol yrev a si sihT"


## Exercise 3

def nested_list_depth_2(lst, target):
    ''' 
        Iterative function that takes a depth-2 nested list and a target value. 
        Each item in lst is either an integer or a list of integers.
        Checks whether target is in lst. 
    '''
    # Iterate over items in the list
    for item in lst:
        # Check if the item is a list
        if type(item) == list:
            # Iterate over items in the list
            for i in item:
                if i == target:
                    return True # Return True if i is the target
        # If item is not a list, it is an integer 
        else:
            if item == target:
                return True # Return True if item is the target

    return False # Return False if target is not found
        

def nested_list_recursive(lst, target):
    '''
        Recursive function that takes a nested list of any depth, and checks 
        whether the target value is in the list.
    '''
    return False

# Test cases (uncomment these when you're ready to test your code)
depth_2_lst = [1, [2, 3], 4, [5, 6]]
# print(nested_list_recursive(depth_2_lst, 2)) # True
# print(nested_list_recursive(depth_2_lst, 7)) # False
depth_3_lst = [1, [2, [3, 4]], 5, [6, [7, 8]]]
# print(nested_list_recursive(depth_3_lst, 3)) # True
# print(nested_list_recursive(depth_3_lst, 9)) # False
depth_5_lst = [1, [2, [3, [4, [5]]]], 6]
# print(nested_list_recursive(depth_5_lst, 5)) # True
# print(nested_list_recursive(depth_5_lst, 7)) # False

## Exercise 4

def fibonacci_recursive(n):
    return 0

# Test cases (uncomment these when you're ready to test your code)
# print(fibonacci_recursive(0)) # 0
# print(fibonacci_recursive(1)) # 1
# print(fibonacci_recursive(2)) # 1
# print(fibonacci_recursive(5)) # 5
# print(fibonacci_recursive(10)) # 55

## Exercise 5

def binary_to_decimal(str):
    return 0

# Test cases (uncomment these when you're ready to test your code)
# print(binary_to_decimal("0")) # 0
# print(binary_to_decimal("1")) # 1
# print(binary_to_decimal("10")) # 2
# print(binary_to_decimal("1010")) # 10
# print(binary_to_decimal("1111")) # 15
# print(binary_to_decimal("1000000")) # 64
