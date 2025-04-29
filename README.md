# 🏥 Análisis de Hospitalizaciones en UCI por COVID-19 en España

Este proyecto realiza un análisis exploratorio de los datos de hospitalizaciones en UCI, contagios, defunciones y hospitalizaciones generales causadas por COVID-19 en España. Los datos han sido proporcionados por el Instituto de Salud Carlos III.

---

## 📌 Objetivos

- Analizar la evolución temporal del COVID-19 en España.
- Comparar el impacto del COVID entre provincias, edades y sexos.
- Visualizar tendencias de contagios, ingresos UCI, hospitalizaciones y muertes.
- Identificar los grupos más vulnerables.

---

## 🔍 Etapas del análisis

1. **Importación de módulos**  
   Uso de Pandas, Numpy y Matplotlib.

2. **Obtención de datos**  
   Los datos se obtienen desde un CSV publicado por el Instituto Carlos III.  
   [Acceso al dataset](https://drive.google.com/file/d/1kbnilQHl3cT8BliwvVRshyP2dicM2Ugy/view)

3. **Gestión de datos (Data Wrangling)**  
   - Limpieza y validación de columnas
   - Revisión de nulos y duplicados
   - Conversión de fechas

4. **Análisis Exploratorio de Datos (EDA)**  
   - Evolución diaria de casos, UCI, hospitalizaciones y muertes
   - Comparativa Barcelona vs Madrid
   - Análisis por género, provincia y grupo de edad

5. **Conclusiones**  
   Se obtiene una visión general del comportamiento del virus por fecha, sexo, edad y ubicación geográfica.

---

## 📊 Visualizaciones incluidas

- Series temporales (contagios, UCI, muertes, hospitalizaciones)
- Comparativa entre provincias (Barcelona vs Madrid)
- Gráfico de tarta por género (muertes)
- Análisis de provincias más afectadas (excluyendo Madrid y Barcelona)
- Rango de edad con más ingresos en UCI

---

## 📁 Estructura del proyecto

```markdown
| Archivo                         | Descripción                                   |
|--------------------------------|-----------------------------------------------|
| `analisis_covid_uci.py`        | Script principal con todo el análisis         |
| `casos_covid.csv`              | Dataset de hospitalizaciones UCI en España    |
| `README.md`                    | Documentación del proyecto                    |
| `.gitignore`                   | Archivos ignorados por Git                   |
| `requirements.txt`            | Dependencias del proyecto                     |
````

## ⚙️ Requisitos
Instala los paquetes necesarios con:

````bash
Copiar
Editar
pip install -r requirements.txt
````

## ✅ Resultado esperado
Al finalizar el proyecto obtendrás:

  - Visualizaciones útiles para interpretar el impacto del COVID-19.

  - Conclusiones claras sobre los grupos más afectados.

  - Validación automática mediante un token SHA256.

## 📄 Licencia
Este proyecto se distribuye con fines educativos.

