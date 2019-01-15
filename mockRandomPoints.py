
import numpy as np


x = (x for x in range(1,7))
y = (x for x in range(1,7))


def criaPontos(n, x, y):
    if len(x) != len(y):
        exit(0)
    pontos = np.zeros((n, len(x)))
    for i in range(n):
        for j in range(len(x)):
            pontos[i, j] = x[j] + np.random.uniform(-y[j], y[j])

    return pontos


pontos = criaPontos(10, x, y)


def toCSV(pontos, target=None):
    f = open("mock.csv", "w+")

    for i in range(len(pontos)):
        for j in range(len(x)):
            if j == len(x) - 1:
                if target != None:
                    f.write(str('{:.5f}'.format(pontos[i][j])) + ',' + str(target[i]) + '\n')
                else:
                    f.write(str('{:.5f}'.format(pontos[i][j])) + '\n')
            else:

                f.write(str('{:.5f}'.format(pontos[i][j])) + ',')


toCSV(pontos, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(pontos)
