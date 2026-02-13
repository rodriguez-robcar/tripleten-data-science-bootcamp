# $\textcolor{blue}{Sprint\ 10\ -\ Introducción\ al\ machine\ learning}$
### Descripción del proyecto

La compañía móvil Megaline no está satisfecha al ver que muchos de sus clientes utilizan planes heredados. Quieren desarrollar un modelo que pueda analizar el comportamiento de los clientes y recomendar uno de los nuevos planes de Megaline: Smart o Ultra.

Tienes acceso a los datos de comportamiento de los suscriptores que ya se han cambiado a los planes nuevos (del proyecto del sprint de Análisis estadístico de datos). Para esta tarea de clasificación debes crear un modelo que escoja el plan correcto. Como ya hiciste el paso de procesar los datos, puedes lanzarte directo a crear el modelo.

Desarrolla un modelo con la mayor exactitud posible. En este proyecto, el umbral de exactitud es 0.75. Usa el dataset para comprobar la exactitud.

Instrucciones del proyecto.
1. Abre y examina el archivo de datos. Dirección al archivo:/datasets/users_behavior.csv Descarga el dataset
2. Segmenta los datos fuente en un conjunto de entrenamiento, uno de validación y uno de prueba.
3. Investiga la calidad de diferentes modelos cambiando los hiperparámetros. Describe brevemente los hallazgos del estudio.
4. Comprueba la calidad del modelo usando el conjunto de prueba.
5. Tarea adicional: haz una prueba de cordura al modelo. Estos datos son más complejos que los que habías usado antes así que no será una tarea fácil. Más adelante lo veremos con más detalle.

Descripción de datos
Cada observación en el dataset contiene información del comportamiento mensual sobre un usuario. La información dada es la siguiente:

- сalls — número de llamadas,
- minutes — duración total de la llamada en minutos,
- messages — número de mensajes de texto,
- mb_used — Tráfico de Internet utilizado en MB,
- is_ultra — plan para el mes actual (Ultra - 1, Smart - 0).

# $\textcolor{blue}{Sprint\ 10\ -\ Introduction\ to\ Machine\ Learning}$
### Project Description

The mobile company Megaline is not satisfied to see that many of its customers are using legacy plans. They want to develop a model that can analyze customer behavior and recommend one of Megaline’s new plans: Smart or Ultra.

You have access to behavioral data from subscribers who have already switched to the new plans (from the Statistical Data Analysis sprint project). For this classification task, you must create a model that selects the correct plan. Since you have already completed the data preprocessing step, you can go straight to building the model.

Develop a model with the highest possible accuracy. In this project, the accuracy threshold is 0.75. Use the dataset to evaluate the accuracy.

Project instructions:

1. Open and examine the data file. File path: /datasets/users_behavior.csv. Download the dataset.
2. Split the source data into a training set, a validation set, and a test set.
3. Investigate the performance of different models by tuning hyperparameters. Briefly describe the findings of your study.
4. Evaluate the quality of the model using the test set.
5. Additional task: perform a sanity check on the model. These data are more complex than those you used before, so it won’t be an easy task. We’ll examine this in more detail later.

Data description:

Each observation in the dataset contains information about a user’s monthly behavior. The available information is:

- calls — number of calls
- minutes — total call duration in minutes
- messages — number of text messages

mb_used — Internet traffic used in MB

is_ultra — plan for the current month (Ultra = 1, Smart = 0)
