def sum_function(num_1, num_2):
    for index in range(len(num_1)):
        try:
            yield f" ('{num_1[index]}' ,'{num_2[index]}')"
        except IndexError:
            yield f" ('{num_1[index]}' ,None)"


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result = sum_function(tutors, klasses)
for i in range(len(tutors)):
    if i >= len(tutors):
        break
    print(next(result))
print(type(result))

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В']
result = sum_function(tutors, klasses)
for i in range(len(tutors)):
    if i >= len(tutors):
        break
    print(next(result))
print(type(result))
