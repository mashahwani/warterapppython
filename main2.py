import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from functions import api_data
from ciities import cities

class App:
    data = api_data(36.23, -23.34)["current_weather"]
    def __init__(self, root):
        #setting title
        root.title("Weather App")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_439=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_439["font"] = ft
        GLabel_439["fg"] = "#000000"
        GLabel_439["justify"] = "center"
        GLabel_439["text"] = "Temperature"
        GLabel_439.place(x=10,y=40,width=166,height=32)

        self.GLabel_17=tk.Label(root)
        ft = tkFont.Font(family='Times',size=58)
        self.GLabel_17["font"] = ft
        self.GLabel_17["fg"] = "#333333"
        self.GLabel_17["justify"] = "center"
        self.GLabel_17["text"] = self.data["temperature"]
        self.GLabel_17.place(x=20,y=60,width=137,height=109)

        GLabel_946=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_946["font"] = ft
        GLabel_946["fg"] = "#333333"
        GLabel_946["justify"] = "center"
        GLabel_946["text"] = "Wind Speed"
        GLabel_946.place(x=200,y=70,width=165,height=34)

        GLabel_643=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_643["font"] = ft
        GLabel_643["fg"] = "#333333"
        GLabel_643["justify"] = "center"
        GLabel_643["text"] = "Wind Direction"
        GLabel_643.place(x=380,y=60,width=120,height=55)

        self.GLabel_155=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        self.GLabel_155["font"] = ft
        self.GLabel_155["fg"] = "#333333"
        self.GLabel_155["justify"] = "center"
        self.GLabel_155["text"] = self.data["windspeed"]
        self.GLabel_155.place(x=240,y=110,width=87,height=40)

        self.GLabel_568=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        self.GLabel_568["font"] = ft
        self.GLabel_568["fg"] = "#333333"
        self.GLabel_568["justify"] = "center"
        self.GLabel_568["text"] = self.data["winddirection"]
        self.GLabel_568.place(x=390,y=120,width=106,height=30)

        GLabel_488=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_488["font"] = ft
        GLabel_488["fg"] = "#333333"
        GLabel_488["justify"] = "center"
        GLabel_488["text"] = "Day/Night"
        GLabel_488.place(x=250,y=170,width=70,height=25)

        GLabel_823=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_823["font"] = ft
        GLabel_823["fg"] = "#333333"
        GLabel_823["justify"] = "center"
        GLabel_823["text"] = "Time"
        GLabel_823.place(x=410,y=170,width=70,height=25)

        self.GLabel_750=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        self.GLabel_750["font"] = ft
        self.GLabel_750["fg"] = "#333333"
        self.GLabel_750["justify"] = "center"
        self.GLabel_750["text"] = self.data["is_day"]
        self.GLabel_750.place(x=220,y=200,width=123,height=48)

        self.GLabel_527=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        self.GLabel_527["font"] = ft
        self.GLabel_527["fg"] = "#333333"
        self.GLabel_527["justify"] = "center"
        self.GLabel_527["text"] = self.data["time"]
        self.GLabel_527.place(x=400,y=210,width=101,height=41)

        self.GLabel_347=tk.Label(root)
        ft = tkFont.Font(family='Times',size=34)
        self.GLabel_347["font"] = ft
        self.GLabel_347["fg"] = "#333333"
        self.GLabel_347["justify"] = "center"
        self.GLabel_347["text"] = "Quetta"
        self.GLabel_347.place(x=0,y=180,width=206,height=81)

        self.combobox_var = tk.StringVar()
        GComboBox_534 = ttk.Combobox(
            root, textvariable=self.combobox_var, font=("Times", 14), justify="center")
        GComboBox_534["values"] = list(cities) # Dropdown values
        GComboBox_534.place(x=70, y=300, width=303, height=43)
        GComboBox_534["state"] = "readonly"  # Prevents manual typing
        GComboBox_534.set("Select a City") 
        # GLineEdit_534=tk.Entry(root)
        # GLineEdit_534["borderwidth"] = "1px"
        # ft = tkFont.Font(family='Times',size=10)
        # GLineEdit_534["font"] = ft
        # GLineEdit_534["fg"] = "#333333"
        # GLineEdit_534["justify"] = "center"
        # GLineEdit_534["text"] = "Enter City Name"
        # GLineEdit_534.place(x=70,y=300,width=303,height=43)

        GButton_269=tk.Button(root)
        GButton_269["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_269["font"] = ft
        GButton_269["fg"] = "#000000"
        GButton_269["justify"] = "center"
        GButton_269["text"] = "Check"
        GButton_269.place(x=380,y=300,width=129,height=39)
        GButton_269["command"] = self.GButton_269_command

    def GButton_269_command(self):
        city = self.combobox_var.get()
        data = api_data(cities[city]["latitude"], cities[city]["longitude"])["current_weather"]
        self.GLabel_17.configure( text=str(data["temperature"]))
        # data["windspeed"]
        # data["winddirection"]
        # data["time"]
        # data["is_day"]
        # print("Button Was clicked.........")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()