data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
    "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_strukture_summ(data_structure):

    total_sum = 0
    total_length = 0

    if isinstance(data_structure, (int, float)):
        total_sum += data_structure
    elif isinstance(data_structure, str):
        total_length += len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            sum_item, length_item = calculate_strukture_summ(item)
            total_sum += sum_item
            total_length += length_item
    elif isinstance(data_structure, dict): 
        for value in data_structure.values():
            sum_item, length_item = calculate_strukture_summ(value)
            total_sum += sum_item
            total_length += length_item

    return total_sum, total_length

total_sum, total_length = calculate_strukture_summ(data_structure)
# result = calculate_strukture_summ (data_structure)
# print (result)# вывод (73, 16)
print(f"Сумма чисел: {total_sum}")
print(f"Сумма длин строк: {total_length}")
