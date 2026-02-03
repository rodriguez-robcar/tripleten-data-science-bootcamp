# $\textcolor{blue}{Sprint\ 6\ -\ Proyecto\ módulo\ 1}$
### Descripción del proyecto

Trabajas para la tienda online Ice que vende videojuegos por todo el mundo. Las reseñas de usuarios y expertos, los géneros, las plataformas (por ejemplo, Xbox o PlayStation) 
y los datos históricos sobre las ventas de juegos están disponibles en fuentes abiertas. 
Tienes que identificar patrones que determinen si un juego tiene éxito o no. Esto te permitirá detectar proyectos prometedores y planificar campañas publicitarias.

Delante de ti hay datos que se remontan a 2016. Imaginemos que es diciembre de 2016 y estás planeando una campaña para 2017.

Lo importante es adquirir experiencia de trabajo con datos. Realmente no importa si estás pronosticando las ventas de 2017 en función de los datos de 2016 o las ventas de 2027 en función de los datos de 2026.

El dataset contiene una columna "rating" que almacena la clasificación ESRB de cada juego. El Entertainment Software Rating Board (la Junta de clasificación de software de entretenimiento) evalúa el contenido de un juego y asigna una clasificación de edad como Adolescente o Adulto.

#### Instrucciones para completar el proyecto

#### $\textcolor{yellow}{Paso\ 1.\}$ Abre el archivo de datos y estudia la información general 

Ruta de archivo:

/datasets/games.csv . Descarga el dataset

#### $\textcolor{yellow}{Paso\ 2.\}$ Prepara los datos

- Reemplaza los nombres de las columnas (ponlos en minúsculas).
- Convierte los datos en los tipos necesarios.
- Describe las columnas en las que los tipos de datos han sido cambiados y explica por qué.
- Si es necesario, elige la manera de tratar los valores ausentes:
  - Explica por qué rellenaste los valores ausentes como lo hiciste o por qué decidiste dejarlos en blanco.
  - ¿Por qué crees que los valores están ausentes? Brinda explicaciones posibles.
  - Presta atención a la abreviatura TBD: significa "to be determined" (a determinar). Especifica cómo piensas manejar estos casos.
  - Calcula las ventas totales (la suma de las ventas en todas las regiones) para cada juego y coloca estos valores en una columna separada.

#### $\textcolor{yellow}{Paso\ 3.\}$ Analiza los datos

- Mira cuántos juegos fueron lanzados en diferentes años. ¿Son significativos los datos de cada período?
- Observa cómo varían las ventas de una plataforma a otra. Elige las plataformas con las mayores ventas totales y construye una distribución basada en los datos de cada año. Busca las plataformas que solían ser populares pero que ahora no tienen ventas. ¿Cuánto tardan generalmente las nuevas plataformas en aparecer y las antiguas en desaparecer?
- Determina para qué período debes tomar datos. Para hacerlo mira tus respuestas a las preguntas anteriores. Los datos deberían permitirte construir un modelo para 2017.
- Trabaja solo con los datos que consideras relevantes. Ignora los datos de años anteriores.
- ¿Qué plataformas son líderes en ventas? ¿Cuáles crecen y cuáles se reducen? Elige varias plataformas potencialmente rentables.
- Crea un diagrama de caja para las ventas globales de todos los juegos, desglosados por plataforma. ¿Son significativas las diferencias en las ventas? ¿Qué sucede con las ventas promedio en varias plataformas? Describe tus hallazgos.
- Mira cómo las reseñas de usuarios y profesionales afectan las ventas de una plataforma popular (tu elección). Crea un gráfico de dispersión y calcula la correlación entre las reseñas y las ventas. Saca conclusiones.
- Teniendo en cuenta tus conclusiones compara las ventas de los mismos juegos en otras plataformas.
- Echa un vistazo a la distribución general de los juegos por género. ¿Qué se puede decir de los géneros más rentables? ¿Puedes generalizar acerca de los géneros con ventas altas y bajas?

#### $\textcolor{yellow}{Paso\ 4.\}$ Crea un perfil de usuario para cada región

Para cada región (NA, UE, JP) determina:

  - Las cinco plataformas principales. Describe las variaciones en sus cuotas de mercado de una región a otra.
  - Los cinco géneros principales. Explica la diferencia.
  - Si las clasificaciones de ESRB afectan a las ventas en regiones individuales.

#### $\textcolor{yellow}{Paso\ 5.\}$ Prueba las siguientes hipótesis:

— Las calificaciones promedio de los usuarios para las plataformas Xbox One y PC son las mismas.

— Las calificaciones promedio de los usuarios para los géneros de Acción y Deportes son diferentes.

Establece tu mismo el valor de umbral alfa.

Explica:

— Cómo formulaste las hipótesis nula y alternativa.

— Qué criterio utilizaste para probar las hipótesis y por qué.

#### $\textcolor{yellow}{Paso\ 6.\}$ Escribe una conclusión general

Formato: Completa la tarea en Jupyter Notebook. Inserta el código de programación en las celdas code y las explicaciones de texto en las celdas markdown. Aplica formato y agrega encabezados.

Descripción de datos

— Name (Nombre)

— Platform (Plataforma)

— Year_of_Release (Año de lanzamiento)

— Genre (Género) 

— NA_sales (ventas en Norteamérica en millones de dólares estadounidenses) 

— EU_sales (ventas en Europa en millones de dólares estadounidenses) 

— JP_sales (ventas en Japón en millones de dólares estadounidenses) 

— Other_sales (ventas en otros países en millones de dólares estadounidenses) 

— Critic_Score (máximo de 100) 

— User_Score (máximo de 10) 

— Rating (ESRB)

Es posible que los datos de 2016 estén incompletos.

# $\textcolor{blue}{Sprint\ 6\ -\ Module\ 1\ Project}$
### Project Description

#### $\textcolor{yellow}{Step\ 1.\}$ Open the dataset and study the general information
File path:
/datasets/games.csv – Download the dataset.

#### $\textcolor{yellow}{Step\ 2.\}$ Prepare the data

- Replace column names (make them lowercase).

- Convert data into the necessary types.

- Describe the columns where data types were changed and explain why.

- If necessary, decide how to handle missing values:

  - Explain why you filled missing values the way you did, or why you left them blank.

  - Why do you think the values are missing? Provide possible explanations.

  - Pay attention to the abbreviation TBD: it means "to be determined." Specify how you plan to handle these cases.

  - Calculate total sales (sum of sales across all regions) for each game and place these values in a separate column.

#### $\textcolor{yellow}{Step\ 3.\}$ Analyze the data

- Check how many games were released in different years. Are the data for each period significant?
- Observe how sales vary across platforms. Choose the platforms with the highest total sales and build a distribution based on yearly data. Look for platforms that used to be popular but now have no sales. How long does it usually take for new platforms to appear and old ones to disappear?
- Determine which period you should take data from. To do this, look at your answers to the previous questions. The data should allow you to build a model for 2017.
- Work only with the data you consider relevant. Ignore data from earlier years.
- Which platforms are leaders in sales? Which are growing and which are declining? Choose several potentially profitable platforms.
- Create a box plot for global sales of all games, broken down by platform. Are the differences in sales significant? What happens to average sales across different platforms? Describe your findings.
- Examine how user and critic reviews affect sales of a popular platform (your choice). Create a scatter plot and calculate the correlation between reviews and sales. Draw conclusions.
- Based on your conclusions, compare sales of the same games on other platforms.
- Look at the overall distribution of games by genre. What can be said about the most profitable genres? Can you generalize about genres with high and low sales?

#### $\textcolor{yellow}{Step\ 4.\}$ Create a user profile for each region

For each region (NA, EU, JP), determine:

- The top five platforms. Describe variations in their market shares across regions.

- The top five genres. Explain the differences.

- Whether ESRB ratings affect sales in individual regions.

#### $\textcolor{yellow}{Step\ 5.\}$ Test the following hypotheses

— The average user ratings for Xbox One and PC platforms are the same.
— The average user ratings for Action and Sports genres are different.

Set the alpha threshold yourself.

Explain:

— How you formulated the null and alternative hypotheses.

— Which criterion you used to test the hypotheses and why.

#### $\textcolor{yellow}{Step\ 6.\}$ Write a general conclusion

Format: Complete the task in Jupyter Notebook. Insert programming code in code cells and explanations in markdown cells. Apply formatting and add headings.

Dataset Description

— Name – Game title

— Platform – Platform

— Year_of_Release – Release year

— Genre – Genre

— NA_sales – Sales in North America (in millions of USD)

— EU_sales – Sales in Europe (in millions of USD)

— JP_sales – Sales in Japan (in millions of USD)

— Other_sales – Sales in other countries (in millions of USD)

— Critic_Score – Maximum of 100

— User_Score – Maximum of 10

— Rating – ESRB rating

— Note: Data for 2016 may be incomplete.
