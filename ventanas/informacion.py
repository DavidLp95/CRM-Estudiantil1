import tkinter as tk
from tkinter import font
from pygame import mixer #Importar el módulo de pygame para la voz

class Informacion:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap("img/tecnisitemas.ico")
        self.root.title("Información")
        self.root.config(bg= "#659dff")
        self.root.geometry("500x300")  # Establecer tamaño de la ventana
        self.crear_widgets()
        
        Creditos = "Creditos.mp3"
        mixer.init()
        mixer.music.load(Creditos)
        mixer.music.play()

    def crear_widgets(self):
        # Crear un marco con borde decorativo
        frame = tk.Frame(self.root, padx=20, pady=20, bd=5, relief=tk.GROOVE, bg="#17926e")
        frame.pack(pady=30, padx=30, fill="both", expand=True)

        # Fuente en negrita para el título
        bold_font = font.Font(family="Helvetica", size=14, weight="bold")
        # Fuente normal para el resto del texto
        normal_font = font.Font(family="Helvetica", size=12)

        # Crear y mostrar el título en negrita
        label_title = tk.Label(frame, text="Proyecto Técnicos en Sistemas", font=bold_font, fg="white", bg="#17926e")
        label_title.pack(pady=(0, 10))  # Espaciado solo abajo

        # Crear y mostrar el resto del texto en fuente normal
        label_info1 = tk.Label(frame, text="Instituto Tecnisistemas", font=normal_font, fg="white", bg="#17926e")
        label_info1.pack(pady=5)

        label_info2 = tk.Label(frame, text="Sistema de Notas V 1.0", font=normal_font, fg="white", bg="#17926e")
        label_info2.pack(pady=5)

        label_info3 = tk.Label(frame, text="Estudiantes: Anamaria Rodriguez \n                     David Niño \n                  Diego Vásquez", font=normal_font, fg="white", bg="#17926e")
        label_info3.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = Informacion(root)
    root.mainloop()