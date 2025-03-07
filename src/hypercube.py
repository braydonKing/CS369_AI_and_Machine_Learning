def find_shell(d):
    return 1-.8**d

import matplotlib.pyplot as plt
import random

xs = list(range(1,21))

ys = [find_shell(x) for x in xs]

plt.plot(xs,ys)
plt.show()

def random_point(d):
    """
    a random point chosen unifomly form a d-dimensional hypercube
    """
    return [random.random() for _ in range(d)]

def distance(p,q):
    squares = [(p[i] - q[i]) ** 2 for i in range(len(p))]
    return sum(squares)**0.5

print(distance([0,0],[3,4]))

def average_distance(d):
    """
    The average distance between the two points chosen uniformly from a dimensional hypercube.
    """

    distances = distance(random_point(d), (random_point(d) for _ in range(10)))

    return sum(distances)/len(distances)