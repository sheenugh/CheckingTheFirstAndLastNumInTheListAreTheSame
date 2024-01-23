

#----- FUNCTIONS -----
def is_last_and_first_num_same(numbers):
    if numbers:
        return numbers[0] == numbers[4]
    else:
        return False

# PSEUDO CODE
# - Actual Code
# - Given lists
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]


# - Result
result_in_x = is_last_and_first_num_same(numbers_x)
print("The result is: ", result_in_x)
result_in_y = is_last_and_first_num_same(numbers_y)
print("The result is ", result_in_y)

