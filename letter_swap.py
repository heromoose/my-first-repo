def reverse_letters(word):
    """ reverses the first and last letter of a word"""
    if len(word) == 1:
        return word
    else:
        return (word[-1] + word[1:-1] + word[0])

def swap(phrase):
    """ takes a phrase, performs specific operations, and then
    returns the rejoined, modified phrase"""
    new_phrase = []
    words = phrase.split()
    for word in words:
        new_phrase.append(reverse_letters(word))
    return " ".join(new_phrase)


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True