# Cargar las biblioteca Pandas con el alias 'pd’
# Cargar las biblioteca Matplotlib con el alias ‘plt’
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Leer datos del archivo datos.csv
data = pd.read_csv ("data/datos.csv")

# Vista previa de las primeras 5 líneas de los datos cargados
print(data.head ())
print(data.columns)

# Limpieza de datos
countryMask = data['Entity'] == 'Mexico'
df = data[countryMask][['Year','Prevalence - Mental disorders - Sex: Both - Age: Age-standardized (Percent)']]
df.rename(columns={'Prevalence - Mental disorders - Sex: Both - Age: Age-standardized (Percent)':'Percentage'},inplace=True)
print(df.head())

#Graficamos las variables
fig, ax = plt.subplots(figsize=(14,6))
ax.plot(df['Year'],df['Percentage'],color='brown',marker='o',label='Mexico')

ax.set_title('Share of population with mental health disorders, 1990 to 2019')

## Eje Y
ax.set_ylim(0,13)
ax.set_yticks(np.arange(0,14,2))
vals = ax.get_yticks()/100
ax.set_yticklabels(['{:,.0%}'.format(x) for x in vals])

## Eje X
ax.set_xlim(1989.9,2019.1)
years = np.arange(1990,2020,5).tolist()
years.append(2019)
ax.set_xticks(years)

## Detalles de grafica
ax.grid(linestyle='--',axis='y')
ax.spines[['top','left','right']].set_visible(False)

plt.legend()
plt.show()
