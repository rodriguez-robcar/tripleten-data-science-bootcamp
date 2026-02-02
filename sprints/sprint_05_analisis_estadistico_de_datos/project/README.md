# $\textcolor{blue}{Sprint\ 5\ -\ Análisis\ estadístico\ de\ datos}$
### Descripción del proyecto

Trabajas como analista para el operador de telecomunicaciones Megaline. La empresa ofrece a sus clientes dos tarifas de prepago, Surf y Ultimate. 
El departamento comercial quiere saber cuál de los planes genera más ingresos para poder ajustar el presupuesto de publicidad.

Vas a realizar un análisis preliminar de las tarifas basado en una selección de clientes relativamente pequeña. 
Tendrás los datos de 500 clientes de Megaline: quiénes son los clientes, de dónde son, qué tarifa usan, así como la cantidad de llamadas que hicieron y los mensajes de texto que enviaron en 2018. 
Tu trabajo es analizar el comportamiento de los clientes y determinar qué tarifa de prepago genera más ingresos. 
Más adelante, encontrarás en las instrucciones del proyecto cuáles son exactamente los aspectos del comportamiento de los clientes que debes analizar. 
Determinar qué plan, en promedio, aporta más ingresos es una cuestión que se abordará mediante pruebas estadísticas. Más adelante encontrarás más información al respecto en la sección de instrucciones del proyecto.

#### Descripción de las tarifas
Nota: Megaline redondea los segundos a minutos y los megabytes a gigabytes. Para las llamadas, cada llamada individual se redondea: incluso si la llamada duró solo un segundo, se contará como un minuto. 
Para el tráfico web, las sesiones web individuales no se redondean. En vez de esto, el total del mes se redondea hacia arriba. Si alguien usa 1025 megabytes este mes, se le cobrarán 2 gigabytes.

A continuación puedes ver una descripción de las tarifas:

* Surf

  1. Pago mensual: $20.
  2. 500 minutos al mes, 50 SMS y 15 GB de datos.
  3. Si se exceden los límites del paquete: 
      - 1 minuto: 3 centavos.
      - 1 SMS: 3 centavos.
      - 1 GB de datos: $10.

* Ultimate

  1. Pago mensual: $70.
  2. 3000 minutos al mes, 1000 SMS y 30 GB de datos.
  3. Si se exceden los límites del paquete:
      - 1 minuto: 1 centavo.
      - 1 SMS: 1 centavo.
      - 1 GB de datos: $7.

#### Diccionario de datos
En este proyecto, trabajarás con cinco tablas diferentes.

* La tabla users (datos sobre los usuarios):
  * user_id: identificador único del usuario.
  * first_name: nombre del usuario.
  * last_name: apellido del usuario.
  * age: edad del usuario (en años).
  * reg_date: fecha de suscripción (dd, mm, aa).
  * churn_date: la fecha en la que el usuario dejó de usar el servicio (si el valor es ausente, la tarifa se estaba usando cuando fue extraída esta base de datos).
  * city: ciudad de residencia del usuario.
  * plan: nombre de la tarifa.

* La tabla calls (datos sobre las llamadas):
  * id: identificador único de la llamada.
  * call_date: fecha de la llamada.
  * duration: duración de la llamada (en minutos).
  * user_id: el identificador del usuario que realiza la llamada.

* La tabla messages (datos sobre los SMS):
  * id: identificador único del SMS.
  * message_date: fecha del SMS.
  * user_id: el identificador del usuario que manda el SMS.

* La tabla internet (datos sobre las sesiones web):
  * id: identificador único de la sesión.
  * mb_used: el volumen de datos gastados durante la sesión (en megabytes).
  * session_date: fecha de la sesión web.
  * user_id: identificador del usuario.

* La tabla plans (datos sobre las tarifas):
  * plan_name: nombre de la tarifa.
  * usd_monthly_fee: pago mensual en dólares estadounidenses.
  * minutes_included: minutos incluidos al mes.
  * messages_included: SMS incluidos al mes.
  * mb_per_month_included: datos incluidos al mes (en megabytes).
  * usd_per_minute: precio por minuto tras exceder los límites del paquete (por ejemplo, si el paquete incluye 100 minutos, el operador cobrará el minuto 101).
  * usd_per_message: precio por SMS tras exceder los límites del paquete.
  * usd_per_gb: precio por gigabyte de los datos extra tras exceder los límites del paquete (1 GB = 1024 megabytes).

# $\textcolor{blue}{Sprint\ 5\ -\ Statistical\ Data\ Analysis}$
### Project Description

You work as an analyst for the telecommunications operator Megaline. The company offers its customers two prepaid plans: Surf and Ultimate. The commercial department wants to know which of the plans generates more revenue in order to adjust the advertising budget.

You will carry out a preliminary analysis of the plans based on a relatively small selection of customers. You will have data on 500 Megaline customers: who they are, where they are from, which plan they use, as well as the number of calls they made and the text messages they sent in 2018. Your task is to analyze customer behavior and determine which prepaid plan generates more revenue. Later, in the project instructions, you will find exactly which aspects of customer behavior you need to analyze. Determining which plan, on average, brings in more revenue is a question that will be addressed using statistical tests. You will find more information about this in the project instructions section.

#### Description of the Plans
Note: Megaline rounds seconds up to minutes and megabytes up to gigabytes. For calls, each individual call is rounded: even if the call lasted only one second, it will be counted as one minute. For web traffic, individual web sessions are not rounded. Instead, the monthly total is rounded up. For example, if someone uses 1025 megabytes in a month, they will be charged for 2 gigabytes.

Here is a description of the plans:

* Surf

  1. Monthly fee: $20
  2. 500 minutes per month, 50 SMS, and 15 GB of data
  3. If package limits are exceeded:
      - 1 minute: $0.03
      - 1 SMS: $0.03
      - 1 GB of data: $10

* Ultimate

    1. Monthly fee: $70
    2. 3000 minutes per month, 1000 SMS, and 30 GB of data
    3. If package limits are exceeded:
      - 1 minute: $0.01
      - 1 SMS: $0.01
      - 1 GB of data: $7

#### Data Dictionary
In this project, you will work with five different tables:

* users (data about users):
  
  * user_id: unique user identifier
  * first_name: user’s first name
  * last_name: user’s last name
  * age: user’s age (in years)
  * reg_date: subscription date (dd, mm, yy)
  * churn_date: the date the user stopped using the service (if the value is missing, the plan was still active when this database was extracted)
  * city: user’s city of residence
  * plan: name of the plan

* calls (data about calls):

  * id: unique call identifier
  * call_date: date of the call
  * duration: duration of the call (in minutes)
  * user_id: identifier of the user who made the call

* messages (data about SMS):

  * id: unique SMS identifier
  * message_date: date of the SMS
  * user_id: identifier of the user who sent the SMS

* internet (data about web sessions):

  * id: unique session identifier
  * mb_used: volume of data used during the session (in megabytes)
  * session_date: date of the web session
  * user_id: user identifier

* plans (data about the plans):

  * plan_name: name of the plan
  * usd_monthly_fee: monthly fee in US dollars
  * minutes_included: minutes included per month
  * messages_included: SMS included per month
  * mb_per_month_included: data included per month (in megabytes)
  * usd_per_minute: price per minute after exceeding package limits (e.g., if the package includes 100 minutes, the operator will charge for the 101st minute)
  * usd_per_message: price per SMS after exceeding package limits
  * usd_per_gb: price per gigabyte of extra data after exceeding package limits (1 GB = 1024 megabytes)
