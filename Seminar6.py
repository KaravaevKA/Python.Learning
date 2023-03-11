# # Завернуть в функцию потом

def ListFill(list_a):
    k = int(input("Введите размер массива: "))
    for i in range(k):
        n = int(input())
        list_a.append(n)
    return(list_a)

def ListFillRandom(list_a):
    import random
    k = int(input("Введите размер массива: "))
    for i in range(k):
        n = random.randint(1,5)
        list_a.append(n)
    return(list_a)
# list_1=[]
# list_2=[]
# print(ListFill(list_1))
# print(ListFill(list_2))

# list_3=[]
# for i in range(len(list_1)):
#     if list_1[i] not in list_2:
#         list_3.append(list_1[i])
# print (list_3)


# Задача 41
# n = int(input())
# list_1 =[]
# for i in range(n):
#     x = int(input())
#     list_1.append(x)
# count = 0
# for i in range(1, n - 1):
#   if list_1[i - 1] < list_1[i] < list_1[i + 1]:
#     count += 1
# print(count)

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.



# list_1=[]
# print(ListFillRandom(list_1))
# count = 0
# while (k>0):
#     for i in range (len(list_1)-1):
#         if list_1[0] == list_1[i]:
#             count+=1
#             list_1.pop(i)
#             break
#     k-=1
#     list_1.pop(0)
# print(count)

# def _res(arr: list) -> int:
#     counter = 0
#     for item in arr:
#         counter += (arr.count(item)//2)
#     return counter//2
# def random_list(N: int, min=-100, max=100) -> list:
#     import random
#     arr = []
#     for i in range(N):
#         arr.append(random.randint(min, max))
#     return arr


# if __name__ == "__main__":
#     count = int(input("Введите длину списка: "))
#     arr = random_list(count, 0, 10)
#     print(arr)
#     print(_res(arr))

# a = int(input('Введите первый элемент прогрессии: '))
# b = int(input('Введите разность прогрессии: '))
# n = int(input('Введите количество элементов прогрессии: '))
# for i in range(n):
#     print(a+i*b)

# a = int(input())
# b = int(input())
# list_1=[-5,9,0,3,-1,-2,1,-4,-2,10,-9,0,-5,-5,7]
# print(list_1)
# for i,x in enumerate(list_1):
#     if b <= x <= a:
#         print("Индекс", i, "значение" , x)
