# $\textcolor{blue}{Sprint\ 13\ -\ Proyecto\ del\ módulo\ 2}$
### Descripción del proyecto

Los datos se almacenan en tres archivos:

- gold_recovery_train.csv — el dataset de entrenamiento descargado
- gold_recovery_test.csv —el dataset de prueba descargado
- gold_recovery_full.csv — el dataset fuente descargado

Los datos se indexan con la fecha y la hora de adquisición (date). Los parámetros cercanos en el tiempo suelen ser similares.

Algunos parámetros no están disponibles porque fueron medidos o calculados mucho más tarde. Por eso, algunas de las características que están presentes en el conjunto de entrenamiento pueden estar ausentes en el conjunto de prueba. El conjunto de prueba tampoco contiene objetivos.

El dataset fuente contiene los conjuntos de entrenamiento y prueba con todas las características.

Tienes a tu disposición los datos en bruto que solamente fueron descargados del almacén de datos. Antes de construir el modelo, comprueba que los datos sean correctos. Para ello, utiliza nuestras instrucciones.

Instrucciones del proyecto

1. Prepara los datos

    1.1. Abre los archivos y examina los datos.

    Ruta de acceso a los archivos:

    - /datasets/gold_recovery_train.csv
    - /datasets/gold_recovery_test.csv
    - /datasets/gold_recovery_full.csv

    1.2. Comprueba que el cálculo de la recuperación sea correcto. Calcula la recuperación de la característica rougher.output.recovery mediante el conjunto de entrenamiento. Encuentra el EAM entre tus cálculos y los valores de la característica. Facilita los resultados.

    1.3. Analiza las características no disponibles en el conjunto de prueba. ¿Cuáles son estos parámetros? ¿Cuál es su tipo?

    1.4. Realiza el preprocesamiento de datos.

2. Analiza los datos

    2.1. Observa cómo cambia la concentración de metales (Au, Ag, Pb) en función de la etapa de purificación.

    2.2. Compara las distribuciones del tamaño de las partículas de la alimentación en el conjunto de entrenamiento y en el conjunto de prueba. Si las distribuciones varían significativamente, la evaluación del modelo no será correcta.

    2.3. Considera las concentraciones totales de todas las sustancias en las diferentes etapas: materia prima, concentrado rougher y concentrado final. ¿Observas algún valor anormal en la distribución total? Si es así, ¿merece la pena eliminar esos valores de ambas muestras? Describe los resultados y elimina las anomalías.

3. Construye el modelo

    3.1. Escribe una función para calcular el valor final de sMAPE.

    3.2. Entrena diferentes modelos. Evalúalos aplicando la validación cruzada. Elige el mejor modelo y pruébalo utilizando la muestra de prueba. Facilita los resultados.

Utiliza estas fórmulas para las métricas de evaluación:

![moved_smape_1576239058_1589899769](https://github.com/user-attachments/assets/e6638a2f-5abe-4f50-8a64-942c9c96bc4c)

<img width="1400" height="255" alt="moved_10 3 3ES" src="https://github.com/user-attachments/assets/4c3a3a5a-af37-420a-b326-fe6cfba4bf70" />

# $\textcolor{blue}{Sprint\ 13\ -\ Module\ 2\ Project}$
### Project Description

The data is stored in three files:

- gold_recovery_train.csv — the downloaded training dataset
- gold_recovery_test.csv — the downloaded test dataset
- gold_recovery_full.csv — the downloaded source dataset

The data is indexed by the date and time of acquisition (date). Parameters that are close in time tend to be similar.

Some parameters are not available because they were measured or calculated much later. For this reason, some features present in the training set may be missing in the test set. The test set also does not contain target values.

The source dataset contains both the training and test sets with all features.

You have access to the raw data that was downloaded directly from the data warehouse. Before building the model, verify that the data is correct. To do so, follow our instructions.

Project Instructions

1. Prepare the data

    1.1. Open the files and examine the data.

    File paths:

    - /datasets/gold_recovery_train.csv

    - /datasets/gold_recovery_test.csv

    - /datasets/gold_recovery_full.csv

    1.2. Verify that the recovery calculation is correct. Calculate the recovery for the feature rougher.output.recovery using the training set. Find the MAE (Mean Absolute Error) between your calculated values and the feature values. Provide the results.

    1.3. Analyze the features not available in the test set. Which parameters are these? What is their data type?

    1.4. Perform data preprocessing.

2. Analyze the data

    2.1. Observe how the concentration of metals (Au, Ag, Pb) changes depending on the purification stage.

    2.2. Compare the particle size distributions of the feed in the training and test sets. If the distributions vary significantly, model evaluation will not be reliable.

    2.3. Consider the total concentrations of all substances at different stages: raw feed, rougher concentrate, and final concentrate. Do you observe any abnormal values in the total distribution? If so, is it worth removing these values from both samples? Describe your findings and remove anomalies.

3. Build the model

    3.1. Write a function to calculate the final sMAPE value.

    3.2. Train different models. Evaluate them using cross-validation. Choose the best model and test it using the test sample.  Provide the results.

Use the following formulas for the evaluation metrics:

![moved_smape_1576239058_1589899769](https://github.com/user-attachments/assets/e6638a2f-5abe-4f50-8a64-942c9c96bc4c)

<img width="1400" height="255" alt="moved_10 3 3ES" src="https://github.com/user-attachments/assets/4c3a3a5a-af37-420a-b326-fe6cfba4bf70" />
