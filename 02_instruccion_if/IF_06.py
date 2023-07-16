import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Martín
apellido: Morales
---
Ejercicio: instrucion_if_06
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener contenido en la caja de texto txtEdad, transformarlo en número 
y calcular si es mayor, niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años) o adolescente (edad entre 13 y 17 años) de edad, 
se deberá informar utilizando el Dialog alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # texto_edad = self.txt_edad.get()
        # numero_edad = int(texto_edad)

        # if numero_edad < 10 :
        #     alert(title="Edad", message="NIÑO")
        # else:
        #     if(numero_edad >= 10 or numero_edad <= 12):
        #         alert(title="Edad", message="PRE-ADOLESCENTE")
        #     else:
        #         if(numero_edad >=13 or numero_edad <= 17):
        #             alert(title="Edad", message="ADOLESCENTE")
        #         else:
        #             alert(title="Edad", message="ADULTO")
        


        # if numero_edad < 10:
        #     print("NIÑO.")
        # elif numero_edad >= 10 or numero_edad <= 12:
        #     print("PRE-ADOLESCENTE")
        # elif numero_edad >= 13 or numero_edad <= 17:
        #     print("ADOLESCENTE")
        # else:
        #     print("Sos un adulto.")
        
        texto_edad=self.txt_edad.get()
        numero_edad=int(texto_edad)

        if(numero_edad<10):
            alert(title="Edad", message="NIÑO/A")
        elif(numero_edad >=10 and numero_edad<=12):
            alert(title="Edad", message="PRE-ADOLESCENTE")
        elif(numero_edad >=13 and numero_edad<=17):
            alert(title="Edad", message="ADOLESCENTE")
        else:
            alert(title="Edad", message="ADULTO.")

        
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()