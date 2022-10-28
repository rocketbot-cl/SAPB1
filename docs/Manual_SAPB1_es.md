



# SAPB1
  
Modulo para automatizar SAP Business One.

![banner](imgs/Banner_SAPB1.png)

## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  

## Como usar este modulo

Para poder ejecutar los comandos deberemos tener en cuenta que los objetos que nos encontremos en SAP B1, ya sea un input, botón o menú se encuentran diferenciados por IDs, y algunos se encuentran dentro de filas y columnas. Para poder conocer estos datos, deberemos activar la opción de "Información del sistema" que se encuentra en el menú Visualizar, o apretar la combinación de teclas Ctrl + Shift + I. Luego en la esquina inferior izquierda podremos ver los datos del objeto. Es importante tener esto en cuanta a la hora de automatizar ya que sera necesario contar con el Form ID y Item ID, como así con la columna y la fila, de corresponder.

## Descripción de los comandos

### Conectar a SAP B1
  
Conectar a SAP B1
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a una variable||result|

### Iniciar sesion en SAP B1
  
Inicia sesion a SAP B1
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Usuario||manager|
|Contraseña||password|
|Nombre base datos||DBSociety01|
|Sociedad||2|

### Click
  
Realiza un click en un item
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Formulario||form|
|Item||item|
|Fila||row|
|Columna||column|
|Tipo|||

### Activar item de menu
  
Activar item de menu
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Item del menu||3392|

### Enviar texto
  
Enviar texto a una entrada de texto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Texto||Hello World!|

### Obtener texto
  
Obtiene el texto de un item
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Formulario||form|
|Item||item|
|Fila||row|
|Columna||column|
|Asignar resultado a una variable||result|

### Click en ventana emergente
  
Click en ventana emergente
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Item||item|

### Obtener datos de formularios y menus visibles
  
Obtener datos de formularios y menus. Los dato seran sobre ls formularios y menus visibles al momento de ejecución.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a una variable||result|

### Obtener datos de matriz visible
  
Obtener datos de matriz. La Matriz seleccionada debe encontrarse visible al momento de ejecución.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Formulario||form|
|Item||item|
|Asignar resultado a una variable||result|
