def running_total(numlist):
    """ take a list of numbers as input
    and return a new list which represents a cumulative total
    of the original list"""
    run_total = 0
    numlist_final = []
    for num in numlist:
        run_total += num
        numlist_final.append(run_total)
    return numlist_final

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])  