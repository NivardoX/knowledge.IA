import numpy as np
import matplotlib.pyplot as plt
import tkinter

from decimal import *
LEARNINGRATE = 0.05


"""amostras = np.array([
            [1, 1, 1],
            [1, 0, 1],
            [0, 1, 1],
            [0, 0, 1]])
"""
amostras = np.array([[2.7810836		,2.550537003	,1],
                    [1.465489372	,	2.362125076	,1],
                    [3.396561688	,	4.400293529	,1],
                    [1.38807019	,	1.850220317		,1],
                    [3.06407232	,	3.005305973		,1],
                    [7.627531214,		2.759262235	,1],
                    [5.332441248,		2.088626775	,1],
                    [6.922596716,		1.77106367	,1],
                    [8.675418651,		-0.242068655,1],
                    [7.673756466,		3.508563011	,	1]])
[tamColuna, tamLinha] = np.shape(amostras)


"""
esperado = [1,1,1, 0]
"""

esperado = [0,0,0,0,0,1,1,1,1,1]
pesos = [np.random.uniform(-1,1),np.random.uniform(-1,1),0]

epocas = 0

#print(amostras)
def ativiv(soma):
    if soma >= 0:
        return 1
    else:
        return 0

acertos = 0
while acertos != tamColuna:
    #print("Epoca {}".format(epocas))
    acertos = 0
    for x in range(tamColuna):

        soma = sum(np.multiply(amostras[x],pesos))

        predict = ativiv(soma)
        e = esperado[x] - predict
        if e == 0:
            #print("Acertou")
            acertos += 1
        else:
            acertos = 0
            pesos[-1] += e * LEARNINGRATE
            for y in range(tamLinha - 1):
                #  print(y)

                pesos[y] += e * LEARNINGRATE * amostras[x][y]
    #print(acertos)
    #print("\n")

    epocas += 1

print(epocas)
def testar(a, b):
    c = [a, b, 1]
    #print(c)
    #print(pesos)
    print(ativiv(sum(np.multiply(c,pesos))))


"""
testar(0,0,)
testar(0,1)
testar(1,0)
testar(1,1)
"""
testar(2.7810836,2.550537003)
testar(1.465489372,2.362125076)
testar(7.673756466,3.508563011)

plt.scatter(amostras[:,0],amostras[:,1],c=esperado)
plt.title("Setosa x versicolor" )
plt.xlabel('Sepal.Width')
plt.ylabel('Sepal.Length')

#plt.plot(amostras[:, 0], amostras[:, 1], 'ro')
#plt.axis([-5, 10, -5,10])
plt.show()
