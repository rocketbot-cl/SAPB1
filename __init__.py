# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import os
import sys
base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "SAPB1" + os.sep + "libs" + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)
from logging import exception
from SAPB1 import *
import psutil 
import time
from threading import Thread
from queue import Queue, Empty

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")

global sap_b1
global types

types = {
        4: 'Button',
        8: 'Static Text',
        16: 'Edit Text',
        99: 'Folder',
        113: 'Combo Box',
        116: 'Linked Button',
        118: 'Edit Text',
        121: 'CheckBox',
        122: 'Option Button',
        127: 'Matrix',
        128: 'Grid'
    }

if module == "connect":
    res = GetParams("result")
    try:
        # This block of code loops until the SAPB1 appear as a running process, once that happen, sleeps for 5 seconds and procedes to make the connection
        processName = 'SAP Business One.exe'
        var = False
        while var == False:
            processes = psutil.process_iter()
            for proc in processes:
                try:
                    # Check if process name contains the given name string.
                    if processName.lower() in proc.name().lower():
                        var = True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
        time.sleep(10)

        sap_b1 = SAP_B1()
        sap_b1.connect_app()
        SetVar(res, True)
    except Exception as e:
        SetVar(res, False)
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "login":
    
    user = GetParams("user")
    password = GetParams("password")
    data_base = GetParams("db")
    society = GetParams("society")
    sync_sap = GetParams('sync_sap')
    async_sap = GetParams('async_sap')
    
    sync_sap = eval(sync_sap) if sync_sap else None
    async_sap = eval(async_sap) if async_sap else None
    
    try:
        if sync_sap or (not sync_sap and not async_sap):
            if society:
                sap_b1.login_2(society)
            else:
                sap_b1.login_1(user, password, data_base)
        else:
            q = Queue()
            if society:
                t = Thread(target=sap_b1.login_2, args=(society,))
                t.start()
            else:
                t = Thread(target=sap_b1.login_1, args=(user, password, data_base))
                t.start()
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "wait_object":
    form_id = GetParams("form_id")
    item_id = GetParams("item_id")
    timeout = GetParams("timeout") or 5
    res = GetParams("res")

    try:
        form = sap_b1.get_form(form_id)
        form.Select()
        
        time_ = 0
        visible = False
        while not visible or time_ <= timeout:
            item = sap_b1.get_item(form, item_id)
            visible = item.Visible
        SetVar(res, visible)
    
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e
    
if module == "click":
    form_id = GetParams("form_id")
    item_id = GetParams("item_id")
    row = GetParams("row")
    column = GetParams("column")
    click_type = GetParams("click_type")
    specific = GetParams("specific")
    try:
        form = sap_b1.get_form(form_id)
        form.Select()
        item = sap_b1.get_item(form, item_id)
        if not row or not column:
            if specific and eval(specific) and item.Type in [16, 118]:
                item.Specific.ClickPicker() # Edit Text (OPTIONAL) Specific click
            else:
                sap_b1.do_click_item(item, click_type)
        else:
            item_s = sap_b1.get_specific_item(form, item_id)
            if item.Type == 128:
                item_s.Columns.Item(column).Click(int(row)) # Grid cell Specific click
            else:
                sap_b1.do_click_grid_item(item_s, row, column, click_type)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "select":
    form_id = GetParams("form_id")
    item_id = GetParams("item_id")
    row = GetParams("row")
    column = GetParams("column")
    method_type = GetParams("type")
    value = GetParams("value")

    try:
        form = sap_b1.get_form(form_id)
        form.Select()
        item = sap_b1.get_specific_item(form, item_id)
        if not row or not column:
            sap_b1.do_select_item(item, method_type, value)
        else:
            sap_b1.do_select_grid_item(item, row, column, method_type, value)

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "activate_menu":
    menu_id = GetParams("menu_id")
    try:
        q = Queue()
        t = Thread(target=sap_b1.activate_menu, args=(menu_id,))
        t.start()
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "send_text":
    text = GetParams("text")
    key_ = GetParams("key")
    try:
        if text:
            sap_b1.sbo_application.SendKeys(text)
        else:
            sap_b1.sbo_application.SendKeys(key_)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "get_value":
    form_id = GetParams("form_id")
    item_id = GetParams("item_id")
    row = GetParams("row")
    column = GetParams("column")    
    res = GetParams("res")
    try:
        form = sap_b1.get_form(form_id)
        form.Select()
        item = sap_b1.get_item(form, str(item_id))
        item_type = item.Type
        if not row or not column:
            try:
                if item_type in [4, 8, 99, 121, 122, 130]:
                    value = item.Specific.Caption
                elif item_type in [16, 113]:
                    try:
                        value = item.Specific.Value
                    except:
                        value = item.Specific.String
                elif item_type == 116:
                    try:
                        value = item.Specific.Value
                    except:
                        value = item.Specific.String
                elif item_type == 118:
                    try:
                        value = item.Specific.Value
                    except:
                        value = item.Specific.String
                elif item_type == 127:
                    value = item.Description
                else:
                    raise Exeption('Type not found.')       
            except:
                value = item.Description         
            
            SetVar(res, value)
        else:
            data_string = item.Specific
            if item_type == 128:
                value = data_string.DataTable.GetValue(str(column),int(row))
            else:
                item_valor = data_string.Columns.Item(str(column)).Cells.Item(int(row))
                value = item_valor.Specific.Value
            SetVar(res, value)
    except Exception as e:
        SetVar(res, False)
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "pop_up":
    item_id = GetParams("item_id")
    try:
        smbForm = sap_b1.sbo_application.Forms.ActiveForm
        smbForm.Items.Item(str(item_id)).Click()
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == 'data':
    res = GetParams('result')

    try:
        forms_ = sap_b1.sbo_application.Forms
        menus_ = sap_b1.sbo_application.Menus

        wholeList =[]
        for form in forms_:
            formDict = {}
            if form.Visible == True:
                formDict['FormTitle'] = form.Title
                formDict['FormID_1'] = form.UniqueID
                formDict['FormID_2'] = form.Type
                formDict['Items'] = []
                for item in form.Items:
                    itemDict = {}
                    if item.Visible == True:
                        try:
                            itemDict['UID'] = item.UniqueID
                            item_type = int(item.Type)
                            itemDict['Type'] = types.get(item_type)
                            itemDict['Position'] = {'Left': item.Left,
                                'Width': item.Width,
                                'Top': item.Top,
                                'Height': item.Height
                            }
                            
                            if item_type in [4, 8, 99, 121, 122, 130]:
                                itemDict['Caption'] = item.Specific.Caption
                            elif item_type in [16, 113]:
                                try:
                                    itemDict['Caption'] = item.Specific.Value
                                except:
                                    itemDict['Caption'] = item.Specific.String
                            elif item_type == 116:
                                try:
                                    itemDict['Caption'] = item.Specific.Value
                                except:
                                    itemDict['Caption'] = item.Specific.String
                            elif item_type == 118:
                                try:
                                    itemDict['Caption'] = item.Specific.Value
                                except:
                                    itemDict['Caption'] = item.Specific.String
                            elif item_type == 127:
                                itemDict['Caption'] = item.Description
                            elif item_type == 128:
                                itemDict['Caption'] = []                                
                            else:
                                raise Exception('Type not found.')                            
                            
                            if item_type == 121:
                                itemDict['Checked'] = item.Specific.Checked
                            if item_type == 122:
                                itemDict['Selected'] = item.Specific.Selected
                            if item_type == 128:
                                itemDict['Columns'] = [col.Name for col in item.Specific.DataTable.Columns]
                            
                        except Exception as e:
                            print(e)
                            itemDict['UID'] = item.UniqueID
                            itemDict['Type'] = item.Type
                            itemDict['Caption'] = item.Description
                            
                        formDict['Items'].append(itemDict)

                wholeList.append(formDict)

        for menu in menus_:
            menuDict = {}
            menuDict['MenuTitle'] = menu.String
            menuDict['MenuID'] = menu.UID
            menuDict['SubMenus'] = []
            try:
                # Only returns the first layer of submenus
                # Check for recusion to get all layers
                for sub in menu.SubMenus:
                    subDict = {}
                    subDict['SubMenuTitle'] = sub.String
                    subDict['SubMenuID'] = sub.UID
                    
                    if not subDict == {}:
                        menuDict['SubMenus'].append(subDict)
            except:
                continue            

            wholeList.append(menuDict)

        SetVar(res, wholeList)
    except Exception as e:
        SetVar(res, False)
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == 'matrix':
    form_id = GetParams("form_id")
    item_id = GetParams("item_id")
    res = GetParams('result')

    import xmltodict
    import json

    try:
        form = sap_b1.get_form(str(form_id))
        item = sap_b1.get_item(form, str(item_id))
        # Createsdict object which will hold the matix data
        matrixDict = {}  
        matrixDict['FormTitle'] = form.Title
        matrixDict['FormID'] = form.Type
        matrixDict['ItemUID'] = item.UniqueID
        
        if item.Type == 128:
            xml_ = item.Specific.DataTable.SerializeAsXML(0)
            matrixDict['DataTable'] = []
            dict_ = json.loads(json.dumps(xmltodict.parse(xml_)))
            SetVar(res, dict_)
        else:
            # Obtain XML versión of the matrix
            matrix_ = item.Specific.SerializeAsXML(0)
            # Converts it into a dict object
            xml_ = '<?xml version="1.0" encoding="UTF-16" ?>' + matrix_
            matrixDict['Matix'] = []
            dict_ = json.loads(json.dumps(xmltodict.parse(xml_)))
            
            # Obtain list o columns and list of rows within the matix
            columns = dict_['Matrix']['ColumnsInfo']['ColumnInfo']
            rows = dict_['Matrix']['Rows']['Row']
            # List to hold the ID of visible columns
            visible_columns = []
            # Initialize a counter which keep track of rows ID
            row_n = 0
            # Gets Row Zero data, which is the matix titles
            row_ = {}
            row_['Row'] = row_n
            row_['Columns Title'] = []
            for col in columns:
                col_ = {}
                if col['Visible'] == '1':
                    visible_columns.append(col['UniqueID'])
                    col_['ID'] = col['UniqueID']
                    col_['Title'] = col['Title']
                    row_['Columns Title'].append(col_)

            matrixDict['Matix'].append(row_)

            # Gets rest of the Rows data, it is divided in two cases a list of rows or a unique row
            # It is structured exactly the same for the Columns 
            # Rows List
            if isinstance(rows, list):
                for row in rows:
                    row_ = {}
                    row_n += 1
                    if row['Visible'] == '1':
                        row_['Row'] = row_n
                        row_cols = []
                        try:
                            columns = row[0]['Columns']['Column']
                        except:
                            columns = row['Columns']['Column']
                        # Columns List
                        if isinstance(columns, list):
                            for col in columns:
                                if col['ID'] not in visible_columns:
                                    continue
                                else:
                                    r_col = {}
                                    r_col['Column'] = col['ID']
                                    r_col['Value'] = col['Value']
                                    row_cols.append(r_col)
                            row_['Columns'] = row_cols
                        # Unique Column
                        else:
                            r_col = {}
                            r_col['Column'] = columns['ID']
                            r_col['Value'] = columns['Value']
                            row_['Columns'] = r_col         
                    if row_ in matrixDict['Matix']:
                        continue
                    else:
                        matrixDict['Matix'].append(row_)
            # Unique Row
            else:
                row_ = {}
                if rows['Visible'] == '1':
                    row_['Row'] = 1
                    row_cols = []
                    columns = rows['Columns']['Column']
                    # Columns List
                    if isinstance(columns, list):
                        for col in columns:
                            if col['ID'] not in visible_columns:
                                continue
                            else:
                                r_col = {}
                                r_col['Column'] = col['ID']
                                r_col['Value'] = col['Value']
                                row_cols.append(r_col)
                        row_['Columns'] = row_cols
                    # Unique Column
                    else:
                        r_col = {}
                        r_col['Column'] = columns['ID']
                        r_col['Value'] = columns['Value']
                        row_['Columns'] = r_col         
                    
                    matrixDict['Matix'].append(row_)

            SetVar(res, matrixDict)
    except Exception as e:
        SetVar(res, False)
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "set_focus":
    form_id = GetParams("form_id")
    item_id = GetParams("item_id")
    row = GetParams("row")
    column = GetParams("column")    
    try:
        if not row or not column:
            form = sap_b1.get_form(str(form_id))
            form.Select()
            item = sap_b1.get_item(form, str(item_id))
            id_ = item.UniqueID
            print(id_)
            form.ActiveItem = id_
            active_item = form.Items.Item(id_)
            item_spec = item.Specific
        else:
            form = sap_b1.get_form(str(form_id))
            form.Select()
            data_string = sap_b1.get_item(form, str(item_id)).Specific
            item_valor = data_string.Columns.Item(str(column)).Cells.Item(int(row))
            id_ = item.UniqueID
            form.ActiveItem = id_
            active_item = form.Items.Item(id_)
            item_spec = item.Specific
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e