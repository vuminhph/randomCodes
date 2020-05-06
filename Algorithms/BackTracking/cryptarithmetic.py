SIZE = 10

def main():
    # str1 = 'SEND'
    # str2 = 'MORE'
    # sum_str = 'MONEY'
    str1 = 'FDB'
    str2 = 'CEGA'
    sum_str = 'DCCB'
    letter_list = get_letters_list(str1, str2, sum_str)

    mappings = {letter : -1 for letter in letter_list}
    if solve_puzzle(str1, str2, sum_str, 0, mappings):
        print(mappings)
    else:
        print('No solution found')
    

def solve_puzzle(str1, str2, sum_str, counter, mappings):
    if len(sum_str) == 0:
        return True
    sum_letter = sum_str[-1]

    if len(str1) == 0 or len(str2) == 0:
        if len(str1) == 0 and len(str2) == 0:
            counter_wrapper = [counter] 
            sum_assignment = get_sum_assignment(sum_letter, 0, 0, counter_wrapper, mappings)
            
            if sum_assignment == 1:
                return True
            else:
                return False

        if len(str1) == 0:
            letter2 = str2[-1]
            letter2_assignments = get_possible_assignments(letter2, mappings)

            letter2_original = mappings[letter2]
            for num2 in letter2_assignments:
                mappings[letter2] = num2
                
                counter_wrapper = [counter]
                sum_assignment = get_sum_assignment(sum_letter, 0, num2, counter_wrapper, mappings)
                sum_original = mappings[sum_letter]
                
                if sum_assignment != -1:
                    mappings[sum_letter] = sum_assignment
                    if solve_puzzle('', str2[:-1], sum_str[:-1], counter_wrapper[0], mappings):
                        return True
                    mappings[sum_letter] = sum_original
            mappings[letter2] = letter2_original
            return False

        if len(str2) == 0:
            letter1 = str1[-1]
            letter1_assignments = get_possible_assignments(letter1, mappings)

            letter1_original = mappings[letter1]
            for num1 in letter1_assignments:
                mappings[letter1] = num1
                
                counter_wrapper = [counter]
                sum_assignment = get_sum_assignment(sum_letter, 0, num1, counter_wrapper, mappings)
                sum_original = mappings[sum_letter]
                
                if sum_assignment != -1:
                    mappings[sum_letter] = sum_assignment
                    if solve_puzzle(str1[:-1], '', sum_str[:-1], counter_wrapper[0], mappings):
                        return True
                    mappings[sum_letter] = sum_original
            mappings[letter1] = letter1_original
            return False

    else:
        letter1 = str1[-1]
        letter2 = str2[-1]
        letter1_assignments = get_possible_assignments(letter1, mappings)
        if len(letter1_assignments) == 0:
            return False

        letter1_original = mappings[letter1]
        for num1 in letter1_assignments:
            mappings[letter1] = num1
            letter2_assignments = get_possible_assignments(letter2, mappings)
            if len(letter2_assignments) == 0:
                continue

            letter2_original = mappings[letter2]
            for num2 in letter2_assignments:
                mappings[letter2] = num2
                counter_wrapper = [counter]
                sum_assignment = get_sum_assignment(sum_letter, num1, num2, counter_wrapper, mappings)
                
                if sum_assignment != -1:
                    sum_original = mappings[sum_letter]
                    mappings[sum_letter] = sum_assignment
                    if solve_puzzle(str1[:-1], str2[:-1], sum_str[:-1], counter_wrapper[0], mappings) == True:
                        return True
                    mappings[sum_letter] = sum_original
            mappings[letter2] = letter2_original
        mappings[letter1] = letter1_original
        return False

def get_possible_assignments(letter, mappings):
    if mappings[letter] != -1:
        return [mappings[letter]]
    
    possible_assignments = [i for i in range(SIZE)]
    possible_assignments = [i for i in possible_assignments if i not in mappings.values()]
    return possible_assignments

# Pass counter as a list to be mutated
def get_sum_assignment(letter, num1, num2, counter, mappings):
    sum = num1 + num2 + counter[0]
    sum, counter[0] = (sum, 0) if sum < 10 else (sum - 10, 1)

    # if letter is not assigned in mappings
    if mappings[letter] == -1:
        # if value is used, fail
        if sum in mappings.values():
            return -1
        # else map letter to sum value
        return sum
    
    # if letter is assigned and is not sum value, fail
    if mappings[letter] != sum:
        return -1
    return sum

def puzzle_is_solved(mappings):
    for value in mappings.values():
        if value == -1:
            return False
    return True

def get_letters_list(*args):
    letters = []
    for string in args:
        for char in string:
            if char.upper() not in letters:
                letters.append(char.upper())
    return letters

if __name__ == '__main__':
    main()