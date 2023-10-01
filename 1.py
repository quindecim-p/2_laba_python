def are_anagrams(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    return sorted(word1) == sorted(word2)


input_word1 = input("Введите первое слово: ")
input_word2 = input("Введите второе слово: ")

if are_anagrams(input_word1, input_word2):
    print("Анаграммы")
else:
    print("Не анаграммы")
