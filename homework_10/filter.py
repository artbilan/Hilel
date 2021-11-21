def new_filter(number: int, number_list: list, smaller=False) -> list:
    new_list = []
    if smaller == False:
        for i in number_list:
            if i > number:
                new_list.append(i)
        return new_list
    elif smaller == True:
        for i in number_list:
            if i < number:
                new_list.append(i)
        return new_list


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 500, 499, 900, -10]

cc = new_filter(-1, a, smaller=True)  # smaller is False - search from right side, smaller is True - left side
print(cc)
