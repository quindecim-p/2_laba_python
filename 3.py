def max_element(matrix):
    if not matrix:
        return None

    max_value = matrix[0][0]
    max_row = 0
    max_col = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > max_value:
                max_value = matrix[row][col]
                max_row = row
                max_col = col

    return max_row, max_col


new_matrix = [
    [5, 2, 4],
    [1, 7, 9],
    [3, 8, 0]
]

result = max_element(new_matrix)

if result:
    print("Индекс строки:", result[0], "\nИндекс столбца:", result[1])
else:
    print("Матрица пустая.")
