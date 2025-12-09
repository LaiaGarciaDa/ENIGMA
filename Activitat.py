from random import randint, random

ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numrand = randint(0,25)        
print(ABC[numrand])

#from cProfile import label
import tkinter as tk
contador = 0
usuario = "Default"

def mostrar_texto_por_pantalla():
    global contador 
    usuario = entrada_texto.get()
    label.config(text=f"bienvenido {usuario}") 
    print(f"click {contador}")  
    


    
root = tk.Tk()
root.title("Mi primera ventana")
root.geometry("500x500")

entrada_texto = tk.Entry(root)
entrada_texto.pack()

label = tk.Label(root, text = f"HOLA {usuario}")
label.pack()

bttn = tk.Button(root, text = "Enter", command = mostrar_texto_por_pantalla)
bttn.pack()


root.mainloop()