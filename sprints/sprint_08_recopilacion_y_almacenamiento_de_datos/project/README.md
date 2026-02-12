# $\textcolor{blue}{Sprint\ 8\ -\ Recopilación\ y\ almacenamiento\ de\ datos\ (SQL)}$
### Descripción del proyecto

Paso 4. Análisis exploratorio de datos (Python)

Además de los datos que recuperaste en las tareas anteriores te han dado un segundo archivo. Ahora tienes estos dos CSV:

/datasets/project_sql_result_01.csv

contiene los siguientes datos:

- company_name: nombre de la empresa de taxis

- trips_amount: el número de viajes de cada compañía de taxis el 15 y 16 de noviembre de 2017. 

/datasets/project_sql_result_04.csv 

contiene los siguientes datos:

- dropoff_location_name: barrios de Chicago donde finalizaron los viajes

- average_trips: el promedio de viajes que terminaron en cada barrio en noviembre de 2017.

 Para estos dos datasets ahora necesitas

- importar los archivos
- estudiar los datos que contienen
- asegurarte de que los tipos de datos sean correctos
- identificar los 10 principales barrios en términos de finalización del recorrido
- hacer gráficos: empresas de taxis y número de viajes, los 10 barrios principales por número de finalizaciones
- sacar conclusiones basadas en cada gráfico y explicar los resultados

Paso 5. Prueba de hipótesis (Python)

/datasets/project_sql_result_07.csv — el resultado de la última consulta. Contiene datos sobre viajes desde el Loop hasta el Aeropuerto Internacional O'Hare. Recuerda, estos son los valores de campo de la tabla:

- start_ts: fecha y hora de la recogida
- weather_conditions: condiciones climáticas en el momento en el que comenzó el viaje
- duration_seconds: duración del viaje en segundos

Prueba la hipótesis:

"La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos".

Decide por tu cuenta dónde establecer el nivel de significación (alfa).

Explica:

Cómo planteaste las hipótesis nula y alternativa,
qué criterio usaste para probar las hipótesis y por qué.

# $\textcolor{blue}{Sprint\ 8\ -\ Data\ Collection\ and\ Storage\ (SQL)}$
### Project Description

Step 4. Exploratory Data Analysis (Python)

In addition to the data you retrieved in the previous tasks, you have been given a second file. You now have these two CSV files:

/datasets/project_sql_result_01.csv

It contains the following data:

- company_name: name of the taxi company
- trips_amount: number of trips for each taxi company on November 15 and 16, 2017

/datasets/project_sql_result_04.csv

It contains the following data:

- dropoff_location_name: Chicago neighborhoods where the trips ended
- average_trips: average number of trips that ended in each neighborhood in November 2017

For these two datasets, you now need to:

- import the files
- study the data they contain
- make sure the data types are correct
- identify the top 10 neighborhoods in terms of trip drop-offs
- create visualizations: taxi companies vs. number of trips, top 10 neighborhoods by number of drop-offs
- draw conclusions based on each graph and explain the results

Step 5. Hypothesis Testing (Python)

/datasets/project_sql_result_07.csv — the result of the last query. It contains data about trips from the Loop to O'Hare International Airport. Recall, these are the table fields:

- start_ts: pickup date and time
- weather_conditions: weather conditions at the moment the trip started
- duration_seconds: trip duration in seconds

Test the hypothesis:

"The average duration of trips from the Loop to O'Hare International Airport changes on rainy Saturdays."

Choose the significance level (alpha) yourself.

Explain:

How you formulated the null and alternative hypotheses

What criterion you used to test the hypotheses and why.

- Install pandas, plotly and streamlit

- Go to the project's folder and execute 'streamlit run app.py'
