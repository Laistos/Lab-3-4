# # task 1.1
# try:
#    word = str(input())
#    letter_list = ()
# 
#    for char in word:
#       if char == ' ':
#          continue
#       letter_list += (char,)
# 
#    print(letter_list)
# except ValueError:
#    print('error')

# # task 1.2
# try:
#    letters = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')
#    result = ''.join(letters)
#    print(result)
# except ValueError:
#    print('error')

# # task 1.3
# try:
#    first_list = str(input('tuple_A: '))
#    second_list = str(input('tuple_B: '))
#    len_first = len(first_list)
#    len_second = len(second_list)
#    mid_index_fisrt = len_first // 2
#    mid_index_second = len_second // 2
#    result = first_list[:mid_index_fisrt] + second_list[mid_index_second:]
#    print(result)
# except ValueError:
#    print('error')

# #task 1.4
# try:
#    list = input()
#    splitted_list = list.split(',')
#    list_counter = []
#    repeated_element = []

#    for element_list in splitted_list:
#       if element_list == ' ':
#          continue
#       if element_list not in repeated_element:
#          count = splitted_list.count(element_list)
#          repeated_element.append(element_list)
#          list_counter.append((element_list, count))

#    result = tuple(list_counter)
#    print(result)
# except ValueError:
#    print('error')

# #task 1.5
# try:
#    list = input()
#    splitted_list = list.split(',')

#    integer = []
#    floats = []
#    string = []

#    for item in splitted_list:
#       item = item.strip()
#       if item.isnumeric():
#          integer.append(int(item))
#       elif item.replace('.', '', 1).isdigit():
#          floats.append(float(item))
#       else:
#          string.append(item)
# 
#    print(integer)
#    print(floats)
#    print(string)
# except ValueError:
#    print('error')

# #task 2.1
# try:
#    word = str(input())
#    letter_list = set()
#    repeated_char = []
#    for char in word:
#       if char == ' ':
#          continue
#       if char not in letter_list:
#          repeated_char.append(char)
#          letter_list.add(char)
# 
#    print(repeated_char)
# except ValueError:
#    print('error')

# #task 2.2
# try:
#    set_A = input("set A: ")
#    set_B = input("set B: ")

#    splitted_A = set(set_A.split(','))
#    splitted_B = set(set_B.split(','))

#    difference_set = sorted(splitted_A.symmetric_difference(splitted_B))
#    print("The difference set is:", difference_set)

# except ValueError:
#    print('error')

# # task 2.3
# try:
#    entered_set_A = input()
#    entered_set_B = input()

#    set_A = entered_set_A.split(',')
#    set_B = entered_set_B.split(',')

#    for element in set_B:
#       if element in set_A:
#          set_A.remove(element)

#    print(set_A)
# except ValueError:
#    print('error')

# # task 2.4
# try:
#    entered_set_A = input('set_A: ')
#    entered_set_B = input('set_B: ')
#    entered_set_C = input('set_C: ')

#    set_A = entered_set_A.split(',')
#    set_B = entered_set_B.split(',')
#    set_C = set(entered_set_C.split(','))

#    for element in set_B:
#       if element in set_A:
#          set_A.remove(element)
#          set_C.add(element)

#    print(set_C)
# except ValueError:
#    print('error')

# # task 2.5
# try:
#    import itertools
#    import random

#    entered_set_A = input('set_A: ')
#    n = int(input())
#    m = int(input())

#    set_A = entered_set_A.split(',')

#    combinations = list(itertools.combinations(set_A, n))

#    m = min(m, len(combinations))

#    selected_combinations = random.sample(combinations, m)

#    print(selected_combinations)
# except ValueError:
#    print('error')

# # task 3
# try:
#    from itertools import groupby

#    cars_list = []

#    while True:
#       manufacturer = input("manufacturer (type 'stop' to finish): ")
#       if manufacturer.lower() == 'stop':
#          break
#       model = input("model: ")
#       cars_list.append((manufacturer, model))

#    cars_list.sort(key=lambda x: x[0])

#    for manufacturer, group in groupby(cars_list, key=lambda x: x[0]):
#       models = list(model for _, model in group)
#       print(f'{manufacturer} {len(models)}')
#       for model in models:
#          print(f'- {model}')

# except ValueError:
#    print('error')