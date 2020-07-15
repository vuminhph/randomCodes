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

    def add_top_value(self, add_by):
        self.stack[self.top] += add_by

def main():
    s = '3 - 1 + 2'
    print(calculator(s))

def calculator(s):
    s = s.replace(' ', '')
    SIZE = 10

    multi_digit = 0
    negative_opt = [False for i in range(SIZE)]
    
    result_st = Stack(SIZE)
    result_st.push(0)

    for i, char in enumerate(s):
        if char == '(':
            result_st.push(0)

        elif char.isdigit():
            if i != len(s) - 1 and s[i + 1].isdigit():
                    multi_digit = multi_digit * 10 + int(char)
                    continue

            if negative_opt[result_st.top]:
                add_by = - (multi_digit * 10 + int(char))
                multi_digit = 0
                negative_opt[result_st.top] = False
            else:
                add_by = multi_digit * 10 + int(char)
                multi_digit = 0

            result_st.add_top_value(add_by)

        elif char == '-':
            negative_opt[result_st.top] = True

        elif char == ')':
            inner_result = result_st.pop()
            inner_result = inner_result  if not negative_opt[result_st.top] else - inner_result

            result_st.add_top_value(inner_result)

    return result_st.pop()


if __name__ == '__main__':
    main()