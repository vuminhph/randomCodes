def get_bell_number(iterations):
    bell_nums = [1]
    last_row = [1]

    while iterations - 1 != 0:
        last_elems = last_row
        last_row = [last_elems[-1]]

        for i in range(len(last_elems)):
            last_row.append(last_elems[i] + last_row[-1])
        
        bell_nums.append(last_row[-1])
        iterations -= 1

    return bell_nums

print(get_bell_number(100))