my_str = input("введите строку ")
my_word = []
num = 1
for x in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [x]}")
        num += 1
    else:
        print(f" {num} {my_word [x] [0:10]}")
        num += 1
