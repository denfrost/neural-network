import numpy as np
import matplotlib.pyplot as plt

# Определим активационную функцию (ступенчатую функцию)
def step_function(x):
    return 1 if x >= 0 else 0

# Класс для однослойного персептрона
class Perceptron:
    def __init__(self, input_size, lr=0.01, epochs=1):
        self.weights = np.zeros(input_size + 1)  # Веса + смещение
        self.lr = lr  # Скорость обучения
        self.epochs = epochs  # Количество эпох

    def predict(self, x):
        z = np.dot(x, self.weights[1:]) + self.weights[0]
        return step_function(z)

    def fit(self, X, d):
        epoch_weights = []  # Для хранения весов после каждой эпохи
        epoch_errors = [] # ощибка результата
        for _ in range(self.epochs):
            for xi, target in zip(X, d):
                prediction = self.predict(xi)
                error = target - prediction
                self.weights[1:] += self.lr * error * xi
                self.weights[0] += self.lr * error
            epoch_weights.append(self.weights.copy())  # Сохраняем веса после каждой эпохи
            epoch_errors.append(error)  # Сохраняем ощибку после каждой эпохи
        return epoch_weights, epoch_errors

# Пример данных для fit
X = np.array([[1, 0, 1],  # Спам
              [0, 1, 0],  # Не спам
              [1, 1, 0],  # Спам
              [0, 0, 1]]) # Не спам

d = np.array([1, 0, 1, 0])  # Целевые значения

# Инициализация и обучение персептрона
perceptron = Perceptron(input_size=3, lr=0.1, epochs=100)
epoch_weights, epoch_errors = perceptron.fit(X, d)

print(f"Начальные веса : {epoch_weights[0]}, fit error [start]: [{epoch_errors[0]}]") #быстрый Анализ конечных весов и изменение ошибки
print(f"Итоговые веса : {epoch_weights[perceptron.epochs-1]}, fit error [end]: {epoch_errors[perceptron.epochs-1]}") #быстрый Анализ конечных весов и изменение ошибки

# Визуализация изменения весов по эпохам
epoch_numbers = range(1, perceptron.epochs + 1)
plt.figure(figsize=(10, 6))
for i in range(len(perceptron.weights) - 1):
    weights_i = [weights[i] for weights in epoch_weights]
    plt.plot(epoch_numbers, weights_i, marker='o', label=f'Weight {i + 1}')

plt.title('Изменение весов персептрона по эпохам')
plt.xlabel('Эпоха')
plt.ylabel('Значение веса')
plt.xticks(epoch_numbers)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Тестирование персептрона на новых данных
new_data = np.array([[1, 0, 0],  # Предсказание для нового сообщения
                     [0, 1, 1]])
for xi in new_data:
    print(f"Входные данные: {xi}, Предсказание: {perceptron.predict(xi)}")

# Проверка персептрона на старых данных
old_data = np.array([[1, 0, 1],  # Проверка для теста спама
                     [1, 1, 0]])
for xi in old_data:
    print(f"Проверочные данные: {xi}, Предсказание: {perceptron.predict(xi)}")