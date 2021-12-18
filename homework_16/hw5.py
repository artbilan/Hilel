def homework_1(string):
    string = string.title()
    return string


def homework_2(string):
    a = string
    a1, a2, a3, a4, a5, a6, a7, a8 = a[:4], a[5:17], a[18:21], a[22:24], a[26:32], a[33:37], a[38:46], a[47:51]
    a = {a1:a2, a3:a4, a5:a6, a7:a8}
    return a


def homework_3(new_list):
    new_list = str(new_list)
    new_list = new_list.lower()
    return new_list
