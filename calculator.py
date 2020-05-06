class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.stack = [None for i in range(size)]

    def overflown(self):
        return self.top == self.size

    def isEmpty(self):
        return self.top == -1

    def push(self, value):
        if not self.overflown():
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if not self.isEmpty():
            item = self.stack[self.top]
            self.top -= 1
            return item

def main():
    s = '(2 + (4 + 2) - 1) - (5 + 8)'
    print(calculator(s))

def calculator(s):
    s = s.replace(' ', '')

    max_depth = 10
    result = [0 for i in range(max_depth)]
    depth_level = 0

    parenthesis_st = Stack(max_depth)
    operand_st = Stack(2)
    operator_st = Stack(2)
    
    for char in s:
        if char == '(':
            parenthesis_st.push(char)
            depth_level += 1
        elif char.isdigit():
            operand_st.push(int(char))
            if not operator_st.isEmpty():
                result[depth_level] += operation_result(operator_st, operand_st)
        elif char in ('+', '-'):
            operator_st.push(char)
        elif char == ')':
            depth_level -= 1
            result[depth_level] += sum(result[depth_level + 1])
            result[depth_level + 1] = 0

    return result[0]


def operation_result(operator_st, operand_st):
    return operand_st.pop() + operand_st.pop() if operator_st.pop() == '+' else operand_st.pop() - operand_st.pop()

if __name__ == '__main__':
    main()