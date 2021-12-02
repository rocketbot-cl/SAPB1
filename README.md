



# SAPB1
  
Module to automate actions in SAP Business One. Do clicks, get text values, set text in inputs fields and many more.  

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  


## Como usar este modulo

Para poder ejecutar los comandos deberemos tener en cuenta que los objetos que nos encontremos
 en SAP B1, ya sea un input, botón o menú se encuentran diferenciados por IDs, y algunos se encuentran dentro de filas y
 columnas. Para poder conocer estos datos, deberemos activar la opción de "Información del sistema" que se encuentra en 
el menú visualizar, o apretar la combinación de teclas Ctrl + Shift + I. Luego en la esquina inferior izquierda podremos
 verlas propiedades del objeto. Debemos tener en cuenta esto a la hora de automatizar ya que es necesario saber el Item 
ID y Form ID, así además como la columna y la fila de ser necesario.



## Overview


1. Connect to SAP B1  
Connect to an SAP B1 instance

2. Login to SAP B1  
Log in to the SAP B1 instance using username and password

3. Click  
Click on an item, taking into account the form in which it is located and ID

4. Activate menu item  
Activate menu item by ID

5. Send text  
Send text to an input text

6. Get text  
Get text from an item from a input field

7. Select combobox  
Select an option from a combobox  




----
### OS

- windows

### Dependencies

### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)