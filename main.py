import numpy as np
import matplotlib.pyplot as plt

data = np.array([1000, 1150, 1200, 1350, 2150, 1400, 1450, 1500, 1550, 1560])
n = len(data)

# Вычисляем среднее значение
mean = sum(data) / n

# Вычисляем сумму квадратов отклонений
variance_sum = sum((x - mean) ** 2 for x in data)

# Вычисляем дисперсию
variance = variance_sum / (n - 1)

# Возвращаем стандартное отклонение
variance2 = variance ** 0.5

results = []
for i in range(1, len(data)):
    y_i = data[i]
    y_i_1 = data[i - 1]
    formula_result = abs(y_i - y_i_1) / variance2
    results.append(formula_result)

dover_p = 2


def check_irwin_criteria(values, dover_p):
    outliers = []
    for i in range(len(values)):
        if values[i] >= dover_p:
            outliers.append((i, values[i]))
    return outliers


def adjust_values(values, dover_p):
    adjusted_values = values.copy()
    formatted_original_values = [f"{value:.2f}" for value in adjusted_values]
    print("Оригинальный ряд значений:", formatted_original_values)

    # Сначала проверяем на наличие выбросов
    outliers = check_irwin_criteria(adjusted_values, dover_p)
    for i in range(len(adjusted_values)):
        if adjusted_values[i] >= dover_p:
            if i > 0 and i < len(adjusted_values) - 1:
                adjusted_values[i] = (adjusted_values[i - 1] + adjusted_values[i + 1]) / 2
            elif i == 0:
                adjusted_values[i] = adjusted_values[1]
            else:
                adjusted_values[i] = adjusted_values[-2]

    # Проверяем снова после замены
    outliers_after_adjustment = check_irwin_criteria(adjusted_values, dover_p)

    # Выводим информацию о выбросах до и после замены
    if outliers:
        for index, value in outliers:
            print(f"Есть выбросы, значение: {value:.2f}")
    else:
        print("Ряд удовлетворяет критерию Ирвина до замены.")

    if outliers_after_adjustment:
        print("Есть выбросы после замены:")
        for index, value in outliers_after_adjustment:
            print(f"Индекс: {index}, Значение: {value:.2f}")
    else:
        print("Ряд удовлетворяет критерию Ирвина после замены.")

    return adjusted_values


# Вывод результатов
print()
print(f"Средняя цена = {mean:.2f} рублей")
print(f"Дисперсия: {variance:.2f}")
print(f"Стандартное отклонение: {variance2:.2f}")
print()

# Форматирование значений в списке
adjusted_values = adjust_values(results, dover_p)
formatted_values = [f"{val:.2f}" for val in adjusted_values]
print("Измененные значения:", formatted_values)


def adjust_values(values, dover_p):
    adjusted_values = values.copy()

    # Пример корректировки значений (результаты можно изменить в зависимости от логики)
    for i in range(len(adjusted_values)):
        adjusted_values[i] += dover_p  # Здесь вы можете применить свою логику корректировки

    formatted_original_values = [f"{value:.2f}" for value in adjusted_values]

    return adjusted_values


# Оригинальный ряд значений
original_values = ['0.48', '0.16', '0.48', '2.56', '2.40', '0.16', '0.16', '0.16', '0.03']
# Измененные значения
modified_values = ['0.48', '0.16', '0.48', '1.44', '0.80', '0.16', '0.16', '0.16', '0.03']

# Преобразуем значения в тип float
original_values = list(map(float, original_values))
modified_values = list(map(float, modified_values))

# Индексы значений
indices = range(len(original_values))

# Создаем график
plt.figure(figsize=(10, 5))
plt.plot(indices, original_values, marker='o', label='Оригинальные значения', color='blue')
plt.plot(indices, modified_values, marker='o', label='Измененные значения', color='red')

# Добавляем аннотации для изменения
for i, (original, modified) in enumerate(zip(original_values, modified_values)):
    if original != modified:
        plt.annotate(f'{modified}', (i, modified), textcoords="offset points", xytext=(0,10), ha='center', color='red')

# Настраиваем график
plt.title('Сравнение оригинальных и измененных значений')
plt.xticks(indices)
plt.xlabel('Индексы')
plt.ylabel('Значения')
plt.legend()
plt.grid()

# Показываем график
plt.show()
