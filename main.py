# from functions import api_data
import tkinter as tk


# data = api_data(30.18, 66.99)
# if data == 400 or data == 404:
#     print("Bad Request...!")
# else:
#     print(data)

root = tk.Tk()
root.title("Weather App")
# root.geometry("500x400")

main_frame = tk.Frame(root)
main_frame.pack()

row_1 = tk.Frame(main_frame )
row_1.grid(row=0,column=0, padx=50, pady=50)

row_1_col_1 = tk.Frame(row_1)
row_1_col_2 = tk.Frame(row_1)
row_1_col_1.grid(row=0,column=0)
row_1_col_2.grid(row=0,column=1, padx=60, pady=5)

row_2 = tk.Frame(main_frame)
row_2.grid(row=1,column=0, pady=20)




# Adding Label for temprature
temprature = tk.Label(row_1_col_1, text="Temprature", font=("Helvetica", 14))
temprature.grid(row=0,column=0, padx=5, pady=5)
degree = tk.Label(row_1_col_1, text="45\u00b0C", font=("Arial", 40))
degree.grid(row=1,column=0, padx=5, pady=5)

# Other factors label
wind_speed_label = tk.Label(row_1_col_2, text="Wind Speed", font=("Helvetica", 11))
wind_speed_label.grid(row=0,column=0)
spacer_label = tk.Label(row_1_col_2, text="", width=5)
spacer_label.grid(row=0, column=1)
wind_direction_label = tk.Label(row_1_col_2, text="Wind Direction", font=("Helvetica", 11))
wind_direction_label.grid(row=0,column=2)

wind_speed = tk.Label(row_1_col_2, text="50.23", font=("Arial", 11, "bold"))
wind_speed.grid(row=1,column=0, padx=5, pady=5)
spacer_label = tk.Label(row_1_col_2, text="", width=5)
spacer_label.grid(row=1, column=1)
wind_direction = tk.Label(row_1_col_2, text="290", font=("Arial", 11, "bold"))
wind_direction.grid(row=1,column=2, padx=5, pady=5)

humidity_label = tk.Label(row_1_col_2, text="Wind Speed", font=("Helvetica", 11))
humidity_label.grid(row=2,column=0)
spacer_label = tk.Label(row_1_col_2, text="", width=5)
spacer_label.grid(row=2, column=1)
timezone_label = tk.Label(row_1_col_2, text="Wind Direction", font=("Helvetica", 11))
timezone_label.grid(row=2,column=2)

humidity = tk.Label(row_1_col_2, text="50", font=("Helvetica", 11, "bold"))
humidity.grid(row=3,column=0, padx=5, pady=5)
spacer_label = tk.Label(row_1_col_2, text="", width=5)
spacer_label.grid(row=3, column=1)
timezone = tk.Label(row_1_col_2, text="204", font=("Helvetica", 11, "bold"))
timezone.grid(row=3,column=2, padx=5, pady=5)



city = tk.Label(row_2, text="Quetta", font=("Impact", 36, "bold"))
city.grid(row=1, column=0)
entry = tk.Entry(row_2, width=30, font=("Helvetica", 12))
entry.grid(row=2, column=0)
submit_button = tk.Button(row_2, text="Submit")
submit_button.grid(row=2,column=1)


root.mainloop()

    