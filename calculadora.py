import tkinter as tk

# Función para añadir texto al display
def agregar_texto(valor):
    entrada_var.set(entrada_var.get() + str(valor))

# Función para limpiar el display
def limpiar():
    entrada_var.set("")

# Función para calcular la operación
def calcular():
    try:
        resultado = eval(entrada_var.get())
        entrada_var.set(str(resultado))
    except:
        entrada_var.set("Error")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

# Variable del display
entrada_var = tk.StringVar()

# Entry para mostrar los números y resultados
entrada = tk.Entry(ventana, textvariable=entrada_var, font=("Arial", 20), bd=5, relief="ridge", justify="right")
entrada.pack(fill="both", ipadx=8, pady=10, padx=10)

# Frame para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack()

# Lista de botones
botones = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Crear botones en la interfaz
for i, fila in enumerate(botones):
    for j, boton in enumerate(fila):
        if boton == "=":
            b = tk.Button(frame_botones, text=boton, width=5, height=2, font=("Arial", 20), command=calcular)
        else:
            b = tk.Button(frame_botones, text=boton, width=5, height=2, font=("Arial", 20),
                          command=lambda x=boton: agregar_texto(x))
        b.grid(row=i, column=j, padx=5, pady=5)

# Botón de limpiar
boton_clear = tk.Button(ventana, text="C", width=5, height=2, font=("Arial", 20), command=limpiar, bg="red", fg="white")
boton_clear.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
