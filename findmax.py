def find_max(list):
    max = list[0]
    for i in list:
        if (max < i):
            max=i
    return max

    