#Cual es el promedio de ventas y promedio de superficie vendida por cada vendedor.
import pandas as pd
import numpy as np


datos1 = pd.read_csv('Laboratorio2.csv', encoding='latin1', header=0)
df = pd.DataFrame(datos1)
#print(df)

Promedio_Ventas=df.groupby(['Vendedor'])['Precio_Venta'].mean()
Promedio_Superficie=df.groupby(['Vendedor'])['Precio_Venta'].mean()

#print
print("Promedios de ventas por vendedores:")
print(Promedio_Ventas)

print("Promedios de Superficies Vendidas:")
print(Promedio_Superficie)