# $\textcolor{blue}{Sprint\ 11\ -\ Aprendizaje\ supervisado\}$
### Descripción del proyecto

Los clientes de Beta Bank se están yendo, cada mes, poco a poco. Los banqueros descubrieron que es más barato salvar a los clientes existentes que atraer nuevos.

Necesitamos predecir si un cliente dejará el banco pronto. Tú tienes los datos sobre el comportamiento pasado de los clientes y la terminación de contratos con el banco.

Crea un modelo con el máximo valor F1 posible. Para aprobar la revisión, necesitas un valor F1 de al menos 0.59. Verifica F1 para el conjunto de prueba. 

Además, debes medir la métrica AUC-ROC y compararla con el valor F1.

Instrucciones del proyecto
1. Descarga y prepara los datos.  Explica el procedimiento.
2. Examina el equilibrio de clases. Entrena el modelo sin tener en cuenta el desequilibrio. Describe brevemente tus hallazgos.
3. Mejora la calidad del modelo. Asegúrate de utilizar al menos dos enfoques para corregir el desequilibrio de clases. Utiliza conjuntos de entrenamiento y validación para encontrar el mejor modelo y el mejor conjunto de parámetros. Entrena diferentes modelos en los conjuntos de entrenamiento y validación. Encuentra el mejor. Describe brevemente tus hallazgos.
4. Realiza la prueba final.

Descripción de los datos
Puedes encontrar los datos en el archivo  /datasets/Churn.csv file. Descarga el conjunto de datos.

Características

- RowNumber: índice de cadena de datos
- CustomerId: identificador de cliente único
- Surname: apellido
- CreditScore: valor de crédito
- Geography: país de residencia
- Gender: sexo
- Age: edad
- Tenure: período durante el cual ha madurado el depósito a plazo fijo de un cliente (años)
- Balance: saldo de la cuenta
- NumOfProducts: número de productos bancarios utilizados por el cliente
- HasCrCard: el cliente tiene una tarjeta de crédito (1 - sí; 0 - no)
- IsActiveMember: actividad del cliente (1 - sí; 0 - no)
- EstimatedSalary: salario estimado

Objetivo

- Exited: El cliente se ha ido (1 - sí; 0 - no)

# $\textcolor{blue}{Sprint\ 11\ -\ Supervised\ Learning\}$
### Project Description

Beta Bank customers are leaving, little by little, every month. The bankers discovered that it is cheaper to retain existing customers than to attract new ones.

We need to predict whether a customer will leave the bank soon. You have data on customers’ past behavior and contract termination with the bank.

Create a model with the highest possible F1 score. To pass the review, you need an F1 score of at least 0.59. Check the F1 score on the test set.

Additionally, you must measure the AUC-ROC metric and compare it with the F1 score.

Project Instructions

1. Download and prepare the data. Explain the procedure.
2. Examine the class balance. Train the model without taking class imbalance into account. Briefly describe your findings.
3. Improve the model’s quality. Make sure to use at least two approaches to correct class imbalance. Use training and validation sets to find the best model and the best set of parameters. Train different models on the training and validation sets. Find the best one. Briefly describe your findings.
4. Perform the final test.

Data Description

You can find the data in the file /datasets/Churn.csv. Download the dataset.

Features

- RowNumber: data row index
- CustomerId: unique customer identifier
- Surname: last name
- CreditScore: credit score
- Geography: country of residence
- Gender: gender
- Age: age
- Tenure: number of years the customer’s fixed-term deposit has been active
- Balance: account balance
- NumOfProducts: number of banking products used by the customer
- HasCrCard: customer has a credit card (1 – yes; 0 – no)
- IsActiveMember: customer activity (1 – yes; 0 – no)
- EstimatedSalary: estimated salary

Target

- Exited: customer has left (1 – yes; 0 – no)
