my_list = [2, 2, 7, 9, 3, 1, 1, 10, 8, 5]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)
