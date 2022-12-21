



# SAPB1
  
Module to automate SAP Business One.  

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  

## How to use this module

To be able to execute the commands we must take into account that the objects that we find in SAP B1, either an input, button or menu are differentiated by IDs, and some of them are located within rows and columns. In order to know this data, we must activate the "System information" option found in the View menu, or press the Ctrl + Shift + I key combination. Then in the lower left corner we will be able to see the object data. It is important to take this into account when automating since it will be necessary to have the Form ID and Item ID, as well as the column and row, if applicable.

## Overview

1. Connect to SAP B1  
Connect to SAP B1. The application must be open at the time of executing the command.

2. Login to SAP B1  
Login to SAP B1

3. Click  
Do a click on an item

4. Select  
Select an item

5. Activate menu item  
Activate menu item

6. Send text or key  
Send text or key to a text input. If the text is empty, the key will be sent.

7. Get text  
Get text from an item

8. Click on pop up  
Click on pop up window

9. Get visible forms and menus data  
Get data of forms and menus. The data will be about visible forms and menus at the moment of the execution.

10. Get visible matrix data  
Get matrix data. Matrix must be visible at the moment of execution.  




----
### OS

- windows

### Dependencies

### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)