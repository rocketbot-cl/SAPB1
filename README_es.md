



# SAPB1
  
Modulo para automatizar SAP Business One.  

## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  

## Como usar este modulo

Para poder ejecutar los comandos deberemos tener en cuenta que los objetos que nos encontremos en SAP B1, ya sea un input, botón o menú se encuentran diferenciados por IDs, y algunos se encuentran dentro de filas y columnas. Para poder conocer estos datos, deberemos activar la opción de "Información del sistema" que se encuentra en el menú Visualizar, o apretar la combinación de teclas Ctrl + Shift + I. Luego en la esquina inferior izquierda podremos ver los datos del objeto. Es importante tener esto en cuanta a la hora de automatizar ya que sera necesario contar con el Form ID y Item ID, como así con la columna y la fila, de corresponder.

## Overview

1. Conectar a SAP B1  
Conectar a SAP B1. La aplicación debe estar abierta al momento de ejecutar el comando.

2. Iniciar sesión en SAP B1  
Iniciar sesión en SAP B1

3. Click  
Realiza un click en un item

4. Seleccionar  
Seleccionar un item

5. Activar item de menu  
Activar item de menu

6. Enviar texto o tecla  
Enviar texto o tecla a una entrada de texto. Si se deja vacío el texto, se enviará la tecla.

7. Obtener texto  
Obtiene el texto de un ítem

8. Click en ventana emergente  
Click en ventana emergente

9. Obtener datos de formularios y menus visibles  
Obtener datos de formularios y menus. Los dato seran sobre ls formularios y menus visibles al momento de ejecución.

10. Obtener datos de matriz visible  
Obtener datos de matriz. La Matriz debe encontrarse visible al momento de ejecución.  




----
### OS

- windows

### Dependencies

### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)