import random
import matplotlib.pyplot as plt

random.seed(0)

n=100 # Number of data pts.

theta = [0.1,0.2] # Parameters of the true model.

xs = [random.random() for _ in range(n)]
ys = [theta[0] + theta[1]*x + random.gauss(0,0.02) for x in xs]

print(xs, ys)

x_model = [0,1]
y_model = [theta[0] + theta[1]*x for x in x_model]

plt.plot(xs,ys,'b.')
plt.plot(x_model,y_model,'r-')
plt.show()