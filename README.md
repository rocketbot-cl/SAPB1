



# SAPB1
  
Module to automate actions in SAP Business One. Do clicks, get text values, set text in inputs fields and many more.  

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  

## How to use this module

To be able to execute the commands we must take into account that the objects that we find in SAP B1, either an input, button or menu are differentiated by IDs, and some of them are inside rows and columns. In order to know this data, we will have to activate the option "System information" that is in the visualize menu, or press the combination of keys Ctrl + Shift + I. Then in the lower left corner we will be able to see the properties of the object. We must take this into account when automating since it is necessary to know the Item ID and Form ID, as well as the column and row if necessary.



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