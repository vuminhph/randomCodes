def validate_symbols(s):
    para_stack = []

    for c in s:
        if c in ['{', '(', '[']:
            para_stack.append(c)
        else:
            if c == ')':
                if para_stack[-1] != '(':
                    return False
                else:
                    para_stack.pop()
            if c == '}':
                if para_stack[-1] != '{':
                    return False
                else:
                    para_stack.pop()
            if c == ']':
                if para_stack[-1] != '[':
                    return False
                else:
                    para_stack.pop()
    return True

print(validate_symbols('{{[}'))