def strip_non_alphanum(phrase):
    """ strips out any non alpha numeric chars and returns the cleaned string"""
    final_str = ""
    for char in phrase:
        if char.isalnum():
            final_str += char
    return final_str


def is_real_palindrome(phrase):
    """ compares a string to its reversed form. returns true if palindromic, 
    false otherwise. Preps the string by normalizing for case and calling a helper
    function to strip out non alpha numeric chars.
    """

    phrase = strip_non_alphanum(phrase.casefold()) # handles case sensitivity

    return phrase[::-1] == phrase 


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True