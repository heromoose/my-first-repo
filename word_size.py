
def word_sizes(string):
    word_sizes = {}
    word_list = string.split()
    for word in word_list:
        size = len(word)
        if size in word_sizes:
            # increment
            word_sizes[size] += 1
        else:
            # create new key/val pair
            word_sizes[size] = 1
    return word_sizes


string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
