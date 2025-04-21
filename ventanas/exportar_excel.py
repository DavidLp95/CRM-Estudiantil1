import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import sqlite3

# Función para crear la conexión a la base de datos
def crear_conexion():
    try:
        return sqlite3.connect("mi_base_de_datos.db")
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

class exportar_excel:
    def _init_(self, root):
        self.root = root
        self.root.title("Gestión de Estudiantes")

        # Crear tabla (Treeview) para mostrar los datos
        self.tree = ttk.Treeview(
            self.root,
            columns=("Nombres", "Apellidos", "Identificación", "Edad", "Programa"),
            show="headings",
        )
        
        self.tree.heading("Nombres", text="Nombres")
        self.tree.heading("Apellidos", text="Apellidos")
        self.tree.heading("Identificación", text="Identificación")
        self.tree.heading("Edad", text="Edad")
        self.tree.heading("Programa", text="Programa")
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

        for col in self.tree["columns"]:
            self.tree.column(col, width=150)

        # Botón para cargar datos
        self.load_button = tk.Button(self.root, text="Cargar Datos", command=self.cargar_datos)
        self.load_button.pack(pady=10)

        # Botón para exportar a Excel
        self.export_button = tk.Button(self.root, text="Exportar a Excel", command=self.exportar_a_excel)
        self.export_button.pack(pady=10)

    def cargar_datos(self):
        """Carga los datos de los estudiantes desde la base de datos y los muestra en la tabla."""
        try:
            for row in self.tree.get_children():
                self.tree.delete(row)  # Limpiar la tabla eliminando todas las filas existentes

            conexion = crear_conexion()
            if conexion is not None:
                cursor = conexion.cursor()
                cursor.execute("""
                    SELECT nombres, apellidos, identificacion, edad, programa
                    FROM estudiantes
                """)
                for row in cursor.fetchall():
                    self.tree.insert("", tk.END, values=row)
                conexion.close()
            else:
                messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los datos: {e}")

    def exportar_a_excel(self):
        """Exporta los datos de la tabla a un archivo Excel."""
        try:
            # Obtener datos de la tabla
            datos = [self.tree.item(row)["values"] for row in self.tree.get_children()]
            if not datos:
                messagebox.showwarning("Aviso", "No hay datos para exportar.")
                return
            
            # Crear un DataFrame con los datos
            columnas = ("Nombres", "Apellidos", "Identificación", "Edad", "Programa")
            df = pd.DataFrame(datos, columns=columnas)

            # Guardar el archivo Excel
            ruta_archivo = "datos_estudiantes.xlsx"
            df.to_excel(ruta_archivo, index=False)

            messagebox.showinfo("Éxito", f"Datos exportados correctamente a {ruta_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar a Excel: {e}")

# Crear la ventana principal
if _name_ == "_main_":
    root = tk.Tk()
    app = exportar_excel(root)
    root.mainloop()