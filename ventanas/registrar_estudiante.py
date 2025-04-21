# registrar_estudiante.py

import tkinter as tk
from pygame import mixer #Importar el módulo de pygame para la voz
from tkinter import messagebox
from base_datos import crear_conexion

class RegistrarEstudiante:
    def __init__(self, root, callback):
        """Inicializa la ventana para registrar un nuevo estudiante."""
        self.root = root
        self.callback = callback
        self.root.iconbitmap("img/tecnisitemas.ico")
        self.root.title("Registrar Estudiante")
        self.root.config(bg="white")  # Color de fondo de la ventana principal
        self.root.geometry("900x250")  # Establecer el tamaño de la ventana
        self.crear_widgets()
        
        Registro = "Registro_estudiante.mp3"
        mixer.init()
        mixer.music.load(Registro)
        mixer.music.play()

    def crear_widgets(self):
        """Crea los widgets de la interfaz para ingresar los datos del estudiante."""
        frame = tk.Frame(self.root, bg="#659dff", padx= 50, pady= 10)  # Crear un marco para los campos de búsqueda
        frame.pack(padx= 2, pady=2)  # Empaquetar el marco con un padding vertical de 10 píxeles

        # Etiqueta y campo de entrada para "Nombres"
        tk.Label(frame, text="Nombres:", font=("Helvetica", 15),fg= "white",bg="#17926e").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_nombres = tk.Entry(frame, width=30, font=("Helvetica", 12))
        self.entry_nombres.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y campo de entrada para "Apellidos"
        tk.Label(frame, text="Apellidos:", font=("Helvetica", 15), fg= "white",bg="#17926e").grid(row=0, column=2, padx=10, pady=10, sticky="e")
        self.entry_apellidos = tk.Entry(frame, width=30, font=("Helvetica", 12))
        self.entry_apellidos.grid(row=0, column=3, padx=10, pady=10)

        # Etiqueta y campo de entrada para "Identificación"
        tk.Label(frame, text="Identificación:", font=("Helvetica", 15), fg= "white",bg="#17926e").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_identificacion = tk.Entry(frame, width=30, font=("Helvetica", 12))
        self.entry_identificacion.grid(row=1, column=1, padx=10, pady=10)

        # Etiqueta y campo de entrada para "Edad"
        tk.Label(frame, text="Edad:", font=("Helvetica", 15), fg= "white",bg="#17926e").grid(row=1, column=2, padx=10, pady=10, sticky="e")
        self.entry_edad = tk.Entry(frame, width=30, font=("Helvetica", 12))
        self.entry_edad.grid(row=1, column=3, padx=10, pady=10)

        # Etiqueta y campo de entrada para "Programa"
        tk.Label(frame, text="Programa:", font=("Helvetica", 15), fg= "white",bg="#17926e").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_programa = tk.Entry(frame, width=30, font=("Helvetica", 12))
        self.entry_programa.grid(row=2, column=1, padx=10, pady=10)

        # Frame para los botones
        frame_botones = tk.Frame(self.root, bg="#659dff", padx= 300, pady= 25)  # Crear un marco para los campos de búsqueda
        frame_botones.pack(padx= 2, pady=2)  # Empaquetar el marco con un padding vertical de 10 píxeles

        # Botón para guardar el estudiante
        btn_guardar = tk.Button(
            frame_botones,
            text="Guardar",
            command=self.guardar_estudiante,
            bg="#17926e",
            bd= 3,
            fg="white",
            font=("Comic Sans MS", 12),
            width=15
        )
        btn_guardar.pack(side=tk.LEFT, padx=10)

        # Botón para cancelar
        btn_cancelar = tk.Button(
            frame_botones,
            text="Cancelar",
            command=self.root.destroy,
            bg="#17926e",
            bd= 3,
            fg="white",
            font=("Comic Sans MS", 12),
            width=15
        )
        btn_cancelar.pack(side=tk.LEFT, padx=10)

    def guardar_estudiante(self):
        """Guarda los datos del nuevo estudiante en la base de datos."""
        try:
            nombres = self.entry_nombres.get().strip()
            apellidos = self.entry_apellidos.get().strip()
            identificacion = self.entry_identificacion.get().strip()
            edad = self.entry_edad.get().strip()
            programa = self.entry_programa.get().strip()

            if not nombres or not apellidos or not identificacion or not edad or not programa:
                messagebox.showerror("Error", "Todos los campos deben estar llenos.")
                return

            edad = int(edad)

            conexion = crear_conexion()
            if conexion is not None:
                cursor = conexion.cursor()
                cursor.execute("""
                    INSERT INTO estudiantes (nombres, apellidos, identificacion, edad, programa) 
                    VALUES (?, ?, ?, ?, ?)
                """, (nombres, apellidos, identificacion, edad, programa))
                conexion.commit()
                conexion.close()

                self.callback()
                messagebox.showinfo("Éxito", "Registro guardado exitosamente.")
                self.root.destroy()
            else:
                messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "La identificación ya existe. Ingrese una identificación única.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el estudiante: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrarEstudiante(root, lambda: None)
    root.mainloop()