
def union (list1, list2):
    """takes 2 lists; then coverts them to sets and returns the union"""
    return set(list1).union(set(list2))



print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True