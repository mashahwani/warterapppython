import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import ttk
from functions import api_data
from ciities import cities


class App:
    data = api_data(30.18, 66.99)[
    "current_weather"]
    def __init__(self, root):
        # setting title
        root.title("Weather App")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_70 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        GLabel_70["font"] = ft
        GLabel_70["fg"] = "#333333"
        GLabel_70["justify"] = "center"
        GLabel_70["text"] = "Temprature"
        GLabel_70.place(x=50, y=40, width=71, height=30)

        self.GLabel_984 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=43)
        self.GLabel_984["font"] = ft
        self.GLabel_984["fg"] = "#333333"
        self.GLabel_984["justify"] = "center"
        self.GLabel_984["text"] = self.data["temperature"] or "-"
        self.GLabel_984.place(x=10, y=70, width=154, height=69)

        GLabel_870 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        GLabel_870["font"] = ft
        GLabel_870["fg"] = "#333333"
        GLabel_870["justify"] = "center"
        GLabel_870["text"] = "Wind Speed"
        GLabel_870.place(x=250, y=50, width=85, height=30)

        GLabel_534 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        GLabel_534["font"] = ft
        GLabel_534["fg"] = "#333333"
        GLabel_534["justify"] = "center"
        GLabel_534["text"] = "Wind Direction"
        GLabel_534.place(x=390, y=50, width=103, height=30)

        self.GLabel_384 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        self.GLabel_384["font"] = ft
        self.GLabel_384["fg"] = "#333333"
        self.GLabel_384["justify"] = "center"
        self.GLabel_384["text"] = self.data["windspeed"] or "-"
        self.GLabel_384.place(x=250, y=90, width=70, height=25)

        self.GLabel_215 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        self.GLabel_215["font"] = ft
        self.GLabel_215["fg"] = "#333333"
        self.GLabel_215["justify"] = "center"
        self.GLabel_215["text"] = self.data["winddirection"] or "-"
        self.GLabel_215.place(x=400, y=90, width=70, height=25)

        GLabel_865 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        GLabel_865["font"] = ft
        GLabel_865["fg"] = "#333333"
        GLabel_865["justify"] = "center"
        GLabel_865["text"] = "Day/Night"
        GLabel_865.place(x=250, y=130, width=70, height=25)

        GLabel_584 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        GLabel_584["font"] = ft
        GLabel_584["fg"] = "#333333"
        GLabel_584["justify"] = "center"
        GLabel_584["text"] = "Time"
        GLabel_584.place(x=400, y=130, width=70, height=25)

        self.GLabel_743 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        self.GLabel_743["font"] = ft
        self.GLabel_743["fg"] = "#333333"
        self.GLabel_743["justify"] = "center"
        self.GLabel_743["text"] = (self.data and (
            self.data["is_day"] and "Day" or "Night")) or "-"
        self.GLabel_743.place(x=250, y=170, width=70, height=25)

        self.GLabel_408 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        self.GLabel_408["font"] = ft
        self.GLabel_408["fg"] = "#333333"
        self.GLabel_408["justify"] = "center"
        self.GLabel_408["text"] = self.data["time"] or "-"
        self.GLabel_408.place(x=400, y=170, width=70, height=25)

        self.GLabel_960 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=34)
        self.GLabel_960["font"] = ft
        self.GLabel_960["fg"] = "#333333"
        self.GLabel_960["justify"] = "center"
        self.GLabel_960["text"] = "Quetta"
        self.GLabel_960.place(x=10, y=150, width=177, height=63)

        self.combobox_var = tk.StringVar()
        GComboBox_368 = ttk.Combobox(
            root, textvariable=self.combobox_var, font=("Helvetica", 14))
        GComboBox_368["values"] = list(cities)  # Values for the dropdown
        GComboBox_368.place(x=130, y=240, width=238, height=37)
        GComboBox_368["state"] = "readonly"  # Prevents manual typing
        GComboBox_368.set("Select an option")  # Default display text

        GButton_519 = tk.Button(root)
        GButton_519["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_519["font"] = ft
        GButton_519["fg"] = "#000000"
        GButton_519["justify"] = "center"
        GButton_519["text"] = "Check"
        GButton_519.place(x=380, y=240, width=106, height=34)
        GButton_519["command"] = self.GButton_519_command

    def on_click(self):
        messagebox.showerror('Error', 'Invalid City Name')
    
    def GButton_519_command(self):
        selected_option = self.combobox_var.get()
        try:
            new_data = api_data(cities[selected_option]["latitude"], cities[selected_option]["longitude"])[
            "current_weather"]
            self.GLabel_984.configure(text=new_data["temperature"])
            self.GLabel_960.configure(text=selected_option)
            self.GLabel_215.configure(text=new_data["winddirection"])
            self.GLabel_384.configure(text=new_data["windspeed"])
            self.GLabel_408.configure(text=new_data["time"])
        except KeyError:
            self.on_click()
            # label = tk.Label(root, text="Click the button to show the message ",
            # font=('Calibri 15 bold'))
            # label.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
