import numpy as np
import matplotlib.pyplot as plt


def shuffle_in_unison(a, b):
    if len(a) == len(b):
        x = np.random.permutation(len(a))
        a = a[x]
        b = b[x]
        return a, b
    else:
        print("Both arrays must have the same size")


def divide1(a, p):
    a = np.array(a)
    if p > 1:
        p = p / 100

    tam = len(a)
    small_int = int(tam * p)
    big_int = tam - small_int

    a_big = a[:big_int]
    a_small = a[big_int:]

    return a_big, a_small


def divide2(a, b, p):
    if len(b) != len(a):
        print("Both arrays must have the same size")
        return 0
    a = np.array(a)
    b = np.array(b)
    if p > 1:
        p = p / 100
    if p > 0.5:
        p = 1 - p

    tam = len(a)
    small_int = int(tam * p)
    big_int = tam - small_int

    a_big = a[:big_int]
    a_small = a[big_int:]

    b_big = b[:big_int]
    b_small = b[big_int:]

    return a_big, a_small, b_big, b_small


def normalize(b):
    a = np.array(b, dtype=float)
    for i in range(len(a)):
        a[i] = np.array(a[i], dtype=float)
        maior = a[i].max()
        menor = a[i].min()
        for j in range(len(a[i])):
            a[i][j] = ((a[i][j] - menor) / (maior - menor))

    return a


def complete_prep(x, y, p):
    x1 = normalize(x)
    y1 = y
    x1, y1 = shuffle_in_unison(x1, y1)
    return divide2(x1, y1, p)


def plot_pontos(x, y):
    x = np.array(x)
    y = np.array(y)
    colors = np.array(['m', 'c', 'y', 'r', 'g', 'b'])
    plt.scatter(x[:, 0], x[:, 1], c=colors[y])
    plt.show()


def k_to_oneofk(x):
    x = np.array(x)
    tam = len(x)
    cls = []
    for i in range(len(x)):
        if x[i] in cls:
            pass
        else:
            cls.append(x[i])
    cls.sort()
    y = np.zeros((tam, len(cls)))

    for i in range(len(x)):
        y[i][cls.index(x[i])] = 1

    return y


def oneofk_to_k(x):
    x = np.array(x)
    y = []
    for i in range(len(x)):
        y.append(x[i].index(1))

    return y
