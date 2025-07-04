def is_palindrome(phrase):
    """ compares a string to its reversed form. returns true if palindromic, 
    false otherwise"""
    return phrase[::-1] == phrase 

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)