import tkinter as tk  # Importar el módulo tkinter para la interfaz gráfica
from pygame import mixer #Importar el módulo de pygame para la voz
from tkinter import ttk, messagebox  # Importar ttk para widgets avanzados y messagebox para diálogos de mensajes
from base_datos import crear_conexion  # Importar la función crear_conexion desde base_datos.py

class RegistrarNotas:
    def __init__(self, root, callback):
        """Inicializa la ventana para registrar notas de un estudiante."""
        self.root = root  # Asignar la raíz de Tkinter a self.root
        self.root.iconbitmap("img/tecnisitemas.ico")
        self.callback = callback  # Asignar la función callback para actualizar datos
        self.root.title("Registrar Notas")  # Establecer el título de la ventana
        self.root.geometry("1000x600")  # Aumentar el tamaño de la ventana
        self.root.config(bg="white")  # Color de fondo de la ventana principal
        self.crear_widgets()  # Llamar a la función para crear los widgets de la interfaz
        
        Notas = "Notas_estudiante.mp3"
        mixer.init()
        mixer.music.load(Notas)
        mixer.music.play()

    def crear_widgets(self):
        """Crea los widgets de la interfaz para buscar y registrar notas."""
        # Crear frame para la búsqueda de estudiante
        frame_buscar = tk.Frame(self.root, bg="#659dff", padx= 80, pady= 10)  # Crear un marco para los campos de búsqueda
        frame_buscar.pack(padx= 2, pady=2)  # Empaquetar el marco con un padding vertical de 10 píxeles

        # Etiqueta y campo de entrada para buscar estudiante
        tk.Label(frame_buscar, text="Buscar estudiante (Nombre o Identificación):", fg= "white",bg="#659dff", font=("Helvetica", 16),).pack(side="left", padx=5)
        self.entry_buscar = tk.Entry(frame_buscar, font=("Helvetica", 13), width=30)  # Campo de entrada agrandado
        self.entry_buscar.pack(side="left", padx=4)
        btn_buscar = tk.Button(
            frame_buscar,
            text="Buscar",
            command=self.buscar_estudiante,
            bg="#17926e",
            bd= 3,
            fg="white",
            font=("Comic Sans MS", 12),
            width=10
        )
        btn_buscar.pack(side="left", padx=5)

        # Crear tabla (Treeview) para mostrar los datos de los estudiantes encontrados
        self.tree = ttk.Treeview(
            self.root,
            columns=("Nombres", "Apellidos", "Identificación", "Edad", "Programa"),
            show='headings'
        )
        self.tree.heading("Nombres", text="Nombres")
        self.tree.heading("Apellidos", text="Apellidos")
        self.tree.heading("Identificación", text="Identificación")
        self.tree.heading("Edad", text="Edad")
        self.tree.heading("Programa", text="Programa")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        for col in self.tree["columns"]:
            self.tree.column(col, width=150)

        # Crear frame para ingresar las notas
        frame_notas = tk.Frame(self.root, bg="#659dff", padx= 350, pady= 10)
        frame_notas.pack(pady=5)

        #Etiqueta y campo de entrada para cada nota, organizados en pares horizontalmente
        tk.Label(frame_notas, text="Nota 1:", font=("Helvetica", 15), fg= "white",bg="#17926e").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nota1 = tk.Entry(frame_notas, font=("Helvetica", 12), width=10)
        self.entry_nota1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_notas, text="Nota 2:", font=("Helvetica", 15), fg= "white",bg="#17926e").grid(row=0, column=2, padx=5, pady=5)
        self.entry_nota2 = tk.Entry(frame_notas, font=("Helvetica", 12), width=10)
        self.entry_nota2.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_notas, text="Nota 3:", font=("Helvetica", 15), fg= "white",bg="#17926e").grid(row=1, column=0, padx=5, pady=5)
        self.entry_nota3 = tk.Entry(frame_notas, font=("Helvetica", 12), width=10)
        self.entry_nota3.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_notas, text="Nota 4:", font=("Helvetica", 15), fg= "white",bg="#17926e").grid(row=1, column=2, padx=5, pady=5)
        self.entry_nota4 = tk.Entry(frame_notas, font=("Helvetica", 12), width=10)
        self.entry_nota4.grid(row=1, column=3, padx=5, pady=5)

        # Botón para guardar las notas, debajo de los campos de notas
        btn_guardar = tk.Button(
            self.root,
            text="Guardar Notas",
            command=self.guardar_notas,
            bg="#17926e",
            bd= 3,
            fg="white",
            font=("Comic Sans MS", 12),
            width=15
        )
        btn_guardar.pack(pady=10)

    def buscar_estudiante(self):
        """Busca estudiantes por nombre o identificación y muestra los resultados en la tabla."""
        try:
            conexion = crear_conexion()  # Crear conexión a la base de datos
            if conexion is not None:
                cursor = conexion.cursor()  # Crear un cursor para ejecutar comandos SQL
                query = "SELECT nombres, apellidos, identificacion, edad, programa FROM estudiantes WHERE nombres LIKE ? OR identificacion LIKE ?"  # Definir la consulta SQL
                criterio = self.entry_buscar.get().strip()  # Obtener y limpiar el criterio de búsqueda
                if not criterio:
                    # Si el criterio de búsqueda está vacío, mostrar mensaje de error
                    messagebox.showerror("Error", "Ingrese un criterio de búsqueda.")
                    return  # Salir de la función
                cursor.execute(query, ('%' + criterio + '%', '%' + criterio + '%'))  # Ejecutar la consulta SQL con el criterio
                rows = cursor.fetchall()  # Obtener todos los resultados de la consulta

                # Limpiar la tabla antes de mostrar los resultados
                for row in self.tree.get_children():
                    self.tree.delete(row)  # Eliminar cada fila existente en la tabla

                if rows:
                    for row in rows:
                        self.tree.insert("", tk.END, values=row)  # Insertar cada fila en la tabla
                else:
                    messagebox.showinfo("Información", "No se encontraron registros.")  # Mostrar mensaje si no hay resultados
                conexion.close()  # Cerrar la conexión a la base de datos
            else:
                messagebox.showerror("Error", "No se pudo conectar a la base de datos.")  # Mostrar mensaje de error si la conexión falla
        except sqlite3.Error as e:
            # Mostrar mensaje de error en caso de excepción
            messagebox.showerror("Error", f"Error al buscar estudiantes: {e}")

    def guardar_notas(self):
        """Guarda las notas ingresadas para el estudiante seleccionado."""
        try:
            selected_item = self.tree.selection()  # Obtener el ítem seleccionado en la tabla
            if not selected_item:
                # Si no se ha seleccionado ningún ítem, mostrar mensaje de error
                messagebox.showerror("Error", "Seleccione un registro para registrar las notas.")
                return  # Salir de la función

            # Obtener los datos del ítem seleccionado
            item = self.tree.item(selected_item)
            identificacion = item['values'][2]  # Obtener la identificación del estudiante

            # Obtener y validar las notas ingresadas
            nota1 = self.entry_nota1.get().strip()
            nota2 = self.entry_nota2.get().strip()
            nota3 = self.entry_nota3.get().strip()
            nota4 = self.entry_nota4.get().strip()

            if not nota1 or not nota2 or not nota3 or not nota4:
                # Si alguna nota está vacía, mostrar mensaje de error
                messagebox.showerror("Error", "Todos los campos de notas deben estar llenos.")
                return  # Salir de la función

            # Convertir las notas a float
            nota1 = float(nota1)
            nota2 = float(nota2)
            nota3 = float(nota3)
            nota4 = float(nota4)

            # Calcular el promedio
            promedio = (nota1 + nota2 + nota3 + nota4) / 4

            conexion = crear_conexion()  # Crear conexión a la base de datos
            if conexion is not None:
                cursor = conexion.cursor()  # Crear un cursor para ejecutar comandos SQL
                # Ejecutar consulta SQL para actualizar las notas y el promedio del estudiante
                cursor.execute("""
                    UPDATE estudiantes 
                    SET nota1=?, nota2=?, nota3=?, nota4=?, promedio=? 
                    WHERE identificacion=?
                """, (nota1, nota2, nota3, nota4, promedio, identificacion))
                conexion.commit()  # Confirmar los cambios en la base de datos
                conexion.close()  # Cerrar la conexión a la base de datos

                self.callback()  # Llamar a la función callback para actualizar los datos en la tabla principal
                messagebox.showinfo("Éxito", "Notas registradas exitosamente.")  # Mostrar mensaje de éxito
                self.root.destroy()  # Cerrar la ventana de registro de notas
            else:
                messagebox.showerror("Error", "No se pudo conectar a la base de datos.")  # Mostrar mensaje de error si la conexión falla
        except ValueError:
            # Mostrar mensaje de error si hay problemas con la conversión de tipos
            messagebox.showerror("Error", "Las notas deben ser números válidos.")
        except sqlite3.Error as e:
            # Mostrar mensaje de error en caso de excepción
            messagebox.showerror("Error", f"Error al guardar las notas: {e}")

# Código para ejecutar el script directamente (opcional)
if __name__ == "__main__":
    root = tk.Tk()  # Crear una instancia de Tkinter
    app = RegistrarNotas(root, lambda: None)  # Crear una instancia de RegistrarNotas con una función callback vacía
    root.mainloop()  # Iniciar el bucle principal de la interfaz gráfica