import customtkinter
from tkinter import PhotoImage

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

logo = PhotoImage(file="inge.png")

root.geometry("500x600+350+20")
root.minsize(400,500)
root.title("Data Saver: INGEMOTIONS")
root.iconbitmap("inge.ico")

def sliderprint():
    print(slider._output_value)

#Crear una barra de valor
slider = customtkinter.CTkSlider(root, from_=0, to=100)
slider.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(root, text="Value", command=sliderprint)
button.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)



root.mainloop()