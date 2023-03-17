# Написать программу, которая выводит из списка двузначные числа
# numbers = [8, 11, 0, -23, 140, 65, 1996]
# number_new=list(filter(lambda x: 9<x<100 or -9>x>-100, numbers))
# print(number_new)

# print(*filter(lambda x: len(str(abs(int(x)))) == 2, input().split()))


# Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером N x N, состоящий из нулей, а по главной диагонали - единицы. 
# (Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла). 
# Результат вывести в виде таблицы чисел как показано в примере ниже.

# N = int(input())
# list_1 = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
# for r in list_1:   
#     print(*r)
            

# Преобразовать набора списков 
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]

# data=list(zip(users,ids,salary))
# print(data)
# data_new=list(zip(*zip(users,ids,salary)))
# print(data_new)

# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]

# a,b,c = map(list,zip(users, ids, salary))
# print(a,b,c, sep="\n")
# a,b,c= map(list,zip(a,b,c))

# print(a,b,c, sep="\n")


