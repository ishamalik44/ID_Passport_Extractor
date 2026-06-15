import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

from gui.main_window import MainWindow

app = MainWindow()
app.mainloop()