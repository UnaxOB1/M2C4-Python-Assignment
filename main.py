from decimal import Decimal
import math

#1
python_list = ['Yellow', 'Germany', 'Apple', 'Cat', 'Pepper']

python_tuple = (2.50, 48, [1, 2, 3], 'Orange', 'A long string')

python_float = 59.99

python_integer = 101

python_decimal = Decimal(25.33)

python_dictionary = {'name': 'Chris', 'age': 30, 'password': 5633}

#2
print(math.ceil(python_float))

#3
print(math.sqrt(python_float))

#4
first_element = python_dictionary['name']
print(first_element)

#5
second_element = python_tuple[1]
print(second_element)

#6
python_list.append('Last element')
print(python_list)

#7
python_list[0] = 'Red'
print(python_list)

#8
sorted_list = sorted(python_list)
print(sorted_list)

#9
python_tuple += ('More content', )
print(python_tuple)
