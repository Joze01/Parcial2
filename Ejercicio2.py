#El precio de venta más alto por cada vendedor en cada departamento y tipo de venta.
import pandas as pd
import numpy as np


datos1 = pd.read_csv('Laboratorio2.csv', encoding='latin1', header=0)
df = pd.DataFrame(datos1)
#print(df)
print("Vena mas alta por cada vendedor en cada departamento y por cada tipo")
resultado=df.groupby(['Vendedor','Provincia','Tipo'])['Precio_Venta'].max()


print(resultado)