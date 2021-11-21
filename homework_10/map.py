def new_map(update_string: str, other_list: list) -> list:
    new_list = []
    for i in other_list:
        new_list.append(f'{update_string} {i}')
    return new_list


names = ["John", "Robert", "Marta"]
new_li = new_map("Hello", names)
print(new_li)
