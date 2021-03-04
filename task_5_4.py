src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list_2 = [src[i+1] for i in range(len(src)-1) if src[i] < src[i+1]]
print(f'самый короткий путь: {new_list_2},   {type(new_list_2)}')

new_list = []
for i in range(len(src)-1):
    if src[i] < src[i+1]:
        list = src[i+1]
        new_list.append(list)
print(f'решение по длиннее: {new_list},   {type(new_list)}')
