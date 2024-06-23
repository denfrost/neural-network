import numpy as np


# Определим активационную функцию (например, ступенчатую функцию)
def step_function(x):
    return 1 if x >= 0 else 0


# Класс для однослойного персептрона
class Perceptron:
    def __init__(self, input_size, lr=0.01, epochs=100):
        self.weights = np.zeros(input_size + 1)
        self.lr = lr
        self.epochs = epochs

    def predict(self, x):
        z = np.dot(x, self.weights[1:]) + self.weights[0]
        return step_function(z)

    def fit(self, X, d):
        for _ in range(self.epochs):
            for xi, target in zip(X, d):
                prediction = self.predict(xi)
                error = target - prediction
                self.weights[1:] += self.lr * error * xi
                self.weights[0] += self.lr * error


# Пример использования
if __name__ == "__main__":
    # Входные данные (X) и целевые значения (d)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    d = np.array([0, 0, 0, 1])  # логическое И (AND)

    # Создаем и обучаем персептрон
    perceptron = Perceptron(input_size=2)
    perceptron.fit(X, d)

    # Тестируем персептрон
    for xi in X:
        print(f"Входные данные: {xi}, Предсказание: {perceptron.predict(xi)}")
