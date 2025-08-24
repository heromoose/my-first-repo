
def interleave(list1, list2):
    """since the requirements indicate both lists will be the same size, I decided
    to go with a simple approach. Index through the arrays and add them to a final array
    in an interleaved pattern. If the list sizes are different, only the elements through
    the end of list1 will be interleaved."""
    result = []
    for index in range(len(list1)):
        result.append(list1[index])
        result.append(list2[index])

    return result

def interleave2(list1, list2):
    combined = zip(list1, list2)
    result = []
    # now iterate through each tuple and extract
    for element in combined:
        result.extend(element)
    return result


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave2(list1, list2) == expected)      # True