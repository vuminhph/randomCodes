def min_window(in_str, req_str):
    req_record = {}
    for c in req_str: req_record[c] = 0

    # print(map)
    counter = len(req_str)
    begin = 0
    end = 0
    substr_size = float("inf")
    head = 0

    while end < len(in_str):
        if in_str[end] not in req_str:
            end += 1
        else:
            if req_record[in_str[end]] == 0:
                counter -= 1
            req_record[in_str[end]] += 1
            end += 1
        
        while counter == 0:
            if in_str[begin] not in req_str:
                begin += 1
            else:
                if end - begin < substr_size:
                    head = begin
                    substr_size = end - head

                req_record[in_str[begin]] -= 1
                if req_record[in_str[begin]] == 0:
                    counter += 1
                begin += 1

    return "" if substr_size == float("inf") else in_str[head: head + substr_size]

print(min_window('HGFADSABKAFGCDKCEFA', 'ABKC'))