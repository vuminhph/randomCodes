def first_non_repeat(s):
    if len(s) == 0:
        return ''
    record = {}
    for char in s:
        if record.get(char) == None:
            record[char] = True
        else:
            if record[char]:
                record[char] = False
    
    for k, v in record.items():
        if v:
            return k

print(first_non_repeat('oh my god dude where is my car'))

