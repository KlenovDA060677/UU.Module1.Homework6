# Практическое задание по теме: "Словари и множества"

# Создаем словарь и выводим данные словаря на экран
my_dict = {"anton": 1980, "aleksandr": 1983, "andrey": 1987, "boris": 1988,
           "konstantin": 1992, "peter": 1988, "mikle": 1993}
print(my_dict)

# Выводим значение по заданному ключу
name = "peter"
print(f"Год рождения {name.title()} - {my_dict[name]}")

# Пытаемся вывести значение из словаря по несуществующему ключу
name = "dmitry"
print(my_dict.get(name, f"Данных о '{name.title()}' нет в словаре!"))

# Добавляем несколько пар в словарь
new_users = {"dmitry": 1977, "ivan": 1979}
my_dict.update(new_users)
print(f"В словарь были добавлены новые данные \n {list(new_users.items())}")

# Удаляем пару из словаря
block_user = "aleksandr"
print (f"Из словаря удалили пару- '{block_user}: {my_dict.pop(block_user)}'")
print(my_dict)

# Создаем множество
my_set = {1,1,1,"Дмитрий","Антон","дмитрий",3,3,5,5,7,7,7,"Дмитрий","Антон",True, True}
print(my_set)

# Добавляем несколько значений во множество
new_number = map(int, input('Введите произвольные числа через запятую'
                            ' для добавления во множество: ').split(',',))
my_set.update(new_number)
print(my_set)

# Удаляем значение из множества
my_set.discard("дмитрий")
print(my_set)