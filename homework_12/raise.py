def func(args, li):
   if len(li) < 10:
       li.append(args)
       print(li)
       print(len(li))
   else:
       raise IndexError("Index out of range")


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

func(10, li)
