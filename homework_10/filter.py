def new_filter(number: int, number_list: list, smaller=False) -> list:
    new_list = []
    if smaller is False:
        for i in number_list:
            if i > number:
                new_list.append(i)
        return new_list
    elif smaller is True:
        for i in number_list:
            if i < number:
                new_list.append(i)
        return new_list


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 500, 499, 900, -10]
search = new_filter(-1, li, smaller=True)  # smaller is False - search from right side, smaller is True - left side
print(search)
