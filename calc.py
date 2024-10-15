import tkinter as tk

def convertir():
    try:
        millas = float(entry_millas.get())
        km = millas * 1.60934 
        label_resultado.config(text=f"{millas} millas son {km:.2f} kilómetros.")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa un número válido.")
ventana = tk.Tk()
ventana.title("Conversor de Millas a Km")
ventana.geometry("500x300")
label_millas = tk.Label(ventana, text="Introduce millas:")
label_millas.pack()

entry_millas = tk.Entry(ventana)
entry_millas.pack()

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()
ventana.mainloop()
