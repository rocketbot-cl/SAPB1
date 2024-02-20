



# SAPB1
  
With this module you can automate SAP Business One.  

*Read this in other languages: [English](Manual_SAPB1.md), [Português](Manual_SAPB1.pr.md), [Español](Manual_SAPB1.es.md)*
  
![banner](imgs/Banner_SAPB1.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module

To be able to execute the commands we must take into account that the objects that we find in SAP B1, either an input, button or menu are differentiated by IDs, and some of them are located within rows and columns. In order to know this data, we must activate the "System information" option found in the View menu, or press the Ctrl + Shift + I key combination. Then in the lower left corner we will be able to see the object data. It is important to take this into account when automating since it will be necessary to have the Form ID and Item ID, as well as the column and row, if applicable.


## Description of the commands

### Connect to SAP B1
  
Connect to SAP B1. The application must be open at the time of executing the command.
|Parameters|Description|example|
| --- | --- | --- |
|Set result to a variable|Name of the variable where the result will be stored|res|

### Login to SAP B1
  
Login to SAP B1
|Parameters|Description|example|
| --- | --- | --- |
|User||manager|
|Password||password|
|Database name (Optional)||DBSociety01|
|Society (Optional)||2|
|Synchronous mode|Connect synchronously|Checkbox|
|Asynchronous mode|Connect asynchronously|Checkbox|

### Wait
  
Wait for an item
|Parameters|Description|example|
| --- | --- | --- |
|Form||form|
|Item||item|
|Timeout (Seconds - Optional)||5|
|Set result to a variable|Name of the variable where the result will be stored|result|

### Click
  
Do a click on an item
|Parameters|Description|example|
| --- | --- | --- |
|Form||form|
|Item||item|
|Row||row|
|Column||column|
|Type|||
|Click on picker|Click on the object search engine, applicable in the case of Text Edit objects|checkbox|

### Select
  
Select an item
|Parameters|Description|example|
| --- | --- | --- |
|Form||form|
|Item||item|
|Row||row|
|Column||column|
|Type|||
|Parameter||Value/Index|

### Activate menu item
  
Activate menu item
|Parameters|Description|example|
| --- | --- | --- |
|Menu item||3392|

### Send text or key
  
Send text or key to a text input. If the text is empty, the key will be sent.
|Parameters|Description|example|
| --- | --- | --- |
|Text||Hello World!|
|Send key||ENTER|

### Get text
  
Get text from an item
|Parameters|Description|example|
| --- | --- | --- |
|Form||form|
|Item||item|
|Row||row|
|Column||column|
|Set result to a variable|Name of the variable where the result will be stored|result|

### Click on pop up
  
Click on pop up window
|Parameters|Description|example|
| --- | --- | --- |
|Set result to a variable|Name of the variable where the result will be stored|item|

### Get visible forms and menus data
  
Get data of forms and menus. The data will be about visible forms and menus at the moment of the execution.
|Parameters|Description|example|
| --- | --- | --- |
|Set result to a variable|Name of the variable where the result will be stored|data|

### Get visible matrix data
  
Get matrix data. Matrix must be visible at the moment of execution.
|Parameters|Description|example|
| --- | --- | --- |
|Form||form|
|Item||item|
|Set result to a variable|Name of the variable where the result will be stored|result|
