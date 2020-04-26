def lonely_number(numbers):
    occurences = {}
    for i in range(len(numbers)):
        if occurences.get(numbers[i]) is None:
            occurences[numbers[i]] = 1
        else:
            occurences[numbers[i]] += 1
    
    for key in occurences.keys():
        if occurences[key]  == 1:
            return key


numbers = [4,1,4,7,9,4,7,1]
print(lonely_number(numbers))
