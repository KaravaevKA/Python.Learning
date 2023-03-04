# Дано натуральное число *N* и последовательность из *N* элементов. Требуется вывести эту последовательность в обратном порядке.

# def rec(N):
#     i = input()
#     if N == 1:
#         return i
#     return (rec(N-1) + " " + i)
# m = int(input())
# print(rec(m))

# Написать функцию вычисления факториала числа n:


# def factorial(n):
#     if (n==1):
#         return 1
#     for i in range(1,n):
#         return n*factorial(n-i)   

# print(factorial(4))

# Написать функцию для нахождения наибольшего общего делителя двух чисел:

# def nod(a, b):
#     if a<b:
#         a, b = b, a
#     if a%b == 0:
#         return b
#     return nod(b, a%b)

# print(nod(48,36))

# Написать функцию для нахождения суммы цифр числа:

# def sum(N):
#     if (N % 10 == 0):
#         return N
#     return sum(N//10) + N%10
# M = int(input())
# print(sum(M))

# Найти N-е число Фибоначчи 
# n= int(input())
# def Fib(n):
#     if n == 1 or n==2:
#         return 1
#     return Fib(n-2) + Fib(n-1)
# print(Fib(n))