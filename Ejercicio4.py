#Represente en un gráfico de pastel las proporciones de cada tipo de venta realizada respecto a
# los montos pagados por los clientes en 2007.


import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


datos1 = pd.read_csv('Laboratorio2.csv', encoding='latin1', header=0)
df = pd.DataFrame(datos1)

df['Fecha_Alta']=pd.to_datetime(df['Fecha_Alta'])
start_date=pd.to_datetime("31-12-06")
end_date=pd.to_datetime("01-01-08")


mask = (df['Fecha_Alta'] > start_date) & (df['Fecha_Alta'] < end_date)
df = df.loc[mask]

#print(df)


frameLocal=df['Tipo'].groupby(df['Tipo']).count().reset_index(name='Cantidad').sort_values(['Cantidad'], ascending=False)

totales=frameLocal['Cantidad'].sum()
frameLocal['Cantidad']=(frameLocal['Cantidad']/totales)*100
print(frameLocal)

print(totales)
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = frameLocal['Tipo']
sizes = frameLocal['Cantidad']

fig1, ax1 = plt.subplots()
ax1.pie(sizes,  labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()