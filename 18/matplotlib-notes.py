import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Line Chart
# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.xlabel("Time")
# plt.ylabel("Sine")
# plt.title("Sine over time")
# plt.plot(x,y)
# plt.show()

# Scatterplot
import pandas as pd
A =  pd.read_csv("data_1d.csv", header=None).as_matrix()
x = A[:, 0]
y = A[:, 1]
# plt.scatter(x,y)
# plt.show()

# Histogram
# plt.hist(x)
# plt.show()

# Random histogram
# R = np.random.random(10000)
# plt.hist(R, bins=20)
# plt.show()

# MNIST Digit data
df = pd.read_csv("../../../pML/machine_learning_examples/DATA/train.csv")
print(df.shape)

M = df.as_matrix()

# 1st image
im = M[0, 1:]
print(im.shape)
im = im.reshape(28, 28)

# plt.imshow(im)
# plt.imshow(im, cmap='gray')
plt.imshow(255-im, cmap='gray')
plt.show()
print(M[0,0])
