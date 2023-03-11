# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# print(values)
# values_transformed = list(map(lambda x: x, values))
# print(values_transformed)

# if values == values_transformed:
#     print('ok')
# else:
#     print("ne ok")


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# def res(orbits:list) -> list:
#     max_orbit = max(map(lambda a: a[0]*a[1], filter(lambda a: a[0] != a[1], orbits)))     #map: перемножение элементов, фильтр: элементы неравны
#     return list(filter(lambda a: a[0]*a[1] == max_orbit, orbits))
# print(res(orbits))



# def find_farthest_orbit(orbits):
#     return max(orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1])


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (100, 100)]
# print(*find_farthest_orbit(orbits))
# Ключ "Распаковывает значения кортежа, и дает сравнение"

strings = ["Hello, world!", "Word", "Another sentence"]
string1=list(filter(lambda x:len(x.split())==1,strings)) #.split() "заменяет" пробелы в списках, чтобы мы могли посчитать здесь слова
print(string1)



#HOMEWORK

