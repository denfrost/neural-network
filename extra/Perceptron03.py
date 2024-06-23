import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

class Perceptron:
    def __init__(self):
        self.weights = np.random.rand(1)

    def predict(self, x):
        return sigmoid(np.dot(x, self.weights))

    def update_weights(self, x, y):
        self.weights += (y - self.predict(x)) * x

# Установка случайных значений для входных данных
np.random.seed(0)
X = 2 * np.random.rand(100,1)

# Создание модели
model = Perceptron()

# Обучение
for i in range(10000):
    for x,y in zip(X,model.predict(X)):
        model.weights += (y - model.predict(x)) * x

# Проверка
print(model.predict(X))