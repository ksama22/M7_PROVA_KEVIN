import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def hi():
    print("Hi")

def Ex1NotesMitjanes(arxiu):
    # Dropna quita los null
    df = pd.read_csv(arxiu, usecols=["NAME", "NOTES"]).dropna()
    # https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_r.html?highlight=avg
    # Agrupa por notas segun el nombre y hace la media
    df = df.groupby('NAME').agg({'NOTES': 'mean'})
    print(df)
    #Esto crea una grafica con esta array pero no de x e y como deberia
    plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'g-')
    plt.title("MITJA NOTA ALUMNAT CICLE")
    plt.ylabel('ALUMNAT')
    plt.xlabel('NOTES')
    #Muestra el grafico
    plt.show()


def Ex2Faltes(arxiu):
    # Dropna quita los null
    df = pd.read_csv(arxiu, usecols=["NAME", "ABSENCES"]).dropna()
    # https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_r.html?highlight=avg
    # Agrupa por notas segun el nombre y hace la SUMA
    df = df.groupby('NAME').sum({'ABSENCES': 'mean'})
    print(df)
    #Esto crea una grafica con esta array pero no de x e y como deberia
    plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 'g-')
    plt.title("% de faltes DAW2")
    plt.ylabel('FALTES EN %')
    plt.xlabel('Alumnat')
    #plt.legend()
    #Muestra el grafico
    plt.show()
