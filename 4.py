file = None

try:
    file = open("example.txt", "r")
    content = file.read()
    number = int(content)
    result = 10 / number

except FileNotFoundError:
    print("Файл не найден.")
except ValueError:
    print("Не удалось преобразовать в число.")
except ZeroDivisionError:
    print("Деление на ноль.")
finally:
    file.close()

print("Программа завершена.")
