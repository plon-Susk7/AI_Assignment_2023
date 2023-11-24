import numpy as np

X = np.arange(-20, 20, 0.1)
np.random.shuffle(X)
eps = np.random.rand(400) * 10
y = 23 * X + 43 + eps


learning_rate = 0.001
iterations = 100
w = 0
b = 0

for _ in range(iterations):
    y_pred = w * X + b
    dw = 2 * np.mean(X * (y_pred-y))
    db = 2 * np.mean(y_pred-y)
    w -= learning_rate * dw
    b -= learning_rate * db

print(f'w = {w:.2f}, b = {b:.2f}')