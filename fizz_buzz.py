def fizz_buzz(n):
    string_repr = []
    
    for i in range(1, n + 1):
        if i % 15 == 0:
            string_repr.append('fizzbuzz')
        elif i % 3 == 0:
            string_repr.append('fizz')
        elif i % 5 == 0:
            string_repr.append('buzz')
        else:
            string_repr.append(str(i))

    return ''.join(string_repr)

print(fizz_buzz(15))