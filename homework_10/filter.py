import re


def new_filter(lam, new_list):
    new_li = []
    new_int = None
    lam = str(lam)
    cc = re.findall('\d+', lam)
    for i in cc:
        if i.isdigit():
            new_int = int(i)
    if "<" in lam:
        for i in new_list:
            if i < new_int:
                new_li.append(i)
    elif ">" in lam:
        for i in new_list:
            if i > new_int:
                new_li.append(i)
    return new_li


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 500, 499, 900, -10]

a = new_filter(lambda x: x < 0, li)
print(a)
