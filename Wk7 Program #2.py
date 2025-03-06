#reilly kurth
#3/6/2025
#wk7 program 2

def larger_than_n(numbers_list, n):
    result = [num for num in numbers_list if num > n]
    return result

# Example usage
list = [-100, -50, -5.5, 0, 1, 3, 17.5, 26, 1000]
n = -1
result = larger_than_n(list, n)
