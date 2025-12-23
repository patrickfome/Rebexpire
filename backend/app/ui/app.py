import tkinter as tk
from services.storage_service import load_data, save_data

class DocumentsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des documents")
        self.geometry("1000x600")

        self.data = load_data()
        self.build_ui()

    def build_ui(self):
        tk.Label(self, text="Application Documents", font=("Arial", 16)).pack()
