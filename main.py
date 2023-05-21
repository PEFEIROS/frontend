from tkinter import *
import tkinter as tk

global botaoNum

def pegaTamanho(tamanho):
    tamanho = float(tamanho.get())
    print(tamanho)


def pegaForca(forca):
    forca = float(forca.get())
    print(forca)


def adicionaBarra():
    barra.config(relief=SUNKEN)
    canvas.bind("<ButtonPress-1>", click)
    canvas.bind("<B1-Motion>", drag)

    
def click(e):
    # define start point for line
    coords["x"] = e.x
    coords["y"] = e.y

    # create a line on this point and store it in the list
    lines.append(canvas.create_line(coords["x"], coords["y"], coords["x"], coords["y"], fill="black", width=4))
    adicionaBarraBotao()
    

def drag(e):
    # update the coordinates from the event
    coords["x2"] = e.x
    coords["y2"] = e.y

    # Change the coordinates of the last created line to the new coordinates
    canvas.coords(lines[-1], coords["x"], coords["y"], coords["x2"], coords["y2"])


def adicionaBarraBotao():
    global botaoNum
    botaoNum += 1
    barraBotao.append(tk.Button(root, text="Barra {}".format(botaoNum)))
    barraBotao[-1].place(relx=coordBotao["relx"], rely=coordBotao["rely"], relwidth=0.05, relheight=0.04, anchor='w')
    coordBotao["relx"] += 0.06
    
    if (coordBotao["relx"] > 0.14):
        coordBotao["relx"] = 0.01
        coordBotao["rely"] += 0.06


root = tk.Tk()
root.title('Projeto de PEF')
root.geometry('800x640')

# label 1
label1 = tk.Label(root, bg='#abaaa9')
label1.place(relx=0, rely=0.5, relwidth=0.2, relheight=1, anchor='w')

canvas = Canvas(root, bg="#dbfffd")
canvas.place(relx=1, rely=0.5, relwidth=0.8, relheight=1, anchor='e')

# dicionario das coordenadas das barras
coords = {"x":0,"y":0,"x2":0,"y2":0}
# lista que armazena todas as coordenadas das barras
lines = []

coordBotao = {"relx":0.01, "rely":0.55}
barraBotao = []
botaoNum = 0
barra = tk.Button(root, text='Adicionar barras', command=adicionaBarra)
barra.place(relx=0.02, rely=0.05, relwidth=0.15, relheight=0.04, anchor='w')

vinculo = tk.Button(root, text='Adicionar vinculos')
vinculo.place(relx=0.02, rely=0.1, relwidth=0.15, relheight=0.04, anchor='w')

tamanho = tk.Label(root, text='Tamanho da barra:')
tamanho.place(relx=0.02, rely=0.2, relwidth=0.1, relheight=0.04, anchor='w')

tamanhoVar = tk.StringVar()
tamanhoEntrada = tk.Entry(root, textvariable=tamanhoVar, borderwidth=5, relief=tk.FLAT)
tamanhoEntrada.place(relx=0.02, rely=0.25, relwidth=0.12, relheight=0.04, anchor='w')

tamanhoBotao = tk.Button(root, text="Aplicar", command=lambda: pegaTamanho(tamanhoVar))
tamanhoBotao.place(relx=0.15, rely=0.25, relwidth=0.045, relheight=0.04, anchor='w')

forca = tk.Label(root, text='Forca aplicada no nó ##:')
forca.place(relx=0.02, rely=0.4, relwidth=0.15, relheight=0.04, anchor='w')

forcaVar = tk.StringVar()
forcaEntrada = tk.Entry(root, textvariable=forcaVar, borderwidth=5, relief=tk.FLAT)
forcaEntrada.place(relx=0.02, rely=0.45, relwidth=0.12, relheight=0.04, anchor='w')

forcaBotao = tk.Button(root, text="Aplicar", command=lambda: pegaForca(forcaVar))
forcaBotao.place(relx=0.15, rely=0.45, relwidth=0.045, relheight=0.04, anchor='w')

root.mainloop()



