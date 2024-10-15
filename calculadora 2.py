import tkinter as tk
from tkinter import ttk
class CurrencyConverterApp:
    def __init__(self, root):
      
        self.root = root
        self.root.title("Conversor de Dólares a Quetzales")
        self.create_widgets()
        self.conversion_rate = 7.75  

    def create_widgets(self):
     
        ttk.Label(self.root, text="De (USD):").grid(column=0, row=0, padx=10, pady=10)
        ttk.Label(self.root, text="A (GTQ):").grid(column=0, row=1, padx=10, pady=10)

        self.entry_usd = ttk.Entry(self.root)
        self.entry_usd.grid(column=1, row=0, padx=10, pady=10)
        self.entry_gtq = ttk.Entry(self.root, state='readonly')
        self.entry_gtq.grid(column=1, row=1, padx=10, pady=10)
        ttk.Button(self.root, text="Convertir", command=self.convert).grid(column=0, row=2, columnspan=2, padx=10, pady=10)
    def convert(self):
        try:
            usd_amount = float(self.entry_usd.get())  
            gtq_amount = usd_amount * self.conversion_rate  
            self.update_result(gtq_amount)
        except ValueError:
            self.update_result("Entrada no sirve")
    def update_result(self, result):
        self.entry_gtq.config(state='normal')
        self.entry_gtq.delete(0, tk.END)  
        self.entry_gtq.insert(0, f"{result:.2f}" if isinstance(result, float) else result)
        self.entry_gtq.config(state='readonly')
def main():
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
