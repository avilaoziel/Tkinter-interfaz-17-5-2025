import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def Interfaz_inicio():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Bienvenido a la Interfaz", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar mensaje de bienvenida", command=lambda: messagebox.showinfo("Saludo", "Mucho gusto !!!")).pack()

def lista_despegable():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Ingrese opciones", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Oziel Avila Guerra:").pack()
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="Selección A:").pack()
    opcion_elegida = tk.StringVar(value="Grupo A")
    tk.Radiobutton(area_dinamica, text="Grupo A", variable=opcion_elegida, value="Grupo A").pack()
    tk.Radiobutton(area_dinamica, text="Grupo B", variable=opcion_elegida, value="Grupo B").pack()

    tk.Label(area_dinamica, text="Lista desplegable:").pack()
    combo = ttk.Combobox(area_dinamica, values=["Uno", "Dos", "Tres"])
    combo.pack()
    combo.current(0)

    def accion_guardar():
        valor = campo_texto_uno.get()
        messagebox.showinfo("Revisión", f"Texto: {valor}\nSelección: {opcion_elegida.get()}\nLista: {combo.get()}")

    tk.Button(area_dinamica, text="Botón 2", command=accion_guardar).pack(pady=10)

def cambio_color():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Configuraciones temporales", font=("Arial", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "lightyellow", "black"]
    tk.Label(area_dinamica, text="Cambiar fondo:").pack()

    def cambiar_color(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: cambiar_color(col)).pack(pady=2)

def centro_ayuda():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Texto de ayuda que el alumno debe mejorar", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

def area_dinamica_limpia():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Interfaz para prácticas")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Inicio", command=Interfaz_inicio, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Listas, Alummno", command=lista_despegable, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ajuste de Intefaz", command=cambio_color, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ayuda", command=centro_ayuda, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

Interfaz_inicio()
ventana_principal.mainloop()
