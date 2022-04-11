import win32com.client
try:
    from threading import Thread
    from queue import Queue, Empty
except ImportError:
    from Queue import Queue, Empty  

def click_items(*arr_item, click_type = 0):
    try:
        for item in arr_item:
            item.Click(click_type)
        
    except:
        PrintException()


class SAP_B1:
    def __init__(self):
        self.sbo_gui_api = win32com.client.Dispatch("SAPbouiCOM.SboGuiApi") 
        self.connection_string = "0030002C0030002C00530041005000420044005F00440061007400650076002C0050004C006F006D0056004900490056"
        self.sbo_application = None            

    def connect_app(self):
        self.sbo_gui_api.Connect(self.connection_string)
        self.sbo_application = self.sbo_gui_api.GetApplication(-1)

    def login(self, user, pwd, society=None):
        
        form = self.get_form("821")
        form.Items.Item("4").Click(0)
        self.sbo_application.SendKeys(user)
        form.Items.Item("5").Click(0)
        self.sbo_application.SendKeys(pwd)
        print("society")
        if society:
            print("queue")
            q = Queue()
            t = Thread(target=click_items, args=([form.Items.Item("10000103")]), daemon=False)
            t.start()
            form = self.get_form("820")
            form.Items.Item("1470000132").Click(0)
            self.sbo_application.SendKeys(society)
            form.Items.Item("19").Click(0)
            self.sbo_application.SendKeys(user)
            form.Items.Item("20").Click(0)
            self.sbo_application.SendKeys(pwd)
        print("click")
        form.Items.Item("1").Click(0)

    def get_form(self, id_form):
        return self.sbo_application.Forms.GetForm(str(id_form), 0)
    
    def get_specific_item(self, form, item_id):
        return form.Items.Item(str(item_id)).Specific

    def get_item(self, form, item_id):
        return form.Items.Item(str(item_id))

    def do_click_grid_item(self, item, row, column, click_type):
        # item.Columns.Item(str(row)).Cells.Item(int(column)).Click(click_type)
        q = Queue()
        t = Thread(target=click_items, args=(item.Columns.Item(str(column)).Cells.Item(int(row)), click_type), daemon=False)
        t.start()
    
    def do_click_item(self, item, click_type):
        q = Queue()
        t = Thread(target=click_items, args=(item, click_type), daemon=False)
        t.start()
    
    def activate_menu(self, id_menu):
        self.sbo_application.ActivateMenuItem(str(id_menu))
    
    def get_value(self, item, row, column):
        return item.Columns.Item(str(row)).Cells.Item(int(column)).Specific.Value


if __name__ == '__main__':
    import time
    sap_b1 = SAP_B1()
    sap_b1.connect_app()
    form = sap_b1.get_form("133")
    #data_source = form.DataSources
    data_string = sap_b1.get_item(form, "1")
    id_ = data_string.UniqueID
    print(id_)
    form.ActiveItem = id_
    #sap_b1.sbo_application.Click(0)
    #' Check a specific item ID is in focus
    item = form.Items.Item(id_)
    #item.Click(0)
    item_spec = item.Specific

    #Dim bActiveItem As Boolean = oComboBox.Active
    sap_b1.sbo_application.SendKeys("{ENTER}")
    #item_valor = data_string.Columns.Item(str("V_2")).Cells.Item(int(1))
    

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
