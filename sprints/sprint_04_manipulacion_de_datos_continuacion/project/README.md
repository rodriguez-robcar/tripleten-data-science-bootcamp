# $\textcolor{blue}{Sprint\ 4\ -\ Manipulación\ de\ datos\ (continuación)}$
### Descripción del proyecto

Instacart es una plataforma de entregas de comestibles donde la clientela puede registrar un pedido y hacer que se lo entreguen, similar a Uber Eats y Door Dash. 
Este conjunto de datos particular fue lanzado públicamente por Instacart en 2017 para una competición Kaggle. 
Los datos reales pueden descargarse directamente de la página de la competición Kaggle.

El conjunto de datos que te hemos proporcionado tiene modificaciones del original. 
Redujimos el tamaño del conjunto para que tus cálculos se hicieran más rápido e introdujimos valores ausentes y duplicados. 
Tuvimos cuidado de conservar las distribuciones de los datos originales cuando hicimos los cambios.

Tu misión es limpiar los datos y preparar un informe que brinde información sobre los hábitos de compra de los clientes de Instacart. 
Después de responder a cada pregunta, escribe una breve explicación de tus resultados en una celda markdown de tu Jupyter notebook.

Este proyecto requerirá que hagas gráficos que comuniquen tus resultados. 
Asegúrate de que cualquier gráfico que vayas a crear tenga un título, ejes etiquetados y una leyenda si es necesario; e incluye plt.show() al final de cada celda con un gráfico.

#### Diccionario de datos

Hay cinco tablas en el conjunto de datos, y tendrás que usarlas todas para hacer el preprocesamiento de datos y el análisis exploratorio de datos. A continuación se muestra un diccionario de datos que enumera las columnas de cada tabla y describe los datos que contienen.

* instacart_orders.csv: cada fila corresponde a un pedido en la aplicación Instacart.
  
  * 'order_id': número de ID que identifica de manera única cada pedido.
  * 'user_id': número de ID que identifica de manera única la cuenta de cada cliente.
  * 'order_number': el número de veces que este cliente ha hecho un pedido.
  * 'order_dow': día de la semana en que se hizo un pedido (0 si es domingo).
  * 'order_hour_of_day': hora del día en que se hizo el pedido.
  * 'days_since_prior_order': número de días transcurridos desde que este cliente hizo su pedido anterior.

* products.csv: cada fila corresponde a un producto único que pueden comprar los clientes.
  * 'product_id': número ID que identifica de manera única cada producto.
  * 'product_name': nombre del producto.
  * 'aisle_id': número ID que identifica de manera única cada categoría de pasillo de víveres.
  * 'department_id': número ID que identifica de manera única cada departamento de víveres.

* order_products.csv: cada fila corresponde a un artículo pedido en un pedido.
  * 'order_id': número de ID que identifica de manera única cada pedido.
  * 'product_id': número ID que identifica de manera única cada producto.
  * 'add_to_cart_order': el orden secuencial en el que se añadió cada artículo en el carrito.
  * 'reordered': 0 si el cliente nunca ha pedido este producto antes, 1 si lo ha pedido.

* aisles.csv
  * 'aisle_id': número ID que identifica de manera única cada categoría de pasillo de víveres.
  * 'aisle': nombre del pasillo.

* departments.csv
  * 'department_id': número ID que identifica de manera única cada departamento de víveres.
  * 'department': nombre del departamento.

# $\textcolor{blue}{Sprint\ 4\ -\ Data\ Wrangling\ (Continued)}$
### Project Description

Instacart is a grocery delivery platform where customers can place an order and have it delivered, similar to Uber Eats and DoorDash.
This particular dataset was publicly released by Instacart in 2017 for a Kaggle competition.
The original data can be downloaded directly from the Kaggle competition page.

The dataset we have provided has been modified from the original.
We reduced its size so that your calculations would run faster, and we introduced missing and duplicate values.
We took care to preserve the distributions of the original data when making these changes.

Your mission is to clean the data and prepare a report that provides insights into the shopping habits of Instacart customers.  
After answering each question, write a brief explanation of your results in a markdown cell in your Jupyter notebook.

This project will require you to create visualizations that communicate your findings.
Make sure that any chart you create has a title, labeled axes, and a legend if necessary; and include plt.show() at the end of each cell containing a chart.

#### Data Dictionary

There are five tables in the dataset, and you will need to use all of them for data preprocessing and exploratory data analysis. 
Below is a data dictionary listing the columns of each table and describing the data they contain:

* instacart_orders.csv: each row corresponds to an order placed in the Instacart app.
  * order_id: ID number that uniquely identifies each order.
  * user_id: ID number that uniquely identifies each customer account.
  * order_number: the number of times this customer has placed an order.
  * order_dow: day of the week the order was placed (0 = Sunday).
  * order_hour_of_day: hour of the day the order was placed.
  * days_since_prior_order: number of days since this customer’s previous order.

* products.csv: each row corresponds to a unique product available for purchase.
  * product_id: ID number that uniquely identifies each product.
  * product_name: name of the product.
  * aisle_id: ID number that uniquely identifies each grocery aisle category.
  * department_id: ID number that uniquely identifies each grocery department.

* order_products.csv: each row corresponds to an item ordered within an order.
  * order_id: ID number that uniquely identifies each order.
  * product_id: ID number that uniquely identifies each product.
  * add_to_cart_order: the sequential order in which each item was added to the cart.
  * reordered: 0 if the customer has never ordered this product before, 1 if they have.

* aisles.csv
  * aisle_id: ID number that uniquely identifies each grocery aisle category.
  * aisle: name of the aisle.

* departments.csv
  * department_id: ID number that uniquely identifies each grocery department.
  * department: name of the department.
