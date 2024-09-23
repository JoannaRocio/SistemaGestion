import pymysql
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

# Conectar a la base de datos
conexion = pymysql.connect(host='localhost', user='root', password='1920', database='gestion_base')

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Gestión de Autos")
        self.geometry("400x300")
        
        # Widgets de la interfaz
        self.label_nombre = tk.Label(self, text="Nombre:")
        self.label_nombre.pack(pady=5)
        
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack(pady=5)
        
        self.label_auto = tk.Label(self, text="Auto:")
        self.label_auto.pack(pady=5)
        
        self.entry_auto = tk.Entry(self)
        self.entry_auto.pack(pady=5)
        
        self.btn_seleccionar_foto = tk.Button(self, text="Seleccionar Fotos", command=self.seleccionar_fotos)
        self.btn_seleccionar_foto.pack(pady=5)
        
        self.btn_subir = tk.Button(self, text="Subir Datos", command=self.subir_datos)
        self.btn_subir.pack(pady=20)
        
        self.fotos_rutas = []  # Lista de rutas de las fotos seleccionadas

    def seleccionar_fotos(self):
        # Permitir seleccionar múltiples fotos
        fotos_rutas = filedialog.askopenfilenames(title="Seleccionar Fotos", filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
        if fotos_rutas:
            self.fotos_rutas = []
            ruta_guardar_fotos = r'C:\Users\Ezequiel Santillan\Desktop\python\imagenes'
            
            # Asegurarse de que la carpeta exista
            if not os.path.exists(ruta_guardar_fotos):
                os.makedirs(ruta_guardar_fotos)
            
            for foto_ruta in fotos_rutas:
                # Procesar cada foto (por ejemplo, cambiar el tamaño)
                foto = Image.open(foto_ruta)
                foto.thumbnail((800, 800))
                
                foto_guardada = os.path.join(ruta_guardar_fotos, os.path.basename(foto_ruta))
                foto.save(foto_guardada)
                self.fotos_rutas.append(foto_guardada)
                
            messagebox.showinfo("Fotos Seleccionadas", f"Fotos guardadas en: {ruta_guardar_fotos}")
        else:
            messagebox.showwarning("Advertencia", "No se seleccionaron fotos")

    def subir_datos(self):
        nombre = self.entry_nombre.get()
        auto = self.entry_auto.get()
        
        if not nombre or not auto or not self.fotos_rutas:
            messagebox.showwarning("Error", "Por favor, completa todos los campos y selecciona fotos.")
            return
        
        try:
            with conexion.cursor() as cursor:
                # Insertar el auto en la tabla 'autos'
                sql_insert_auto = "INSERT INTO autos (nombre, auto) VALUES (%s, %s)"
                cursor.execute(sql_insert_auto, (nombre, auto))
                auto_id = cursor.lastrowid  # Obtener el ID del auto recién insertado

                # Insertar cada imagen en la tabla 'imagenes'
                for foto_ruta in self.fotos_rutas:
                    with open(foto_ruta, 'rb') as foto_file:
                        foto_data = foto_file.read()
                    
                    sql_insert_imagen = "INSERT INTO imagenes (auto_id, foto) VALUES (%s, %s)"
                    cursor.execute(sql_insert_imagen, (auto_id, foto_data))
                
            conexion.commit()
            messagebox.showinfo("Éxito", "Datos subidos exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al subir datos: {e}")
        finally:
            conexion.close()

# Crear la ventana principal
app = VentanaPrincipal()
app.mainloop()
