# Необходимо разработать метод connect_dicts(dict1, dict2), который соединит два
# переданных словаря, значениями ключей в которых являются числа, и вернет
# новый словарь, полученный по следующим правилам:
# • приоритетными являются ключи того словаря, сумма значений ключей
# которого больше (если суммы значений ключей будут равны, то второй
# словарь считается более приоритетным)
# • ключи со значениями меньше 10 не должны попасть в финальный
# словарь
# • получившийся словарь должен вернуться упорядоченным по значениям
# ключей в порядке возрастания.
# Тесты для примеров и проверки:
# connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }) # =>
# { "c": 11, "b": 12 }
# connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) # =>
# { d: 11, "c": 12, "a": 13 }
# connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }) # =>
# { "c": 11, "b": 12, "a": 15 }
# print(sum({"a": 2, "b": 12}.values))


# dict_1 = {'John': 15, 'Rick': 10, 'Misa': 12}
# dict_2 = {'Bonnie': 18, 'Rick': 20, 'Matt': 16}

# def mergeDictionary(dict_1, dict_2):
#    dict_3 = {**dict_1, **dict_2}
#    for key, value in dict_3.items():
#        if key in dict_1 and key in dict_2:
#                dict_3[key] = [value , dict_1[key]]
#    return dict_3

# dict_3 = mergeDictionary(dict_1, dict_2)
# print(dict_3)
# Output  {'John': 15, 'Rick': [20, 10], 'Misa': 12, 'Bonnie': 18, 'Matt': 16}


def connect_dicts(dict1: dict, dict2: dict):  # Нежен рефакторинг

    d1 = {}
    d2 = {}
    total = 0

    for key, value in dict1.items():
        if value >= 10:
            d1[key] = value
        total += value

    for key, value in dict2.items():
        if value >= 10:
            d2[key] = value
        total -= value

    return (
        dict(sorted({**d1, **d2}.items(), key=lambda items: items[1]))
        if total <= 0
        else dict(sorted({**d2, **d1}.items(), key=lambda items: items[1]))
    )


# print(
#     connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5})
# )  # =>{ "c": 11, "b": 12 }
# print(
#     connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15})
# )  # =>{ d: 11, "c": 12, "a": 13 }
# print(
#     connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15})
# )  # =>{ "c": 11, "b": 12, "a": 15 }

