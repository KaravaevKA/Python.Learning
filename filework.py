

def Selection_menu(choice) ->int:
  if choice == 1:
    PrintPhonebook()
  elif choice == 2:
    SearchSurname()
  elif choice == 3:
    SearchNumber()
  elif choice == 4:
    Phonebook_add()
  elif choice == 5:
    Phonebook_save()
  elif choice == 6:
    Phonebook_remove_contact()
  elif choice == 7:
    Phonebook_edit()
  
def Phonebook_edit():
  Phonebook_remove_contact()
  Phonebook_add()


def Phonebook_save():
  file = open('phon copy2.txt', encoding = 'utf-8')
  list_1=list()
  for line in file:
    list_1.append(line)
  file.close()
  file = open('Phonebook.txt', 'w+', encoding = 'utf-8')
  for line in list_1:
    file.write(line)
  file.close()

def Phonebook_remove_contact():
  find = str(input('Выберите контакт: '))
  file = open('phon copy2.txt', encoding = 'utf-8')
  list_1 = list()
  for line in file:
    if find not in line:
      list_1.append(line)
  file.close()
  file = open('phon copy2.txt', 'w',encoding='utf-8')
  for line in list_1:
    file.write(line)
  file.close()

  

def SearchNumber():
  file = open('phon copy2.txt', 'r+', encoding='utf-8')
  list_1=list()
  for line in file:
    list_1.append(line)
  list_result = list()
  number = str(input('Укажите номер: '))
  for line in list_1:
    if number in line:
      list_result.append(line)
  print(list_result)
  file.close()

def SearchSurname():
  file = open('phon copy.txt', 'r+', encoding='utf-8')
  list_1=list()
  for line in file:
    list_1.append(line)
  list_result = list()
  surname = str(input('Укажите фамилию: '))
  for line in list_1:
    if surname in line:
      list_result.append(line)
  print(list_result)
  file.close()

def Phonebook_add():
  file = open('phon copy2.txt', 'a+', encoding='utf-8')
  # surname = str(input('Введите фамилию: '))
  # name = str(input('Введите имя: '))
  # number = str(input('Введите номер: '))
  # description = input('Введите описание: ')
  # file.write('\n')
  # file.write(surname)
  # file.write('  ')
  # file.write(name)
  # file.write('  ')
  # file.write(number)
  # file.write('  ')
  # file.write(description)
  surname = list()
  name = list()
  number = list()
  description = list()
  surname.append(str(input('Введите фамилию: ')))
  name.append(str(input('Введите имя: ')))
  number.append(str(input('Введите номер: ')))
  description.append(str(input('Добавьте описание: ')))
  data = list(*zip(surname, name, number, description))
  for line in data:
    file.write((line) + ' ')

  file.write('\n')

  file.close() 
  
  
def PrintPhonebook():
  file = open('phon copy2.txt', 'r', encoding='utf-8')
  for line in file:
    print(line)
  file.close()

while True:
  print('\nВыберите необходимое действие:\n'
          "1. Отобразить весь справочник\n"
          "2. Поиск по фамилии\n"
          "3. Поиск по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удаление контакта\n"
          "7. Редактирование данных\n"
          "8. Закончить работу")
  choice=int(input())
  if 1<=choice<=7:
    Selection_menu(choice)
  elif choice==8:
    break
  else: print('Ошибка') 
  
    
    
    
