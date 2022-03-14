



# SAPB1

Módulo para automatizar acciones de SAP Business One. Hacer clicks, obtener textos, escribir, entre tantas otras.
  
![banner](imgs/Banner_SAPB1.png)

## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  



## Descripción de los comandos

### Conectar a SAP B1
  
Conectarse a una instancia SAP B1
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a una variable|Asigna el resultado de la ejecución de la tarea a una variable|res|

### Iniciar sesion en SAP B1
  
Inicia sesion con la instancia de SAP B1 utilizando nombre de usuario y contraseña
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Usuario|Nombre de usuario|manager|
|Contraseña|Contraseña del usuario|manager|

### Click
  
Realiza un click en un item teniendo en cuenta el formulario en el que se encuentra y ID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Formulario|ID del formulario|59|
|Item|102|item|
|Fila|ID de la fila|1|
|Columna|ID de la columna|5|
|Tipo|Tipo de click||

### Activar item de menu
  
Activar item de menu por ID.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Item menu|ID del item de menu a activar|3392|

### Enviar texto
  
Enviar texto a una entrada de texto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Texto|Texto a enviar.|Hello World!|

### Obtener texto
  
Obtiene el texto de un item o entrada de texto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Formulario|ID del formulario|133|
|Item|ID del item|46|
|Fila|ID de la fila|1|
|Columna|ID de la columna|5|
|Resultado|Asigna el resultado de la ejecución de la tarea a una variable|result|

### Seleccionar combobox
  
Selecciona la opcion de un menu desplegable
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Form|ID del formulario|255|
|Item|ID del item|13|
|Valor|Valor del combobox a elegir|9|

### Click en Checkbox
  
Realiza un click en un checkbox teniendo en cuenta el formulario en el que se encuentra y ID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Formulario|ID del formulario|59|
|Item|ID del item|102|
|Fila|ID de la fila|1|
|Columna|ID de la columna|5|
|Tipo de accion|Accion a ejecutar||
