



# SAPB1
  
Module to automate SAP Business One.  
  
![banner](imgs/Banner_SAPB1.png)

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  

## How to use this module

To be able to execute the commands we must take into account that the objects that we find in SAP B1, either an input, button or menu are differentiated by IDs, and some of them are located within rows and columns. In order to know this data, we must activate the "System information" option found in the View menu, or press the Ctrl + Shift + I key combination. Then in the lower left corner we will be able to see the object data. It is important to take this into account when automating since it will be necessary to have the Form ID and Item ID, as well as the column and row, if applicable.

## Description of the commands

### Connect to SAP B1
  
Connect to SAP B1
|Parameters|Description|example|
| --- | --- | --- |
|Set result to a variable||result|

### Login to SAP B1
  
Login to SAP B1
|Parameters|Description|example|
| --- | --- | --- |
|User||manager|
|Password||password|
|Database name||DBSociety01|
|Society||2|

### Click
  
Do a click in an item
|Parameters|Description|example|
| --- | --- | --- |
|Form||form|
|Item||item|
|Row||row|
|Column||column|
|Type|||

### Activate menu item
  
Activate menu item
|Parameters|Description|example|
| --- | --- | --- |
|Menu item||3392|

### Send text
  
Send text to an input
|Parameters|Description|example|
| --- | --- | --- |
|Text||Hello World!|

### Get text
  
Get text from an item
|Parameters|Description|example|
| --- | --- | --- |
|Form||form|
|Item||item|
|Row||row|
|Column||column|
|Set result to a variable||result|

### Click in pop up
  
Click in pop up
|Parameters|Description|example|
| --- | --- | --- |
|Item||item|

### Get visible forms and menus data
  
Get data of forms and menus. The data will be about visible forms and menus at the momento of the execution.
|Parameters|Description|example|
| --- | --- | --- |
|Set result to a variable||result|

### Get visible matrix data
  
Get matrix data. The selected Matrix must be visible at the moment of execution.
|Parameters|Description|example|
| --- | --- | --- |
|Form||form|
|Item||item|
|Set result to a variable||result|
