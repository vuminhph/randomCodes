def is_dollar_delete_equal(arr):
    dollar_str = arr[0]
    non_dollar_str = arr[1]

    dollar_locs = []
    for i in range(len(dollar_str)):
        if dollar_str[i] == '$':
            dollar_locs.append(i)

    for i in range(len(dollar_str)):
        if i - 1 not in dollar_locs and i not in dollar_locs:
            if dollar_str[i] not in non_dollar_str:
                return False
    return True
