#1
low_str = "john marta james Morgan Adam Maria huang"
up_str = low_str.title()
print(up_str)

#2
a = ["John", "Marta", "James", "Amanda", "Marianna"]
print("***" + "names" + "****************")
print(a[-1])
print(f'  {a[-2]}')
print(f'   {a[-3]}')
print(f'   {a[-4]}')
print(f'    {a[-5]}')

#3
a = "name=Amanda=sssss&age=32&&salary=1500&currency=quro"
a1, a2, a3, a4, a5, a6, a7, a8 = a[:4], a[5:17], a[18:21], a[22:24], a[26:32], a[33:37], a[38:46], a[47:51]
a = {a1:a2, a3:a4, a5:a6, a7:a8}
print(a)
print(type(a))

#4

a = ["FirstItem", "FriendsList", "MyTuple"]
a = str(a)
a1, a2, a3, a4, a5, a6 = a[2:7], a[7:11], a[15:22], a[22:26], a[30:32], a[32:37]

b = a1 + "_" + a2
b = b.lower()

c = a3 + "_" + a4
c = c.lower()

d = a5 + "_" + a6
d = d.lower()
print(b)
print(c)
print(d)


#5
a = """ Есть строка с именами разделенная пробелами "john marta james Morgan Adam Maria huang" преобразовать строку
        таким образом что бы каждое имя однозначно начиналось с большой буквы.

        Есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"],
        выведите в консоль имена каждое с новой строки выровняв по правой стороне используя метод строки и
        форматирование через f string. Так же над именами первой строкой выведини заговловок Names где слово names
        должно быть посредине а остальное пространство заполнено скажем символом "*".

        Есть строка переданная в качестве квери параметров " name=Amanda=sssss&age=32&&salary=1500&currency=quro"./

        Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары значение после равно
        {name: Amanda=sssss, age: 32, salary: 1500, currency: quro} У вас есть список имен переменных в формате кэмел
        кейс ["FirstItem", "FriendsList", "MyTuple"] преобразовать его в список имен переменных для пайтона в формате
        снейк кейс ["first_item", "friends_list", "my_tuple"]."""


b = a.split('\n')
print(type(b))
