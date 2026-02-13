# $\textcolor{blue}{Sprint\ 17\ -\ Aprendizaje\ automático\ de\ textos}$
### Descripción del proyecto

Film Junky Union, una nueva comunidad vanguardista para los aficionados de las películas clásicas, está desarrollando un sistema para filtrar y categorizar reseñas de películas. Tu objetivo es entrenar un modelo para detectar las críticas negativas de forma automática. Para lograrlo, utilizarás un conjunto de datos de reseñas de películas de IMDB con etiquetado para construir un modelo que clasifique las reseñas como positivas y negativas. Este deberá alcanzar un valor F1 de al menos 0.85.

Instrucciones del proyecto

1. Carga los datos.
2. Preprocesa los datos, si es necesario.
3. Realiza un análisis exploratorio de datos y haz tu conclusión sobre el desequilibrio de clases.
4. Realiza el preprocesamiento de datos para el modelado.
5. Entrena al menos tres modelos diferentes para el conjunto de datos de entrenamiento.
6. Prueba los modelos para el conjunto de datos de prueba.
7. Escribe algunas reseñas y clasifícalas con todos los modelos.
8. Busca las diferencias entre los resultados de las pruebas de los modelos en los dos puntos anteriores. Intenta explicarlas.
9. Muestra tus hallazgos.

¡Importante! Para tu comodidad, la plantilla del proyecto ya contiene algunos fragmentos de código, así que puedes usarlos si lo deseas. Si deseas hacer borrón y cuenta nueva, simplemente elimina todos esos fragmentos de código. Aquí está la lista de fragmentos de código:

- un poco de análisis exploratorio de datos con algunos gráficos;
- evaluate_model(): una rutina para evaluar un modelo de clasificación que se ajusta a la interfaz de predicción de scikit-learn;
- BERT_text_to_embeddings(): una ruta para convertir lista de textos en insertados con BERT.

Tu trabajo principal es construir y evaluar modelos.

Como puedes ver en la plantilla del proyecto, te sugerimos probar modelos de clasificación basados en regresión logística y potenciación del gradiente, pero puedes probar otros métodos. Puedes jugar con la estructura de la plantilla del proyecto siempre y cuando sigas sus instrucciones.

No tienes que usar BERT para el proyecto porque requiere mucha potencia computacional y será muy lento en la CPU para el conjunto de datos completo. Debido a esto, BERT generalmente debe ejecutarse en GPU para tener un rendimiento adecuado. Sin embargo, puedes intentar incluir BERT en el proyecto para una parte del conjunto de datos. Si deseas hacer esto, te sugerimos hacerlo de manera local y solo tomar un par de cientos de objetos por cada parte del conjunto de datos (entrenamiento/prueba) para evitar esperar demasiado tiempo. Asegúrate de indicar que estás usando BERT en la primera celda (el encabezado de tu proyecto).

Descripción de los datos
Los datos se almacenan en el archivo imdb_reviews.tsv.

Los datos fueron proporcionados por Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, y Christopher Potts. (2011). <b>Learning Word Vectors for Sentiment Analysis.</b> La Reunión Anual 49 de la Asociación de Lingüística Computacional (ACL 2011).

Aquí se describen los campos seleccionados:

- review: el texto de la reseña
- pos: el objetivo, '0' para negativo y '1' para positivo
- ds_part: 'entrenamiento'/'prueba' para la parte de entrenamiento/prueba del conjunto de datos, respectivamente

Hay otros campos en el conjunto de datos, puedes explorarlos si lo deseas.

# $\textcolor{blue}{Sprint\ 17\ -\ Machine\ Learning\ for\ Texts\ (NLP)}$
### Project Description

Film Junky Union, a new cutting-edge community for classic movie fans, is developing a system to filter and categorize movie reviews. Your goal is to train a model to automatically detect negative reviews. To achieve this, you will use a labeled IMDB movie reviews dataset to build a model that classifies reviews as positive or negative. The model must achieve an F1 score of at least 0.85.

Project Instructions

1. Load the data.
2. Preprocess the data, if necessary.
3. Perform exploratory data analysis and draw conclusions about class imbalance.
4. Perform data preprocessing for modeling.
5. Train at least three different models on the training dataset.
6. Test the models on the test dataset.
7. Write a few reviews yourself and classify them using all models.
8. Look for differences between the test results of the models in the two previous steps. Try to explain them.
9. Present your findings.

Important!

For your convenience, the project template already contains some code snippets, so you may use them if you wish. If you prefer to start from scratch, simply delete those snippets. Here is the list of included code fragments:

- Some exploratory data analysis with a few plots
- evaluate_model(): a routine for evaluating a classification model that follows the scikit-learn prediction interface
- BERT_text_to_embeddings(): a function to convert a list of texts into BERT embeddings

Your main task is to build and evaluate models.

As you can see in the project template, we suggest trying classification models based on logistic regression and gradient boosting, but you may try other methods. You may adjust the structure of the project template as long as you follow its instructions.

You do not have to use BERT for this project because it requires significant computational power and will be very slow on a CPU for the full dataset. For this reason, BERT should generally be run on a GPU for adequate performance. However, you may attempt to include BERT in the project for a portion of the dataset. If you choose to do so, we recommend running it locally and using only a few hundred samples from each dataset split (training/test) to avoid long waiting times. Be sure to indicate that you are using BERT in the first cell (the project header).

Data Description

The data is stored in the file imdb_reviews.tsv.

The dataset was provided by Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts. (2011). <b>Learning Word Vectors for Sentiment Analysis.</b> Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics (ACL 2011).

Here are the selected fields:

- review: the review text
- pos: the target, '0' for negative and '1' for positive
- ds_part: 'train'/'test' indicating the training/test split of the dataset

There are other fields in the dataset; you may explore them if you wish.
