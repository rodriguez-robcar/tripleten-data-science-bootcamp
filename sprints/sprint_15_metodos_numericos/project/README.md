# $\textcolor{blue}{Sprint\ 15\ -\ Métodos\ Numéricos}$
### Descripción del proyecto

Rusty Bargain es un servicio de venta de coches de segunda mano que está desarrollando una app para atraer a nuevos clientes. Gracias a esa app, puedes averiguar rápidamente el valor de mercado de tu coche. Tienes acceso al historial, especificaciones técnicas, versiones de equipamiento y precios. Tienes que crear un modelo que determine el valor de mercado.

A Rusty Bargain le interesa:

- la calidad de la predicción
- la velocidad de la predicción
- el tiempo requerido para el entrenamiento

Instrucciones del proyecto

1. Descarga y examina los datos.
2. Entrena diferentes modelos con varios hiperparámetros (debes hacer al menos dos modelos diferentes, pero más es mejor. Recuerda, varias implementaciones de potenciación del gradiente no cuentan como modelos diferentes). El punto principal de este paso es comparar métodos de potenciación del gradiente con bosque aleatorio, árbol de decisión y regresión lineal.
3. Analiza la velocidad y la calidad de los modelos.

Observaciones:

- Utiliza la métrica RECM para evaluar los modelos.
- La regresión lineal no es muy buena para el ajuste de hiperparámetros, pero es perfecta para hacer una prueba de cordura de otros métodos. Si la potenciación del gradiente funciona peor que la regresión lineal, definitivamente algo salió mal.
- Aprende por tu propia cuenta sobre la librería LightGBM y sus herramientas para crear modelos de potenciación del gradiente (gradient boosting).
- Idealmente, tu proyecto debe tener regresión lineal para una prueba de cordura, un algoritmo basado en árbol con ajuste de hiperparámetros (preferiblemente, bosque aleatorio), LightGBM con ajuste de hiperparámetros (prueba un par de conjuntos), y CatBoost y XGBoost con ajuste de hiperparámetros (opcional).
- Toma nota de la codificación de características categóricas para algoritmos simples. LightGBM y CatBoost tienen su implementación, pero XGBoost requiere OHE.
- Puedes usar un comando especial para encontrar el tiempo de ejecución del código de celda en Jupyter Notebook. Encuentra ese comando.
- Dado que el entrenamiento de un modelo de potenciación del gradiente puede llevar mucho tiempo, cambia solo algunos parámetros del modelo.
- Si Jupyter Notebook deja de funcionar, elimina las variables excesivas por medio del operador del:
  del features_train
  
Descripción de los datos
El dataset está almacenado en el archivo /datasets/car_data.csv. descargar dataset.

Características

- DateCrawled — fecha en la que se descargó el perfil de la base de datos
- VehicleType — tipo de carrocería del vehículo
- RegistrationYear — año de matriculación del vehículo
- Gearbox — tipo de caja de cambios
- Power — potencia (CV)
- Model — modelo del vehículo
- Mileage — kilometraje (medido en km de acuerdo con las especificidades regionales del conjunto de datos)
- RegistrationMonth — mes de matriculación del vehículo
- FuelType — tipo de combustible
- Brand — marca del vehículo
- NotRepaired — vehículo con o sin reparación
- DateCreated — fecha de creación del perfil
- NumberOfPictures — número de fotos del vehículo
- PostalCode — código postal del propietario del perfil (usuario)
- LastSeen — fecha de la última vez que el usuario estuvo activo

Objetivo

- Price — precio (en euros)

# $\textcolor{blue}{Sprint\ 15\ -\ Numerical\ Methods}$
### Project Description

Rusty Bargain is a used car sales service that is developing an app to attract new customers. Thanks to this app, you can quickly find out the market value of your car. You have access to historical data, technical specifications, trim versions, and prices. You need to create a model that determines the market value.

Rusty Bargain is interested in:

- Prediction quality
- Prediction speed
- Time required for training

Project Instructions

1. Download and examine the data.
2. Train different models with various hyperparameters (you must use at least two different models, but more is better. Remember, multiple gradient boosting implementations do not count as different models). The main goal of this step is to compare gradient boosting methods with random forest, decision tree, and linear regression.
3. Analyze the speed and quality of the models.

Notes:

- Use RMSE as the evaluation metric.
- Linear regression is not very suitable for hyperparameter tuning, but it is perfect as a sanity check for other methods. If gradient boosting performs worse than linear regression, something definitely went wrong.
- Learn on your own about the LightGBM library and its tools for building gradient boosting models.
- Ideally, your project should include:
- Linear regression as a sanity check
- A tree-based algorithm with hyperparameter tuning (preferably random forest)
- LightGBM with hyperparameter tuning (try a couple of parameter sets)
- CatBoost and XGBoost with hyperparameter tuning (optional)
- Take note of categorical feature encoding for simpler algorithms. LightGBM and CatBoost have their own implementations, but XGBoost requires One-Hot Encoding (OHE).
- You can use a special command in Jupyter Notebook to measure cell execution time. Find that command.
- Since training gradient boosting models can take a long time, change only a few model parameters.
- If Jupyter Notebook stops working, delete unnecessary variables using the del operator:

  del features_train

Data Description

The dataset is stored in the file /datasets/car_data.csv.

Features:

- DateCrawled — date when the profile was downloaded from the database
- VehicleType — type of vehicle body
- RegistrationYear — year of vehicle registration
- Gearbox — type of transmission
- Power — power (HP)
- Model — vehicle model
- Mileage — mileage (measured in km according to the dataset’s regional specifics)
- RegistrationMonth — month of vehicle registration
- FuelType — type of fuel
- Brand — vehicle brand
- NotRepaired — whether the vehicle has been repaired or not
- DateCreated — date the profile was created
- NumberOfPictures — number of vehicle photos
- PostalCode — postal code of the profile owner (user)
- LastSeen — date when the user was last active

Target:

- Price — price (in euros)
