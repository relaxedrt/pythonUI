import customtkinter
from tkinter import PhotoImage

root = customtkinter.CTk()

root.geometry("500x600+350+20")
root.minsize(400,500)
root.config(bg= "#22272e",)
root.title("Data Saver: INGEMOTIONS")
root.iconbitmap("inge.ico")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root, text="Inicio de turno", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

root.mainloop()