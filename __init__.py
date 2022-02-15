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

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "SAPB1" + os.sep + "libs" + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)
from SAPB1 import *

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")

global sap_b1

try:

    if module == "connect":
        res = GetParams("result")
        sap_b1 = SAP_B1()
        sap_b1.connect_app()
        #print(sap_b1)
        SetVar(res, True)

    if module == "login":
        #print(sap_b1)
        user = GetParams("user")
        password = GetParams("password")
        sap_b1.login(user, password)

    if module == "click":
        form_id = GetParams("form_id")
        item_id = GetParams("item_id")
        row = GetParams("row")
        column = GetParams("column")
        click_type = GetParams("click_type")
        if not row or not column:
            form = sap_b1.get_form(form_id)
            sap_b1.get_item(form, item_id).Click(int(click_type))
        else:
            form = sap_b1.get_form(form_id)
            item = sap_b1.get_specific_item(form, item_id)
            sap_b1.do_click_grid_item(item, row, column, int(click_type))

    if module == "activate_menu":
        menu_id = GetParams("menu_id")
        sap_b1.activate_menu(menu_id)

    if module == "send_text":
        text = GetParams("text")
        sap_b1.sbo_application.SendKeys(text)

    if module == "get_value":
        form_id = GetParams("form_id")
        item_id = GetParams("item_id")
        row = GetParams("row")
        column = GetParams("column")    
        res = GetParams("res")    
        if not row or not column:
            form = sap_b1.get_form(form_id)
            data_string = sap_b1.get_item(form, str(item_id)).Specific
            value = str(data_string.Value)
            SetVar(res, value)
        else:
            form = sap_b1.get_form(str(form_id))
            data_string = sap_b1.get_item(form, str(item_id)).Specific
            item_valor = data_string.Columns.Item(str(column)).Cells.Item(int(row))
            value = str(item_valor.Specific.Value)
            SetVar(res, value)

    if module == "pop_up":
        item_id = GetParams("item_id")
        smbForm = sap_b1.sbo_application.Forms.ActiveForm
        smbForm.Items.Item(str(item_id)).Click()

    if module == "combobox":
        form_id = GetParams("form_id")
        item_id = GetParams("item_id")
        value = GetParams("value")
        form = sap_b1.get_form(form_id)
        data_string = sap_b1.get_item(form, str(item_id)).Specific
        data_string.Select(str(value))

    if module == "checkBox":
        form_id = GetParams("form_id")
        item_id = GetParams("item_id")
        row = GetParams("row")
        column = GetParams("column")
        checkType = GetParams("checkType")
        if not row or not column:
            form = sap_b1.get_form(form_id)
            sap_b1.get_item(form, item_id).Click(int(click_type))
        else:
            form = sap_b1.get_form(form_id)
            item = sap_b1.get_specific_item(form, item_id)
            myItem = form.Items.Item(item_id).Specific.GetCellSpecific(column,int(row)) # C/F
            if int(checkType) == 0:
                myItem.Checked = True
            else:
                myItem.Checked = False

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e
