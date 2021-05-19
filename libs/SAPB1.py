import win32com.client

class SAP_B1:
    def __init__(self):
        self.sbo_gui_api = win32com.client.Dispatch("SAPbouiCOM.SboGuiApi") 
        self.connection_string = "0030002C0030002C00530041005000420044005F00440061007400650076002C0050004C006F006D0056004900490056"
        self.sbo_application = None            

    def connect_app(self):
        self.sbo_gui_api.Connect(self.connection_string)
        self.sbo_application = self.sbo_gui_api.GetApplication(-1)

    def login(self, user, pwd):
        forms = self.sbo_application.Forms
        for form in forms:
            form.Items.Item("4").Click(0)
            self.sbo_application.SendKeys(user)
            form.Items.Item("5").Click(0)
            self.sbo_application.SendKeys(pwd)
            form.Items.Item("1").Click(0)

    def get_form(self, id_form):
        return self.sbo_application.Forms.GetForm(str(id_form), 0)
    
    def get_specific_item(self, form, item_id):
        return form.Items.Item(str(item_id)).Specific

    def get_item(self, form, item_id):
        return form.Items.Item(str(item_id))

    def do_click_grid_item(self, item, row, column):
        double_click = 1
        item.Columns.Item(str(row)).Cells.Item(int(column)).Click(double_click)
    
    def activate_menu(self, id_menu):
        self.sbo_application.ActivateMenuItem(str(id_menu))

if __name__ == '__main__':
    sap_b1 = SAP_B1()
    sap_b1.connect_app()
        # 1 BOTON OK
        # 2 Finalizar
        # 4 usuario
        # 5 pwd



        #for item in items:
        #    print(item.UniqueID)
    #form = sap_b1.get_form("184")
    #sap_b1.get_item(form, "22").Click(0)
    #sap_b1.sbo_application.SendKeys("hola")
    #form.Items.Item("1").Click(1)

    #item = sap_b1.get_specific_item(form, "6")
    #sap_b1.do_click_grid_item(item, "7", 3)
    #sap_b1.do_click_grid_item(item, "7", 4)