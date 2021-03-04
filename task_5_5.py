src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

src_uniq = [element for element in src if src.count(element) == 1]
print(src_uniq)
