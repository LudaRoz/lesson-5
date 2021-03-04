def odd_generator(number):
    for odd in range(1, number + 1, 2):
        yield odd


def odd_generator_adv(number):
    odd = (odd for odd in range(1, number + 1, 2))
    print(*odd)


n = int(input("Введите количество чисел для генератора "))
odd_to_n = odd_generator(n)
print('простой yield')
for i in range(n):
    if i >= n / 2:
        break
    print(next(odd_to_n))

print('простой print')
odd_generator_adv(n)
