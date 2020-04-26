def hexEncoder():
    string = input('String: ')
    code = ''
    for char in string:
        code += hex(ord(char))[2:] + ' '
    print(code)
    return code

def hexDecoder(code):
    code = code.split(' ')[:-1]
    string = ''
    for char in code:
        string += chr(int(char, 16))
    print(string)


code = hexEncoder()
hexDecoder(code)