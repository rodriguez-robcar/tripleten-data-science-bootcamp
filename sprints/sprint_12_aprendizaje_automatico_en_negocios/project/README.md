# $\textcolor{blue}{Sprint\ 12\ -\ Aprendizaje\ automático\ en\ negocios}$
### Descripción del proyecto

Trabajas en la compañía de extracción de petróleo OilyGiant. Tu tarea es encontrar los mejores lugares donde abrir 200 pozos nuevos de petróleo.

Para completar esta tarea, tendrás que realizar los siguientes pasos:

- Leer los archivos con los parámetros recogidos de pozos petrolíferos en la región seleccionada: calidad de crudo y volumen de reservas.
- Crear un modelo para predecir el volumen de reservas en pozos nuevos.
- Elegir los pozos petrolíferos que tienen los valores estimados más altos.
- Elegir la región con el beneficio total más alto para los pozos petrolíferos seleccionados.
- Tienes datos sobre muestras de crudo de tres regiones. Ya se conocen los parámetros de cada pozo petrolero de la región. Crea un modelo que ayude a elegir la región con el mayor margen de beneficio. Analiza los beneficios y riesgos potenciales utilizando la técnica bootstrapping.

Condiciones:

- Solo se debe usar la regresión lineal para el entrenamiento del modelo.
- Al explorar la región, se lleva a cabo un estudio de 500 puntos con la selección de los mejores 200 puntos para el cálculo del beneficio.
- El presupuesto para el desarrollo de 200 pozos petroleros es de 100 millones de dólares.
- Un barril de materias primas genera 4.5 USD de ingresos. El ingreso de una unidad de producto es de 4500 dólares (el volumen de reservas está expresado en miles de barriles).
- Después de la evaluación de riesgo, mantén solo las regiones con riesgo de pérdidas inferior al 2.5%. De las que se ajustan a los criterios, se debe seleccionar la región con el beneficio promedio más alto.

Los datos son sintéticos: los detalles del contrato y las características del pozo no se publican.

Descripción de datos

Los datos de exploración geológica de las tres regiones se almacenan en archivos:

- /datasets/geo_data_0.csv.
- /datasets/geo_data_1.csv.
- /datasets/geo_data_2.csv.
- id — identificador único de pozo de petróleo
- f0, f1, f2 — tres características de los puntos (su significado específico no es importante, pero las características en sí son significativas)
- product — volumen de reservas en el pozo de petróleo (miles de barriles).

Instrucciones del proyecto

1. Descarga y prepara los datos. Explica el procedimiento.

2. Entrena y prueba el modelo para cada región en geo_data_0.csv:
    1. Divide los datos en un conjunto de entrenamiento y un conjunto de validación en una proporción de 75:25
    2. Entrena el modelo y haz predicciones para el conjunto de validación.
    3. Guarda las predicciones y las respuestas correctas para el conjunto de validación.
    4. Muestra el volumen medio de reservas predicho y RMSE del modelo.
    5. Analiza los resultados.
    6. Coloca todos los pasos previos en funciones, realiza y ejecuta los pasos 2.1-2.5 para los archivos 'geo_data_1.csv' y 'geo_data_2.csv'.

3. Prepárate para el cálculo de ganancias:
    1. Almacena todos los valores necesarios para los cálculos en variables separadas.
    2. Dada la inversión de 100 millones por 200 pozos petrolíferos, de media un pozo petrolífero debe producir al menos un valor de 500,000 dólares en unidades para evitar pérdidas (esto es equivalente a 111.1 unidades). Compara esta cantidad con la cantidad media de reservas en cada región.
    3. Presenta conclusiones sobre cómo preparar el paso para calcular el beneficio.

4. Escribe una función para calcular la ganancia de un conjunto de pozos de petróleo seleccionados y modela las predicciones:
    1. Elige los 200 pozos con los valores de predicción más altos de cada una de las 3 regiones (es decir, archivos 'csv').
    2. Resume el volumen objetivo de reservas según dichas predicciones. Almacena las predicciones para los 200 pozos para cada una de las 3 regiones.
    3. Calcula la ganancia potencial de los 200 pozos principales por región. Presenta tus conclusiones: propón una región para el desarrollo de pozos petrolíferos y justifica tu elección.

5. Calcula riesgos y ganancias para cada región:
    1. Utilizando las predicciones que almacenaste en el paso 4.2, emplea la técnica del bootstrapping con 1000 muestras para hallar la distribución de los beneficios.
    2. Encuentra el beneficio promedio, el intervalo de confianza del 95% y el riesgo de pérdidas. La pérdida es una ganancia negativa, calcúlala como una probabilidad y luego exprésala como un porcentaje.
    3. Presenta tus conclusiones: propón una región para el desarrollo de pozos petrolíferos y justifica tu elección. ¿Coincide tu elección con la elección anterior en el punto 4.3?

# $\textcolor{blue}{Sprint\ 12\ -\ Machine\ Learning\ in\ Business}$
### Project Description

You work for the oil extraction company OilyGiant. Your task is to find the best locations to open 200 new oil wells.

To complete this task, you must carry out the following steps:

- Read the files containing parameters collected from oil wells in the selected region: crude quality and reserve volume.
- Create a model to predict the volume of reserves in new wells.
- Select the oil wells with the highest estimated values.
- Choose the region with the highest total profit for the selected oil wells.

You have data on crude samples from three regions. The parameters of each oil well in each region are already known. Create a model that helps choose the region with the highest profit margin. Analyze potential profits and risks using the bootstrapping technique.

Conditions:

- Only linear regression must be used to train the model.
- When exploring a region, a study of 500 points is conducted, selecting the best 200 points for profit calculation.
- The budget for developing 200 oil wells is 100 million USD.
- One barrel of raw material generates $4.5 in revenue. The revenue from one unit of product is $4,500 (the volume of reserves is expressed in thousands of barrels).
- After risk evaluation, keep only the regions with a risk of losses below 2.5%. From those that meet the criteria, select the region with the highest average profit.

The data is synthetic: contract details and well characteristics are not disclosed.

Data Description

Geological exploration data for the three regions are stored in the following files:

- /datasets/geo_data_0.csv
- /datasets/geo_data_1.csv
- /datasets/geo_data_2.csv
- id — unique oil well identifier
- f0, f1, f2 — three feature values for the points (their specific meaning is not important, but the features themselves are significant)
- product — volume of reserves in the oil well (thousands of barrels)

Project Instructions

1. Download and prepare the data. Explain your procedure.

2. Train and test the model for each region in geo_data_0.csv:

    1. Split the data into training and validation sets in a 75:25 ratio.
    2. Train the model and make predictions for the validation set.
    3. Save the predictions and the correct answers for the validation set.
    4. Display the average predicted reserve volume and the RMSE of the model.
    5. Analyze the results.
    6. Place all previous steps into functions, then perform and execute steps 2.1–2.5 for the files geo_data_1.csv and geo_data_2.csv.

3. Prepare for profit calculation:

    1. Store all values necessary for calculations in separate variables.
    2. Given the $100 million investment for 200 oil wells, on average one well must generate at least $500,000 in revenue units to avoid losses (this is equivalent to 111.1 units).
    3. Compare this value with the average reserve amount in each region.
    4. Present conclusions on how to prepare for the profit calculation step.

4. Write a function to calculate profit for a selected set of oil wells and model predictions:

    1. Choose the 200 wells with the highest predicted values in each of the three regions (i.e., the three CSV files).
    2. Sum the target reserve volume based on those predictions. Store the predictions for the 200 wells for each region.
    3. Calculate the potential profit of the top 200 wells per region.
    4. Present your conclusions: propose a region for oil well development and justify your choice.

5. Calculate risks and profits for each region:

    1. Using the predictions stored in step 4.2, apply bootstrapping with 1000 samples to find the profit distribution.
    2. Find the average profit, the 95% confidence interval, and the risk of losses. A loss is negative profit; calculate it as a probability and then express it as a percentage.
    3. Present your conclusions: propose a region for oil well development and justify your choice. Does your selection match your earlier choice in step 4.3?


