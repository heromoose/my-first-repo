def find_dup(list1):
    """ uses sort method to order the list; then iterates thru
    once a dupe is found, immediately exits the method and returns
    the dupe value. Also handles edge case of no dupes found"""
    sorted_list = sorted(list1)
    for index in range(len(sorted_list)-1):
        if sorted_list[index] == sorted_list[index + 1]:
            return sorted_list[index]
    return None
        
def find_dup2(lst):
    dups = [element for element in lst if lst.count(element) == 2]
    return dups[0]

def find_dup3(lst):
    seen = set()

    for element in lst:
        if element in seen:
            return element

        seen.add(element)


print(find_dup([1, 5, 3, 6, 5]) == 5) # True
print(find_dup([1, 5, 3, 6, 9]) == None) # True

print(find_dup3([1, 5, 3, 6, 9]))
