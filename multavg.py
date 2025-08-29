def get_product(values):
    """simple reduction loop (mult)"""
    product = 1
    for val in values:
        product *= val
    return product


def multiplicative_average(values):
    """reduce the list with multiplication; divide by length of list; 
    format to 3 places. Also check edge cases."""
    if not(len(values)):
        return None
    product = get_product(values)
    avg_prod = product / len(values)
    return f"{avg_prod:.3f}"

print(multiplicative_average([-3, 5]) == "-7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([0]) == "0.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
print(multiplicative_average([]) == None)