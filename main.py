import tkinter as tk  # Importar el módulo tkinter para la interfaz gráfica
from pygame import mixer
from ventanas.ventana_principal import VentanaPrincipal  # Importar la clase VentanaPrincipal desde ventana_principal.py

class SistemaNotas:
    def __init__(self, root):
        """Inicializa la ventana principal del sistema de notas."""
        self.root = root  # Asignar la raíz de Tkinter a self.root
        self.root.title("Sistema de Notas de Estudiantes")  # Establecer el título deSSS la ventana
        self.root.geometry("1300x500")  # Establecer el tamaño de la ventana a 900x500 píxeles
        
        inicio = "inicio.mp3"
        mixer.init()
        mixer.music.load(inicio)
        mixer.music.play() 
        # Crear instancia de la ventana principal del sistema de notas
        self.ventana_principal = VentanaPrincipal(root)

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    root = tk.Tk()  # Crear una instancia de Tkinter
    app = SistemaNotas(root)  # Crear una instancia de SistemaNotas
    root.mainloop()  # Iniciar el bucle principal de la interfaz gráfica
