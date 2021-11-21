a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 500]

def new_filter(number, list, smaller = False):
    new_list = []
    if smaller == False:
        for i in list:
            if i > number:
                new_list.append(i)
        return new_list
    elif smaller == True:
        for i in list:
            if i < number:
                new_list.append(i)
        return new_list






cc = new_filter(9, a, smaller = False)
print(cc)