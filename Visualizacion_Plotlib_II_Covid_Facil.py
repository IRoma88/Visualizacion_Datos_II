# -*- coding: utf-8 -*-
"""

## **Introducción**

En este proyecto se va a realizar un análisis de datos sencillo de las hospitalizaciones de UCI en España producidas por el Covid 19.

##**Etapas del Análisis de Datos**

1. Importar módulos de Python
2. Obtención de datos
3. Gestión de Datos (Data Wrangling)
4. Análisis exploratorio de datos (EDA) y visualización
5. Conclusiones

## **1. Importar los módulos de Python**

En este proyecto trabajaremos principalmente con tres módulos de Python que ya conocemos:

* Pandas
* matplotlib, concretamente con el paquete pyplot
* Numpy
"""

#Importa los módulos y paquetes necesarios
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""## **2. Obtención de datos**

Para realizar un análisis de datos es necesario obtener dichos datos, siendo a veces el mayor problema. En este caso, el instituto Carlos III ya ha realizado una gran labor obteniendo dichos datos, que puedes [ver y descargar aquí ](https://drive.google.com/file/d/1kbnilQHl3cT8BliwvVRshyP2dicM2Ugy/view?usp=sharing) en formato CSV.

Añade el archivo csv al colab (esto puede tardar unos minutos) y crea el dataframe df con los datos que contiene.

Visualiza las primeras 5 filas para ver la estructura del dataframe.
"""

df = pd.read_csv('/content/casos_covid.csv')
df.head()

"""##**3. Gestión de Datos (Data Wrangling)**

En esta etapa, los datos se ven modificados para que sea más fácil realizar un posterior análisis y visualización. Las modificaciones más comunes que pueden sufrir los datos son limpieza, transformación, combinación y redimensionado.

Antes de realizar cualquier tipo de modificación de los datos, es recomendable analizar sus columnas, valores nulos, número de filas, tipos de datos, etc.
"""

# Columnas del DataFrame
df.shape[1]

# Número de filas y columnas
df.shape

"""Comprueba qué tipo de datos contiene cada columna, y si contiene valores nulos."""

# Tipo de datos por columna
df.dtypes

# Columnas con valores nulos
df.isnull().sum()

"""Crea una lista con los valores únicos de la columna 'provincia_iso'. Estos valores se refieren a las iniciales de las provincias."""

# Valores únicos de la primera columna
valores_unicos = df['provincia_iso'].unique().tolist()
valores_unicos

"""Haz lo mismo para el género."""

# Valores únicos de la segunda columna
sexos = df['sexo'].unique().tolist()
sexos

"""Y para el grupo de edad."""

# Valores únicos de la segunda columna
edades = df['grupo_edad'].unique().tolist()
edades

"""¿De cuantos días contiene datos el dataset?"""

# Valores únicos de la segunda columna
fechas=df['fecha'].unique().tolist()
fechas

"""En cuanto al resto de columnas, no tiene sentido analizarlas de esta forma, pues son valores dados de ingresos, UCIs, muertes y contagios para cada grupo de provincia,sexo, fecha y edad.

Tras analizar los datos, se concluye que no es necesaria realizar ninguna transformación. Esto es debido a que no hay que limpiar, rellenar o imputar datos porque no hay datos vacíos ni nulos ni duplicados en ninguna de las columnas. En caso de que existieran, podrían interferir en el análisis y habría que tener diferentes estrategias según la cantidad y el tipo de datos.

##**4. Análisis Exploratorio de Datos (EDA) y Visualización**

Una vez se ha analizado la estructura de los datos y se ha decidido cómo gestionarlos, el siguiente paso a realizar y el más emocinante es un análisis exploratorio de datos. Antes de realizar esto, es conveniente hacerse algunas preguntas. Algunas preguntas concretas para este caso, partiendo de los datos podrían ser:
* ¿Hay diferencias en los contagios/UCI/muertes entre edad?
* ¿Hay diferencias en los contagios/UCI/muertes entre sexo?
* ¿Hay diferencias en los contagios/UCI/muertes entre provincias?
* ¿Quién tiene más probabilidad de acabar en UCI por género? Y por edad?

Una vez aclarado qué queremos obtener, procedemos a realizar el análisis de datos.

**Evolución de la pandemia**

En este caso, queremos mostrar en una línea temporal, el número de Contagios, Hospitalizaciones, Ingresos UCI y Defunciones totales, es decir la suma de cada provincia, para cada fecha.

Muestra las 4 gráficas en un mismo área unas encima de otras, con un tamaño de gráfico de 10x14.
"""

# Convertir la columna de fecha a formato datetime para facilitar el manejo de fechas
df['fecha'] = pd.to_datetime(df['fecha'])

# Agrupar por fecha y sumar los valores de interés
df_agg = df.groupby('fecha')[['num_casos', 'num_hosp', 'num_uci', 'num_def']].sum()

# Configurar el tamaño del gráfico
fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(10, 14), sharex=True)

# Títulos y etiquetas
titles = ['Número de Contagios', 'Número de Hospitalizaciones', 'Número de Ingresos UCI', 'Número de Defunciones']
columns = ['num_casos', 'num_hosp', 'num_uci', 'num_def']
colors = ['blue', 'orange', 'red', 'black']

# Graficar cada variable en su respectivo subplot
for i, col in enumerate(columns):
    axes[i].plot(df_agg.index, df_agg[col], color=colors[i], label=titles[i])
    axes[i].set_title(titles[i])
    axes[i].set_ylabel('Casos')
    axes[i].legend()
    axes[i].grid(True)

# Etiqueta del eje X
axes[-1].set_xlabel('Fecha')

# Ajustar el diseño
#plt.tight_layout()
plt.show()

"""#Pregunta 1

¿En qué peridodo se produjeron menos contagios?

a) Invierno 2020-2021

b) Primavera 2020

c) Verano 2020

d) Otoño 2020

Almacena la letra de la respuesta correcta en la variable solucion_1.

¿El resto de gráficas muestran la misma tendencia? Responde con un booleano en la variable solucion_1b
"""

solucion_1='b'

solucion_1b=False

"""**Comparación de la evolución de la pandemia en Barcelona y Madrid**

Vuelve a realizar las gráficas de lineas temporales para los contagios, hospitalizaciones, ingresos UCI y defunciones, pero esta vez representa en cada uno, superpuestos los datos de Barcelona y Madrid. Utiliza el parámetro alpha al 0.5.
"""

# Filtrar los datos para Barcelona y Madrid
df_bcn = df[df['provincia_iso'] == 'B']
df_mad = df[df['provincia_iso'] == 'M']

# Agrupar por fecha y sumar los valores de interés para cada provincia
df_bcn_agg = df_bcn.groupby('fecha')[['num_casos', 'num_hosp', 'num_uci', 'num_def']].sum()
df_mad_agg = df_mad.groupby('fecha')[['num_casos', 'num_hosp', 'num_uci', 'num_def']].sum()

# Configurar el tamaño del gráfico
fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(10, 14), sharex=True)

# Títulos y etiquetas
titles = ['Número de Contagios', 'Número de Hospitalizaciones', 'Número de Ingresos UCI', 'Número de Defunciones']
columns = ['num_casos', 'num_hosp', 'num_uci', 'num_def']
colors = ['blue', 'orange', 'red', 'black']

# Graficar cada variable en su respectivo subplot con Barcelona y Madrid superpuestos
for i, col in enumerate(columns):
    axes[i].plot(df_bcn_agg.index, df_bcn_agg[col], color=colors[i], alpha=0.5, label='Barcelona')
    axes[i].plot(df_mad_agg.index, df_mad_agg[col], color=colors[i], linestyle='dashed', alpha=0.5, label='Madrid')
    axes[i].set_title(titles[i])
    axes[i].set_ylabel('Casos')
    axes[i].legend()
    axes[i].grid(True)

# Etiqueta del eje X
axes[-1].set_xlabel('Fecha')

# Ajustar el diseño
plt.tight_layout()
plt.show()

"""Responde con 'Barcelona' o 'Madrid' en la variable solucion_2 cual ha sido la ciudad con mayor pico de hospitalizaciones por el Covid según las conclusiones sacadas de los gráficos.

Responde, en la variable solucion_2b, con 'Barcelona' o 'Madrid' cual ha tenido el mayor pico de contagios.
"""

solucion_2='Madrid'

solucion_2b='Barcelona'

"""**Muertes absolutas por sexo**

Representa con un gráfico de tarta las muertes totales según el género.

Utiliza como etquetas la lista de valores únicos de la columna 'sexo' y como formato de valor del número dentro del gráfico '%.2f%%'.
"""

# Agrupar las muertes totales por sexo
df_sexo = df.groupby('sexo')['num_def'].sum()

# Crear el gráfico de tarta
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(df_sexo, labels=df_sexo.index, autopct='%.2f%%', colors=['blue', 'pink'], startangle=90)

# Título del gráfico
ax.set_title('Muertes Totales por Sexo')

# Mostrar gráfico
plt.show()

"""Completa la cadena de texto de la variable solucion_3 con los datos visualizados en el gráfico (H,M o NC) y (xx.xx%)."""

solucion_3='El género con más defunciones es H con 55,16%' #sustituye las _ por el dato correspondiente

"""**Provincia más afectada**"""

# Filtrar los datos excluyendo Madrid ('M') y Barcelona ('B')
df_sin_mb = df[~df['provincia_iso'].isin(['M', 'B'])]

# Agrupar por provincia y sumar los contagios
provincia_max_contagios = df_sin_mb.groupby('provincia_iso')['num_casos'].sum().idxmax()

"""¿Cuál es la provincia, sin contar Madrid y Barcelona, con más contagios? Almacena en la solucion_3 el valor correspondiente de la columna 'provincia_iso' (Ej. 'M')."""

solucion_4=provincia_max_contagios
solucion_4

"""**Grupo de edad más afectado**"""

grupo_edad_max_uci = str(df.groupby('grupo_edad')['num_uci'].sum().idxmax())
grupo_edad_max_uci

"""¿Qué rango de edad sufrió más ingresos UCI? Almacena en la variable solucion_5 el rango de edad como cadena de texto (ej. '0-9')"""

solucion_5= 60-69

#@title Ejecuta para obtener el token
import hashlib

correct = str(solucion_1)+ str(solucion_2)+ str(solucion_2b)+ str(solucion_3)+ str(solucion_4)+ str(solucion_5)
pwd = hashlib.sha256(str(correct).encode())
#print('El token para corregir es:\n',pwd.hexdigest())

if pwd.hexdigest()[0:6] == '2b9bad':
  print('¡Felicidades! puedes avanzar al siguiente modulo \n El token es: ',pwd.hexdigest())
else:
  print('Hay algún error en el código o tu forma es diferente a la planteada, pregunta por el foro si no lo ves claro.')



