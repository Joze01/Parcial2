#Grafique el comportamiento para los años 2005 y 2006 de las ventas para oficina y parqueo
# (cuantos se hacen por año por cada vendedor, use la fecha de alta)
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


datos1 = pd.read_csv('Laboratorio2.csv', encoding='latin1', header=0)
df = pd.DataFrame(datos1)
df['Fecha_Alta']=pd.to_datetime(df['Fecha_Alta'])
start_date=pd.to_datetime("31-12-04")
end_date=pd.to_datetime("01-01-07")


mask = (df['Fecha_Alta'] > start_date) & (df['Fecha_Alta'] < end_date)
df = df.loc[mask]

mask=((df['Tipo']=='Parqueo') | (df['Tipo']=='Oficina'))
df = df.loc[mask]


vendedores=df['Vendedor'].groupby(df['Vendedor']).count().reset_index(name='Ventas_Realizadas')



#SET SHOW ALL DF
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


gra = plt.figure("Comportamiento 2005-2006")

axes=plt.gca()
#axes.set_ylim([200,200])
Ejey = vendedores['Vendedor']
Ejex = vendedores['Ventas_Realizadas']

plt.plot(Ejey,Ejex)
plt.show()



