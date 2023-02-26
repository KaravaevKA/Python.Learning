# Задача 25

# instr = "a a a b c a a d c d d"
# count = {}

# for ch in instr.split():
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1

# outString =""

# for key in count:
#     for i in range(count[key]):
#         if i == 0:
#             outString += key + " "
#         else:
#             outString += key + "_" + str(i) + " "

# print(outString)

# stroka = input().split()
# result = {}
# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1

# Задача 27
# s = "She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells."
 
# print(len(set(s.lower().split())))

# Орел и решка
# s=input()
# t=0
# while "Р"*(t+1) in s:
#     t+=1
# if t!=0:
#     print(t)
# else:
#     print(0)

# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.

# import random
# n = 1
# max_number = -1
# while n != 0:
#     n = random.randint(0, 10)
#     print(n)
#     if max_number < n:
#         max_number = n
# print(max_number)

# Задача про холодильники
# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". 
# Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" 
# (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы


# freezer_count= int(input()) 
# virus_dict = {a : set("aA"),
#               n : set("nN"),
#               t : set("tT"),
#               o : set("oO")
#               }
# list_1 = []
# for i in range(freezer_count):
#     freezer_name = input()
#     list_1.append(n)


# n = int(input())
# list1 = []
# for i in range(n):
#     a = input()
#     if 'a' in a:
#         a = a[a.find('a'):]
#         if 'n' in a:
#             a = a[a.find('n'):]
#             if 't' in a:
#                 a = a[a.find('t'):]
#                 if 'o' in a:
#                     a = a[a.find('o'):]
#                     if 'n' in a:
#                         list1.append(i + 1)                   
# print(list1)


# ДОМАШНЯЯ РАБОТА


# Задача 22
# n = int(input('Введите размер первого множества '))
# m = int(input('Введите размер второго множества '))
# a = set()
# b = set()
# for i in range(n):
#     a.add(input())
# print(a)
# for i in range(m):
#     b.add(input())
# print(b)
# u = a.union(b)

# print(sorted(u))

# Задача 24
# n = int(input())
# arr = list()
# for i in range(n):
#     x = int(input())
#     arr.append(x)
# arr_count = list()
# for i in range(len(arr)-1):
#     arr_count.append(arr[-2]+arr[-1]+arr[0])
#     print(max(arr_count))