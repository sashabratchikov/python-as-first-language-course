# Есть два набора данных в виде словарей

data1 = {
	'name': 'James',
	'birth': 1882,
	'death': 1941,
	'books': ['Ulysses', 'A Portrait of the Artist as a Young Man', 'Dubliners']
}

data2 = {
	'second_name': 'Joyce',
	'born_at': 'Dublin',
	'die_at': 'Zurich'
}

# Нужно написать функцию под названием assign, принимающую 2 аргумента - словаря
# Результатом работы будет новый словарь, в котором будут все ключи и их значения из обоих аргументов
#  эта функция совмещает два словаря превращая их в один
# 
# Например:
#   assign({'a': 10}, {'b': 20}) 
# Должна вернуть словарь:
#   {'a': 10, 'b': 20}
#  
# Подсказки
#   1) просматривать ключи словаря можно внутри цикла for ... in ...
#   for key in {'first_key': 10, 'second_key': 20}:
#       <здесь key - будет по-очереди каждым ключем словаря, т.е. сначала first_key, потом second_key
# 
#   2) Получить значение по ключу в словаре можно с помощью синтаксика квадратных скобок
#       dictionary = {'key_name': 333}
#       print(dictionary['key_name'])
#       >>> 333

def assign(dict1, dict2):
	pass
