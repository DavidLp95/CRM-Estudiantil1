# ventana_principal.py
import pandas as pd
import tkinter as tk  # Importar el módulo tkinter para crear interfaces gráficas
from tkinter import ttk, messagebox  # Importar ttk para widgets avanzados y messagebox para cuadros de diálogo de mensajes
from base_datos import crear_conexion  # Importar la función para conectar con la base de datos

class VentanaPrincipal:
    def __init__(self, root):
        """Inicializa la ventana principal del sistema de notas."""
        self.root = root  # Asignar el objeto Tk (ventana principal) a una variable de instancia
        self.root.iconbitmap("img/tecnisitemas.ico")
        self.root.title("Sistema de Notas")
        self.root.config(bg="gray")   # Establecer el título de la ventana principal
        self.crear_menu()  # Llamar al método para crear el menú de la interfaz
        self.crear_widgets()  # Llamar al método para crear los widgets de la interfaz
        self.cargar_datos()  # Llamar al método para cargar los datos de la base de datos


    def crear_menu(self):
        """Crea la barra de menú en la ventana principal."""
        menubar = tk.Menu(self.root, font=("Helvetica", 12))  # Crear una barra de menú con fuente Helvetica tamaño 12
        self.root.config(menu=menubar)  # Configurar la ventana principal para usar la barra de menú

        # Crear menú de opciones "Inicio"
        inicio_menu = tk.Menu(menubar, tearoff=0, font=("Helvetica", 12))  # Crear un submenú "Inicio"
        menubar.add_cascade(label="Inicio", menu=inicio_menu)  # Añadir el submenú "Inicio" a la barra de menú
        inicio_menu.add_command(label="Eliminar base de datos", command=self.eliminar_bd)  # Añadir opción para eliminar la base de datos
        inicio_menu.add_command(label="Salir", command=self.root.quit)  # Añadir opción para salir de la aplicación

        # Crear menú de opciones "Registrar"
        registrar_menu = tk.Menu(menubar, tearoff=0, font=("Helvetica", 12))  # Crear un submenú "Registrar"
        menubar.add_cascade(label="Registrar", menu=registrar_menu)  # Añadir el submenú "Registrar" a la barra de menú
        registrar_menu.add_command(label="Registrar estudiante", command=self.registrar_estudiante)  # Añadir opción para registrar estudiantes
        registrar_menu.add_command(label="Registrar notas", command=self.registrar_notas)  # Añadir opción para registrar notas

        # Crear menú de ayuda
        ayuda_menu = tk.Menu(menubar, tearoff=0, font=("Helvetica", 12))  # Crear un submenú "Ayuda"
        menubar.add_cascade(label="Ayuda", menu=ayuda_menu)  # Añadir el submenú "Ayuda" a la barra de menú
        ayuda_menu.add_command(label="Información", command=self.mostrar_informacion)  # Añadir opción para mostrar información

    def crear_widgets(self): 
        """Crea los widgets de la interfaz, incluyendo botones y la tabla de datos."""
           
        # Crear frame y tabla en donde se  mostrará los datos de los estudiantes
        frame_tabla = tk.Frame(self.root, bd=2, relief=tk.SOLID, padx=10, pady=10) # Configurar marco con bordes sólidos
        frame_tabla.pack(pady=20, fill=tk.BOTH, expand=True) # Empaquetar y expandir el marco para la tabla

        # Crear tabla (Treeview) para mostrar los datos de los estudiantes
        self.tree = ttk.Treeview(
            frame_tabla,
            columns=("Nombres", "Apellidos", "Identificación", "Edad", "Programa", "N1", "N2", "N3", "N4", "Promedio"),
            show='headings'
        )
        # Configurar encabezados de la tabla
        self.tree.heading("Nombres", text="Nombres")
        self.tree.heading("Apellidos", text="Apellidos")
        self.tree.heading("Identificación", text="Identificación")
        self.tree.heading("Edad", text="Edad")
        self.tree.heading("Programa", text="Programa")
        self.tree.heading("N1", text="Nota 1")
        self.tree.heading("N2", text="Nota 2")
        self.tree.heading("N3", text="Nota 3")
        self.tree.heading("N4", text="Nota 4")
        self.tree.heading("Promedio", text="Promedio")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True) # Empaquetar la tabla dentro del marco

        # Configurar las columnas de la tabla con un ancho de 100 píxeles
        for col in self.tree["columns"]:
            self.tree.column(col, width=100)

        # Configurar el estilo de la tabla
        style = ttk.Style()
        style.configure("Treeview", background="#7fc4c4", foreground="black", rowheight=25, fieldbackground="lightblue")
        style.map("Treeview", background=[('selected', '#17926e')])

        # Crear frame para los botones CRUD

        frame_botones = tk.Frame(self.root, bg="#659dff", padx= 350, pady= 10)  # Crear un marco para los botones
        frame_botones.pack(padx= 2, pady=2)  # Empaquetar el marco con un padding vertical de 10 píxeles

        # Botón de búsqueda de estudiante
        btn_buscar = tk.Button(
            frame_botones,
            text="Buscar",
            command=self.buscar_estudiante,
            bg="#17926e",
            fg="white",
            font=("Comic Sans MS", 12),
            width=15
        )
        btn_buscar.grid(row=0, column=0, padx=10, pady=5) # Colocar el botón en una cuadrícula dentro del marco

        # Botón de edición de estudiante
        btn_editar = tk.Button(
            frame_botones,
            text="Editar",
            command=self.editar_estudiante,
            bg="#17926e",
            fg="white",
            font=("Comic Sans MS", 12),
            width=15
        )
        btn_editar.grid(row=0, column=1, padx=10, pady=5) # Colocar el botón en la cuadrícula en columna 1

        # Botón de eliminación de estudiante
        btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar",
            command=self.eliminar_estudiante,
            bg="#17926e",
            fg="white",
            font=("Comic Sans MS", 12),
            width=15
        )
        btn_eliminar.grid(row=0, column=2, padx=10, pady=5)  # Colocar el botón en la cuadrícula en columna 2

        # Botón de actualización de datos
        btn_actualizar = tk.Button(
            frame_botones,
            text="Actualizar",
            command=self.cargar_datos,
            bg="#17926e",
            fg="white",
            font=("Comic Sans MS", 12),
            width=15
        )
        btn_actualizar.grid(row=0, column=3, padx=10, pady=5) # Colocar el botón en la cuadrícula en columna 3

          #boton de descarga hoja excel
        btn_descarga = tk.Button(
            frame_botones,
            text="Descarga excel",
            command = self.exportar_excel,
            bg="#17926e",
            fg="white",
            font=("Comic Sans MS", 12),
            width=15
            
        )
        btn_descarga.grid(row=0, column=3, padx=10, pady=5)# Colocar el botón en la cuadrícula en columna 4

    
    def cargar_datos(self):
        """Carga los datos de los estudiantes desde la base de datos y los muestra en la tabla."""
        try:
            for row in self.tree.get_children():
                self.tree.delete(row) # Limpiar la tabla eliminando todas las filas existentes

            conexion = crear_conexion() # Crear la conexión con la base de datos
            if conexion is not None:
                cursor = conexion.cursor() # Crear un cursor para ejecutar consultas SQL
                cursor.execute("""
                    SELECT nombres, apellidos, identificacion, edad, programa, 
                           COALESCE(nota1, ''), COALESCE(nota2, ''), 
                           COALESCE(nota3, ''), COALESCE(nota4, ''), 
                           COALESCE(promedio, '') 
                    FROM estudiantes
                """)
                for row in cursor.fetchall(): # Insertar cada registro en la tabla de Treeview
                    self.tree.insert("", tk.END, values=row)
                conexion.close() # Cerrar la conexión con la base de datos
            else:
                messagebox.showerror("Error", "No se pudo conectar a la base de datos.") # Mostrar error si falla la conexión
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los datos: {e}") # Mostrar mensaje de error

           #"""Exporta los datos mostrados en el TreeView a un archivo Excel."""
    #"""Exporta los datos mostrados en el TreeView a un archivo Excel."""
    def exportar_excel(self):
        # Extraer los datos del TreeView
        try:
            datos = []
            for row in self.tree.get_children():
                # Verificar si hay datos para exportar
                datos.append(self.tree.item(row)["values"])
                
            if not datos:
                messagebox.showwarning("Advertencia", "No hay datos para exportar.")
                return

        # Definir los nombres de las columnas
            columnas = ["Nombres", "Apellidos", "Identificación", "Edad", "Programa", "N1", "N2", "N3", "N4", "Promedio"]

        # Crear un DataFrame con los datos
            df = pd.DataFrame(datos, columns=columnas)

        # Guardar el DataFrame en un archivo Excel
            archivo_excel = "datos_estudiantes.xlsx"
            df.to_excel(archivo_excel, index=False, engine='openpyxl')

        # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", f"Datos exportados a {archivo_excel}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar a Excel: {e}")
    def eliminar_bd(self):
        """Función para eliminar la base de datos (Implementación pendiente)."""
        pass  # Placeholder para la función

    def registrar_estudiante(self):
        """Abre la ventana para registrar un nuevo estudiante."""
        try:
            import ventanas.registrar_estudiante as registrar_estudiante # Importar ventana para registrar estudiante
            registrar_estudiante.RegistrarEstudiante(tk.Toplevel(self.root), self.cargar_datos) # Crear ventana
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar estudiante: {e}") # Mostrar error si ocurre un problema

    def registrar_notas(self):
        """Abre la ventana para registrar notas de un estudiante."""
        try:
            import ventanas.registrar_notas as registrar_notas # Importar ventana para registrar notas
            registrar_notas.RegistrarNotas(tk.Toplevel(self.root), self.cargar_datos) # Crear y abrir la ventana para registrar notas
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar notas: {e}") # Mostrar error si ocurre un problema

    def mostrar_informacion(self):
        """Muestra una ventana con información sobre la aplicación."""
        try:
            import ventanas.informacion as informacion # Importar el módulo de la ventana de información
            informacion.Informacion(tk.Toplevel(self.root)) # Crear y abrir la ventana de información
        except Exception as e:
            messagebox.showerror("Error", f"Error al mostrar información: {e}") # Mostrar un mensaje de error si ocurre un problema

    def buscar_estudiante(self):
        """Abre una ventana para buscar estudiantes por nombre o identificación."""
        buscar_ventana = tk.Toplevel(self.root) # Crear una nueva ventana secundaria
        buscar_ventana.iconbitmap("img/tecnisitemas.ico")
        buscar_ventana.title("Buscar Estudiante") # Establecer el título de la ventana
        buscar_ventana.geometry("400x300")
        self.root.config(bg="#659dff")

        tk.Label(buscar_ventana, text="Buscar por Nombre o Identificación:",fg= "white",bg="#659dff").pack(pady=10) # Etiqueta para el campo de búsqueda
        entry_buscar = tk.Entry(buscar_ventana, width=40) # Campo de entrada para el criterio de búsqueda
        entry_buscar.pack(pady=10) # Empaquetar el campo de entrada en la ventana

        def realizar_busqueda():
            query = entry_buscar.get().strip() # Obtener y limpiar el criterio de búsqueda
            if not query:
                messagebox.showerror("Error", "Debe ingresar un criterio de búsqueda.") # Mostrar error si el campo está vacío
                return

            try:
                for row in self.tree.get_children():
                    self.tree.delete(row) # Limpiar la tabla antes de realizar la búsqueda

                conexion = crear_conexion() # Crear conexión a la base de datos
                if conexion is not None:
                    cursor = conexion.cursor() # Crear un cursor para ejecutar consultas
                    cursor.execute("""
                        SELECT nombres, apellidos, identificacion, edad, programa, 
                               COALESCE(nota1, ''), COALESCE(nota2, ''), 
                               COALESCE(nota3, ''), COALESCE(nota4, ''), 
                               COALESCE(promedio, '') 
                        FROM estudiantes 
                        WHERE nombres LIKE ? OR identificacion LIKE ?
                    """, ('%' + query + '%', '%' + query + '%')) # Ejecutar consulta para buscar estudiantes
                    resultados = cursor.fetchall() # Obtener todos los resultados de la consulta

                    if resultados:
                        for row in resultados:
                            self.tree.insert("", tk.END, values=row) # Insertar los resultados en la tabla
                    else:
                        messagebox.showinfo("Información", "No se encontraron registros.")  # Mostrar mensaje si no hay resultados
                    conexion.close()
                else:
                    messagebox.showerror("Error", "No se pudo conectar a la base de datos.") # Mostrar error si no se puede conectar

                buscar_ventana.destroy() # Cerrar la ventana de búsqueda
            except Exception as e:
                messagebox.showerror("Error", f"Error al realizar la búsqueda: {e}") # Mostrar error si ocurre un problema

 
         # Crear un frame para organizar los botones
        frame_botones = tk.Frame(buscar_ventana)
        frame_botones.pack(pady=20)
        
        btn_buscar = tk.Button(
            buscar_ventana,
            text="Buscar",
            command=realizar_busqueda,
            bg="#17926e",
            fg="white",
            font=("Comic Sans MS", 12),
            width=15
        ) # Botón para iniciar la búsqueda
        
        btn_buscar.pack(pady=10) # Empaquetar el botón en la ventana

        btn_cancelar = tk.Button(
            buscar_ventana,
            text="Cancelar",
            command=buscar_ventana.destroy,
            bg="#17926e",
             fg="white",
            font=("Comic Sans MS", 12),
             width=15
         )
        
        btn_cancelar.pack(pady=10) 

        
    def editar_estudiante(self):
        """Abre una ventana para editar los datos de un estudiante seleccionado."""
        selected_item = self.tree.selection()  # Obtener el elemento seleccionado en la tabla
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un registro para editar.")  # Mostrar error si no hay selección
            return

        try:
            item = self.tree.item(selected_item) # Obtener los datos del elemento seleccionado
            datos = item['values'] # Extraer los valores de los datos
            editar_ventana = tk.Toplevel(self.root) # Crear una nueva ventana secundaria
            editar_ventana.iconbitmap("img/tecnisitemas.ico")
            editar_ventana.title("Editar Estudiante") # Establecer el título de la ventana

            labels = ["Nombres", "Apellidos", "Identificación", "Edad", "Programa", "Nota 1", "Nota 2", "Nota 3", "Nota 4"] # Etiquetas de los campos
            entries = [] # Lista para almacenar los campos de entrada

            for i, label in enumerate(labels):
                tk.Label(editar_ventana, text=label).grid(row=i, column=0, padx=10, pady=5) # Crear y colocar etiquetas
                entry = tk.Entry(editar_ventana) # Crear campo de entrada
                entry.grid(row=i, column=1, padx=10, pady=5) # Colocar campo de entrada
                entry.insert(0, datos[i]) # Insertar el valor actual en el campo de entrada
                entries.append(entry) # Añadir el campo de entrada a la lista

            def guardar_cambios():
                nuevos_datos = [entry.get().strip() for entry in entries] # Obtener y limpiar los nuevos datos
                try:
                    if not all(nuevos_datos):
                        messagebox.showerror("Error", "Todos los campos deben estar llenos.") # Mostrar error si hay campos vacíos
                        return

                    nota1, nota2, nota3, nota4 = map(float, nuevos_datos[5:9]) # Convertir las notas a float
                    promedio = (nota1 + nota2 + nota3 + nota4) / 4 # Calcular el promedio
                    identificacion = datos[2] # Obtener la identificación del estudiante

                    conexion = crear_conexion() # Crear conexión a la base de datos
                    if conexion is not None:
                        cursor = conexion.cursor() # Crear un cursor para ejecutar consultas
                        cursor.execute("""
                            UPDATE estudiantes 
                            SET nombres=?, apellidos=?, identificacion=?, edad=?, programa=?, 
                                nota1=?, nota2=?, nota3=?, nota4=?, promedio=? 
                            WHERE identificacion=?
                        """, (
                            nuevos_datos[0], nuevos_datos[1], nuevos_datos[2], int(nuevos_datos[3]), nuevos_datos[4],
                            nota1, nota2, nota3, nota4, promedio, identificacion
                        ))# Ejecutar consulta para actualizar los datos del estudiante
                        conexion.commit() # Confirmar los cambios en la base de datos
                        conexion.close() # Cerrar la conexión a la base de datos
                        self.cargar_datos() # Recargar los datos en la tabla
                        messagebox.showinfo("Éxito", "Registro actualizado exitosamente.") # Mostrar mensaje de éxito
                        editar_ventana.destroy() # Cerrar la ventana de edición
                    else:
                        messagebox.showerror("Error", "No se pudo conectar a la base de datos.") # Mostrar error si no se puede conectar
                except ValueError:
                    messagebox.showerror("Error", "La edad y las notas deben ser números válidos.") # Mostrar error si hay valores no válidos
                except Exception as e:
                    messagebox.showerror("Error", f"Error al guardar cambios: {e}") # Mostrar error si ocurre un problema
 
            btn_guardar = tk.Button(
                editar_ventana,
                text="Guardar",
                command=guardar_cambios,
                bg="#17926e",
                fg="white",
                font=("Comic Sans MS", 12),
                width=15
            )# Botón para guardar los cambios
            btn_guardar.grid(row=len(labels), column=0, columnspan=2, pady=10) # Colocar el botón en la ventana

        except Exception as e:
            messagebox.showerror("Error", f"Error al editar estudiante: {e}") # Mostrar error si ocurre un problema

    def eliminar_estudiante(self):
        """Elimina el estudiante seleccionado después de confirmar la acción."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione un registro para eliminar.")
            return

        try:
            respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este registro?")
            if respuesta:
                item = self.tree.item(selected_item)
                identificacion = item['values'][2]

                conexion = crear_conexion()
                if conexion is not None:
                    cursor = conexion.cursor()
                    cursor.execute("DELETE FROM estudiantes WHERE identificacion=?", (identificacion,))
                    conexion.commit()
                    conexion.close()
                    self.cargar_datos()
                    messagebox.showinfo("Éxito", "Registro eliminado exitosamente.")
                else:
                    messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el registro: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()