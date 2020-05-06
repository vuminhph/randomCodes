def main():
    arr = [5,9,21,7]
    print(has_equal_subsets(arr))

def has_equal_subsets(arr):
    total_sum = sum(arr)
    if total_sum % 2 == 1:
        return False
    goal = total_sum // 2

    sub_arr = []
    return find_sub_arr_by_sum(sub_arr, arr, goal)


def find_sub_arr_by_sum(sub_arr, arr, goal, ):
    if sum(sub_arr) == goal:
        return True
    if sum(sub_arr) > goal:
        return False
    possible_elems = get_possible_elems(sub_arr, arr)
    for elem in possible_elems:
        sub_arr.append(elem)
        if find_sub_arr_by_sum(sub_arr, arr, goal) == True:
            return True
        sub_arr.pop()
    return False
        
def get_possible_elems(sub_arr, arr):
    return [i for i in arr if i not in sub_arr]

if __name__ == '__main__':
    main()