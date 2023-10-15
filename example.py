def swap_max(items: list) -> list:
    max_pos = 0
    for i in range(len(items)):
        if items[i] >= items[max_pos]:
            max_pos = i
    tmp = items[0]
    items[0] = items[max_pos]
    items[max_pos] = tmp
    #items[0], items[max_pos] = items[max_pos], items[0]
    return items


my_list = [1, 2, 3, 5, 4]
print(swap_max(my_list))

