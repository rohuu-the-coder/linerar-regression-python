# Training data: hours studied -> marks obtained
x = [1, 2, 3, 4, 5]
y = [20, 40, 60, 80, 100]
m = len(x)

# Initial parameters
w = 0
b = 0
learning_rate = 0.01
epochs = 1000

# Training with gradient descent
for epoch in range(epochs):
    dw = 0
    db = 0

    for i in range(m):
        prediction = w * x[i] + b
        error = prediction - y[i]
        dw += error * x[i]
        db += error

    dw = dw / m
    db = db / m

    w = w - learning_rate * dw
    b = b - learning_rate * db

# Print results after training
print("weight (w):", round(w, 2))
print("bias (b):", round(b, 2))

print("\npredictions:")
for hours in x:
    predicted_marks = w * hours + b
    print(hours, "hours ->", round(predicted_marks, 2), "marks")