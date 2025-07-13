def ordinal_indicator(num):
    """ determines what ordinal indicator to return to calling function based on value provided.
    Note that I decided to programmatically determine the ordinal indicator versus hard-coding since
    the user is asked to enter 6 numbers. This indicates that a future use may require
    the user to enter 10, or 20 or 100 numbers, so I wanted to build scalability into
    the solution."""

    teen_year_check = num % 100
    if 10 <= teen_year_check <= 19:
        return "th"
    
    match num % 10:
        case 0:
            return "th"
        case 1:
            return "st"
        case 2:
            return "nd"
        case 3:
            return "rd"
        case _:
            return "th"

def get_numbers():
    """ gets 6 numbers from the user and return a list of those numbers.
    Note that I don't do any input validation."""
    numbers = []
    for idx in range(1, 7):
        if idx == 6:
            char = input("Enter the last number: ")
            print()
        else:
            char = input(f"Enter the {idx}{ordinal_indicator(idx)} number: ")
        numbers.append(char)
    return numbers

def is_number_in_list(numbers):
    """ determines if the 6th number is present in the first 5 numbers and outputs result"""
    final_value = numbers[5]
    remaining_values = numbers[:5]
    remaining_values_cleaned = ",".join(remaining_values)
    if final_value in remaining_values:
        print(f"{final_value} is in {remaining_values_cleaned}.")
    else:
        print(f"{final_value} isn't in {remaining_values_cleaned}.")
    
is_number_in_list(get_numbers())