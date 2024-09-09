# Вариант 1 с подробной разбивкой
print('Вариант 1')
students = {"Виктория", "Злата", "Михаил", "Тимур", "Мария"}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students_list = sorted(students)  # Преобразование множества в сортированный список

academic_performance = {}
academic_performance.update({students_list[0]:grades[0],
                             students_list[1]:grades[1],
                             students_list[2]:grades[2],
                             students_list[3]:grades[3],
                             students_list[4]:grades[4]})  # Создание словаря с оценками для закрепления материала
print('Оценки: ', academic_performance)

a1 = sum(academic_performance[students_list[0]])  # Сумма баллов
b1 = len(academic_performance[students_list[0]])  # Количество оценок
c1 = a1/b1  # Средний балл

academic_performance[students_list[0]] = c1  # Заменяем значение оценок средним баллом для первого ученика

academic_performance[students_list[1]] = sum(academic_performance[students_list[1]])/len(academic_performance[students_list[1]])
# Заменяем значение оценок средним баллом для второго ученика

academic_performance[students_list[2]] = sum(academic_performance[students_list[2]])/len(academic_performance[students_list[2]])
academic_performance[students_list[3]] = sum(academic_performance[students_list[3]])/len(academic_performance[students_list[3]])
academic_performance[students_list[4]] = sum(academic_performance[students_list[4]])/len(academic_performance[students_list[4]])
# Замена значений остальных учеников на средние баллы

print('Средние баллы: ', academic_performance)
print('Проверка среднего балла Марии: ', academic_performance['Мария'])


# Вариант 2 краткий с вводом имени
print()
print('Вариант 2')
students = {"Виктория", "Злата", "Михаил", "Тимур", "Мария"}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students_list = sorted(students)  # Преобразование множества в сортированный список

academic_performance = {students_list[0]:sum(grades[0])/len(grades[0]),
                        students_list[1]:sum(grades[1])/len(grades[1]),
                        students_list[2]:sum(grades[2])/len(grades[2]),
                        students_list[3]:sum(grades[3])/len(grades[3]),
                        students_list[4]:sum(grades[4])/len(grades[4])}  # Создание словаря со средним баллом
print('Средние баллы: ', academic_performance)

x1 = input('Введите имя ученика для проверки среднего балла: ')
print('Средний балл ученика ', x1, academic_performance.get(str(x1), 'Такого ученика в списке нет!'))