# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

def ind_item(item):
    for i in range(len(items_list)):
        if items_list[i] == item:
            return i
    else:
        return None
for find_item in ['банан', 'груша', 'персик']:
    index_item = ind_item((find_item))  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
