def getTV(actual, guess):
    actual_dict = {}
    for i in range(len(actual)):
        if actual_dict.get(actual[i]) is None:
            actual_dict[actual[i]] = [i]
        else:
            actual_dict[actual[i]].append(i)
    
    targets = 0
    vicinities = 0

    for i in range(len(guess)):
        if actual_dict.get(guess[i]) is None:
            continue
        for loc in actual_dict[guess[i]]:
            if i == loc:
                targets += 1
            if i == loc - 1 or i == loc + 1:
                vicinities += 1

    return str(targets) + 'T' + str(vicinities) + 'V'
    return f'{targets}T{vicinities}V'

print(getTV('345','135'))