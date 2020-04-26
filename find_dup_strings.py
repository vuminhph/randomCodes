
def find_duplicates(s):
    word_dict = {c.lower() : 0 for c in s.split(' ')} 
    for word in s.split():
        word_dict[word.lower()] += 1
    return [word for word in word_dict.keys() if word_dict[word] > 1]

s = 'The dog is the best'
print(find_duplicates(s))

