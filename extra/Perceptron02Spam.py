import numpy as np

# Определим активационную функцию (например, ступенчатую функцию)
def step_function(x):
    return 1 if x >= 0 else 0

# Класс для однослойного персептрона
class Perceptron:
    def __init__(self, input_size, lr=0.01, epochs=1):
        self.weights = np.zeros(input_size + 1) # задает массив с нулями для shape и type
        self.lr = lr #скорость обучения сети
        self.epochs = epochs #количество эпох или итераций
    def predict(self, x): #Функция предсказания
        z = np.dot(x, self.weights[1:]) + self.weights[0] #вычисляет взвешенную сумму входных данных
        return step_function(z) #применяет к ней активационную функцию.

    def fit(self, X, d): #Обучение сети Функция обучения, которая корректирует веса на основе ошибки предсказания и целевых значений.
        for _ in range(self.epochs):
            for xi, target in zip(X, d):
                prediction = self.predict(xi) #вычисление предсказания
                error = target - prediction #ошибка между целевым значением и предсказанием
                self.weights[1:] += self.lr * error * xi #корректирует веса без учета смещения - [первого элемента массива] корректируется для всех весов, связанных с входными данными
                self.weights[0] += self.lr * error # корректируется отдельно как смещение. только [первого элемента массива]
                print(f"Веса : {self.weights[0]} , {self.weights[1:]}" )
                #print(f"Веса {self.weights[1:]} : {xi}, Ошибка: {error} Предсказание: {prediction}")

# Пример Train данных: каждая строка - это сообщение, каждый столбец - наличие определенного слова
X = np.array([[1, 0, 1],  # Спам: слово1 есть, слово2 нет, слово3 есть
              [0, 1, 0],  # Не спам: слово1 нет, слово2 есть, слово3 нет
              [1, 1, 0],  # Спам: слово1 есть, слово2 есть, слово3 нет
              [0, 0, 1]]) # Не спам: слово1 нет, слово2 нет, слово3 есть

d = np.array([1, 0, 1, 0])  # Целевые значения: 1 - спам, 0 - не спам

# Инициализация и обучение персептрона
perceptron = Perceptron(input_size=3, lr=0.1, epochs=10)
perceptron.fit(X, d)

# Тестирование персептрона на новых данных
new_data = np.array([[1, 0, 0],  # Предсказание для нового сообщения
                     [0, 1, 1]])
for xi in new_data:
    print(f"Входные данные: {xi}, Предсказание: {perceptron.predict(xi)}")

# Тестирование персептрона на новых данных
CheckOld_data = np.array([[1, 0, 1],  # Проверка для теста Спам сообщений
                          [1, 1, 0]])

for xi in CheckOld_data:
    print(f"Проверка старых Входные данные: {xi}, Предсказание: {perceptron.predict(xi)}")
