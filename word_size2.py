def strip_word(word):
    """ takes a string as input and returns a version with only alpha characters."""
    alpha_word = ''.join(char for char in word if char.isalpha())
    return alpha_word

def word_sizes(string):
    """takes a string as input, and returns a dict object which contains a frequency
    of the count of each word size. Note that non-letters are excluded from the word
     size calculation. """
    word_sizes = {}
    word_list = string.split()
    for word in word_list:
        # here you need to clean the word
        word = strip_word(word)
        size = len(word)
        if size == 0:
            continue
        word_sizes[size] = word_sizes.get(size, 0) + 1
    return word_sizes

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})