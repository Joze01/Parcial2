#Grafique el comportamiento para los años 2005 y 2006 de las ventas para oficina y parqueo
# (cuantos se hacen por año por cada vendedor, use la fecha de alta)
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


datos1 = pd.read_csv('Laboratorio2.csv', encoding='latin1', header=0)
df = pd.DataFrame(datos1)

#SET SHOW ALL DF
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)



#print(df)
vendedores=df.groupby(['Tipo','Vendedor'])['Precio_Venta'].count().reset_index(name='Ventas_Realizadas').sort_values(['Tipo','Ventas_Realizadas'], ascending=False)


print("El vendedor con mas ventas realizadas es: ")

print(vendedores.groupby('Tipo').nth(0))
