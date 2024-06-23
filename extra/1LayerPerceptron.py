import numpy as np


# Определим активационную функцию (например, ступенчатую функцию)
def step_function(x):
    return np.where(x >= 0, 1, 0)


# Класс для однослойного персептрона
class Perceptron:
    def __init__(self, input_size, lr=0.01, epochs=100):
        self.W = np.zeros(input_size + 1)
        self.lr = lr
        self.epochs = epochs

    def predict(self, x):
        z = self.W.T.dot(x)
        return step_function(z)

    def fit(self, X, d):
        X = np.insert(X, 0, 1, axis=1)  # добавляем единицу для смещения
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                x = X[i]
                y = self.predict(x)
                e = d[i] - y
                self.W = self.W + self.lr * e * x


# Пример использования
if __name__ == "__main__":
    # Входные данные (X) и целевые значения (d)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    d = np.array([0, 0, 0, 1])  # логическое И (AND)

    # Создаем и обучаем персептрон
    perceptron = Perceptron(input_size=2)
    perceptron.fit(X, d)

    # Тестируем персептрон
    print(perceptron.predict(np.array([1, 1, 1])))  # Output: 1
    print(perceptron.predict(np.array([1, 0, 0])))  # Output: 0