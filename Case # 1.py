def sum_neg_between_max_min(arr):
    n = len(arr)
    if n < 3:
        return 0  # между элементами ничего нет
    
    # Индексы максимального и минимального элементов
    idx_max = arr.index(max(arr))
    idx_min = arr.index(min(arr))
    
    # Упорядочиваем границы (между ними — независимо от порядка)
    left, right = min(idx_max, idx_min), max(idx_max, idx_min)
    
    # Суммируем отрицательные элементы строго между границами
    total = sum(x for x in arr[left + 1:right] if x < 0)
    return total


# Пример
A = [5, -3, 2, -7, 8, -1, -4, 6]
print("Массив:", A)
print("Максимум:", max(A), "— индекс", A.index(max(A)))
print("Минимум:", min(A), "— индекс", A.index(min(A)))
print("Сумма отрицательных между ними:", sum_neg_between_max_min(A))