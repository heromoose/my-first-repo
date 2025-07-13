STR_TO_NUM = {"0": 0, "1": 1, "2": 2, "3": 3,
              "4": 4, "5": 5, "6": 6,
              "7": 7, "8": 8, "9": 9
              }

def string_to_integer(string):
    """ this function receives a string with only numeric chars, and then converts
    the string to an actual integer without using any of python's build-in 
    conversion methods. The return value is the converted number."""
    final_num = 0
    for char in string:
        final_num = (final_num * 10) + STR_TO_NUM[char]
    return final_num


print(string_to_integer("0") == 0) # True
print(string_to_integer("4321") == 4321) # True
print(string_to_integer("1") == 1)  # True
print(string_to_integer("570") == 570)  # True

# use a dict mapping to look up numeric values, that's the key to the problem
# iterate thru each char
# look up in the mapping
# need an index counter to handle placevalue
