grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]       # Входные данный

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}        # В ходные данные

list_students = list(students)          # Множество переведено в список

sort_list_students = sorted(list_students)      # Новый список отсортирован

sum_ = 0                         # дополнительные элементы

list_arith_mean = []

dict_mean_grades = {}


for i in grades:            # цикл для среднего ариф
    for j in i:
        sum_ = sum_ + j
    arith_mean = sum_/len(i)
    list_arith_mean.append(arith_mean)
    sum_ = 0


for (x, y) in zip(sort_list_students, list_arith_mean):
    dict_mean_grades[x] = y


print(dict_mean_grades)
