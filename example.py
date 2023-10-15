def swap_max(items: list) -> list:
    max_pos = items.index(max(items))
    items[0], items[max_pos] = items[max_pos], items[0]
    return items


my_list = [1, 2, 3, 5, 4]
print(swap_max(my_list))

