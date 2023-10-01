def process_argument(arg):
    if isinstance(arg, tuple):
        return len(arg)
    elif isinstance(arg, list):
        total = 0
        for item in arg:
            if item == 0:
                break
            total += item
        return total
    elif isinstance(arg, int):
        return int(str(arg)[::-1])
    elif isinstance(arg, str):
        words = arg.split()
        num_words = len(words)

        dic = {i: arg.count(i) for i in arg}
        most_common = max(dic, key=dic.get)
        return f"Количество слов в строке: {num_words}, самый часто встречающийся символ - {most_common}"
    else:
        return "Неизвестный тип аргумента."


arg1 = (1, 2, 3, 4, 5)
arg2 = [1, 2, 3, 0, 4, 5]
arg3 = 12345
arg4 = "abracadabra abra"

result1 = process_argument(arg1)
result2 = process_argument(arg2)
result3 = process_argument(arg3)
result4 = process_argument(arg4)

print("Длина кортежа:", result1)
print("Сумма элементов списка до первого 0:", result2)
print("Число наоборот:", result3)
print(result4)
