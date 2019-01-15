import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
#from keras.datasets import mnist
#(xTrain,yTrain),(xTeste,yTeste) = mnist.load_data()




ROWS = 5
COLS = 5

def trainModel():
    n, m = np.array(letras).shape
    LR = 1. / n
    for i in range(m - 1):
        for j in range(i + 1, m):
            weights[i, j] = LR * np.dot(np.array(letras)[:, i], np.array(letras)[:, j])
            weights[j, i] = weights[i, j]

def inputGrid():
    # Set number of rows and columns

    def activivation(x):
        result = []
        for i in x:
            if i == None:
                result.append(1)
            else:
                result.append(-1)

        print(repr(np.array(result)))
        return np.array(result)

    # Create a grid of None to store the references to the tiles
    tiles = np.array([[None for _ in range(COLS)] for _ in range(ROWS)])
    #print(tiles)
    def callback2(event):
        # Get rectangle diameters
        col_width = c.winfo_width() / COLS
        row_height = c.winfo_height() / ROWS
        # Calculate column and row number
        col = event.x // col_width
        row = event.y // row_height
        # If the tile is not filled, create a rectangle
        row, col = int(row), int(col)

        if row >= ROWS:
            row = ROWS - 1
        elif row < 0:
            row = 0
        if col >= COLS:
            col = COLS - 1
        elif col < 0:
            col = 0
        if not tiles[row][col]:
            tiles[row][col] = c.create_rectangle(col * col_width, row * row_height, (col + 1) * col_width,
                                                 (row + 1) * row_height, fill="black")
        # If the tile is filled, delete the rectangle and clear the reference
        else:
            c.delete(tiles[row][col])
            tiles[row][col] = None

    def callback(event):
        # Get rectangle diameters
        col_width = c.winfo_width() / COLS
        row_height = c.winfo_height() / ROWS
        # Calculate column and row number
        col = event.x // col_width
        row = event.y // row_height
        # If the tile is not filled, create a rectangle
        row, col = int(row), int(col)
        if row >= ROWS:
            row = ROWS - 1
        elif row < 0:
            row = 0
        if col >= COLS:
            col = COLS - 1
        elif col < 0:
            col = 0
        if not tiles[row][col]:
            tiles[row][col] = c.create_rectangle(col * col_width, row * row_height, (col + 1) * col_width,
                                                 (row + 1) * row_height, fill="black")
        # If the tile is filled, delete the rectangle and clear the reference
        #else:
        #    c.delete(tiles[row][col])
        #    tiles[row][col] = None

    # Create the window, a canvas and the mouse click event binding

    def sair():
        exit(0)

    def destroy():
        root.focus()
        root.destroy()
        root.quit()


    root = tk.Tk()
    root.title("HOPFIELD NEURAL NETWORK GRID")
    c = tk.Canvas(root, width=80*COLS, height=80*ROWS, borderwidth=2, background='gray')
    c.pack()
    c.bind("<B1-Motion>", callback)
    c.bind("<Button-1>", callback2)

    b = tk.Button(root, text="Enviar", command=destroy)
    b.pack()
    b1 = tk.Button(root, text="Sair", command=sair)
    b1.pack()

    root.mainloop()

    a = activivation(np.reshape(tiles, ROWS * COLS))

    return a

def mainFrame():
    master = tk.Tk()
    master.title("HOPFIELD NEURAL NETWORK")
    master.geometry("350x80")

    def criarModelo():
        if np.array(letras).shape[0] > np.array(letras).shape[1]*0.14:
            tk.messagebox.showinfo("Aviso!", "A quantidade de modelos aprendidos eh maior que a possivel!")
        letras.append(inputGrid())
        trainModel()


    def testarModelo():
        a = np.array(inputGrid())
        predict(a,np.array(letras))
        trainModel()


    b = tk.Button(master, text="Criar Modelo", command=criarModelo,padx=10,pady=10,fg="black", bg="gray",bd = 3)
    b.pack()
    b1 = tk.Button(master, text="Testar Modelo", command=testarModelo,padx=10,pady=10,fg="black", bg="gray",bd = 3)
    b1.pack()

    master.mainloop()

def activivation(x):
    result = []
    for i in x:
        if i < 0:
            result.append(-1)
        else:
            result.append(1)
    return np.array(result)

def predict(inputData,trainingData):

    n, m = trainingData.shape
    outputs = np.zeros(m)
    inputData = inputData.astype(float)

    # recalling
    for itr in range(n):
        for i in np.random.permutation(m):  # asynchronous activation
            outputs[i] = np.dot(weights[i, :], inputData)
            inputData[i] = np.tanh(outputs[i])
    #print(inputData)
    plt.imshow(np.reshape(activivation(inputData), (ROWS, COLS)), interpolation='nearest')
    plt.show()

    return activivation(inputData)

letras = np.array([[1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1.]
                      ],  # Letter D
    dtype=np.float)
n,m = letras.shape
LR = 1./n

weights = np.zeros((m, m))



for i in range(m - 1):
    for j in range(i + 1, m):
        weights[i, j] = LR * np.dot(letras[:, i], letras[:, j])
        weights[j, i] = weights[i, j]


# training


x = np.array(activivation(np.random.uniform(1, -1, ROWS * COLS)),
                      dtype=np.float)

#letras = list(letras)

letras = list(letras)
mainFrame()
