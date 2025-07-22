NUM_TO_STR = {0: "0", 
              1: "1", 2: "2", 3: "3",
              4: "4", 5: "5", 6: "6",
              7: "7", 8: "8", 9: "9"
              }

def integer_to_string(num):
    """ takes an integer as an argument, and returns a string-ified version
    of that integer, without using any of pythons built-in conversion functions."""
  
    if num == 0: # handles edge case that would otherwise break my algorith
        return "0"
    
    place = 1 # used to select a specific digit place in the overall integer
    numstring = "" # stores the string version of the integer

    while num >= place: # true as long as there are more digits to convert
        digit = (num // place) % 10 # this is the key conversion algorith. 
        numstring = NUM_TO_STR[digit] + numstring # converts digit to a string and appends
        place = place * 10 # moves to the next place (hundreds, thousands, etc)
    return numstring


print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

