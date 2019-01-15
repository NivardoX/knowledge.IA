import pandas as pd
import numpy as np
from numpy import genfromtxt
import random
import copy
import tkinter
import matplotlib.pyplot as plt

LR = 0.5


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def targetGroups(target, config):
    targetMlp = []
    for i in range(len(target)):
        targetMlp.append(np.zeros((config[-1], 1)))

    # print(targetMlp)
    for i in range(len(target)):
        targetMlp[i][target[i]] = 1

    ''' for i in range(len(target)):
         targetMlp[0] = np.reshape(targetMlp[0],(1,2))
     '''

    return targetMlp


def criarMatrizes(config):
    weights = []
    biases = []

    for i in range(len(config) - 1):
        weights.append(np.random.random((config[i + 1], config[i])))

    for i in range(len(config) - 1):
        biases.append(np.random.random((config[i + 1], 1)))

    return weights, biases


def feedForward(weights, amostra, config):
    outs = []
    for i in range(len(config) - 1):
        outs.append(np.zeros((config[i], 1)))

    for i in range(len(config) - 1):
        # print(weights[i])
        # print(amostra)
        x = np.dot(weights[i], amostra)
        print(x)
        print(biases[i])
        x = np.add(x, biases[i])
        x = sigmoid(x)

        # print(x)
        amostra = x
        # print(amostra)
        outs[i] = x
        wait = input("Press any key")

    return outs


def printOuts(config, outs):
    for i in range(len(config) - 1):
        print(outs[i])
        print("")


def derivadaOut(config, target, outs):
    matrizDerividasOutput = []
    # Derivar a camada -

    matrizDerividasOutput.append(np.zeros((config[-1], config[-2])))
    # print(matrizDerividasOutput)
    # printOuts(config,outs)

    count = 0
    # printOuts(config,outs)
    for i in range(config[-2]):
        j = 0
        for j in range(config[-1]):
            count = count + 1
            # print(count)
            # print(outs[-(i + 1)][j])
            # print(i,',',j)
            # print(outs[-1][j])
            derivada = LR * (target[i] - outs[-(i + 1)][j]) * outs[-(i + 1)][j] * (outs[-(i + 1)][j])

            # print("saiu")

    matrizDerividasOutput[i][j] = derivada

    print(matrizDerividasOutput)


# def derivarHidden:
# derivar camadas 0 - -1

config = [2, 3, 2]

amostras = np.matrix([[0, 0],
                      [0, 1],
                      [1, 0],
                      [1, 1]])

amostras = np.transpose(amostras)
target = np.array([0, 1, 1, 0])

target = targetGroups(target, config)

# print(target)

weights, biases = criarMatrizes(config)
# print(biases)
# print("\n")

# print(weights[-1])
outs = feedForward(weights, amostras[:, 0], config)
# print(outs)

# print(weights)

derivadaOut(config, target, outs)

# printOuts(config,outs)


# derivadaOut(config)
# target[j] = np.reshape(target[j], (config[-1], 1))
