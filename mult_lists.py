def multiply_list(list1, list2):
    """ iterate through lists, multiply numbers from each list and store in new list
    don't mutate the original lists. Also, bonus, prevent index out of range error.
    return new final list with results."""
    final_list = []

    for num1, num2 in zip(list1, list2):
        final_list.append(num1 * num2)
    return final_list


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

multiply_list(list1, list2)

