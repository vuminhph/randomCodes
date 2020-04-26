from timeit import default_timer as process_time

def reverse_string(string):
    reversed_str = ''
    for i in range(len(string) - 1, -1, -1):
        reversed_str += string[i]
    return reversed_str

string = 'hello world!'

start = process_time()
print(reverse_string(string), end='\t')
end = process_time()
print(end - start)

# start = process_time()
# print(string[::-1], end='\t')
# end = process_time()
# print(end - start)