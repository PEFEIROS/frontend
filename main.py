from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk

global botaoNum

# class Barra:
    #def __init__(self, x, y, x2, y2):
        #self.x = x
        #self.x2 = x2
        #self.y = y
        #self.y2 = y2
        # adicionar vinculos
    #def getStart(self):
        #return (self.x, self.y)
    #def getEnd(self):
        #return (self.x2, self.y2)
    #def setStart(self, x, y):
        #self.x = x
        #self.y = y
    #def setEnd(self, x2, y2):
        #self.x2 = x2
        #self.y2 = y2

# class BotaoDaBarra:
   # def __init__(self, barra) -> None:
       # self.barra = barra

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
    
    
def botaoMenu(num):
    janela = Toplevel(root)
    janela.title("Botao {}".format(num))
    janela.geometry('360x200')
    janela.minsize(360, 200)
    janela.maxsize(360, 200)
    
    xVar = tk.StringVar()
    # x label
    xLabel = tk.Label(janela, text='Coordenada x1')
    xLabel.grid(row=0, column=0, sticky=tk.N)
    
    # x entry
    xEntry = tk.Entry(janela, textvariable=x, borderwidth=2, relief=tk.FLAT)
    xEntry.grid(row=1, column=0, padx=5, pady=5)
    
    yVar = tk.StringVar()
    # y label
    yLabel = tk.Label(janela, text='Coordenada y1')
    yLabel.grid(row=0, column=1, sticky=tk.N)
    
    #y entry
    yEntry = tk.Entry(janela, textvariable=y, borderwidth=5, width=20, relief=tk.FLAT)
    yEntry.place(row=1, column=1, sticky=tk.N, padx=5, pady=5)
    
    x1Var = tk.StringVar()
    # x1 label
    x1Label = tk.Label(janela, text='Coordenada y1')
    x1Label.grid(row=0, column=1, sticky=tk.N)
    
    # x1 entry
    x1Entry = tk.Entry(janela, textvariable=y, borderwidth=5, width=20, relief=tk.FLAT)
    x1Entry.place(row=1, column=1, sticky=tk.N, padx=5, pady=5)
    
    # aplicar button
    aplicar = tk.Button(janela, text="Aplicar", command=lambda: pegaForca(forcaVar))
    aplicar.grid(row=3, column=3, padx=5, pady=5)
    


def adicionaBarraBotao():
    global botaoNum
    botaoNum += 1
    botaoBarra.append(tk.Button(root, text="Barra {}".format(botaoNum), command=lambda num=botaoNum: botaoMenu(num)))
    botaoBarra[-1].place(relx=botaoCoord["relx"], rely=botaoCoord["rely"], relwidth=0.05, relheight=0.04, anchor='w')
    botaoCoord["relx"] += 0.06
    
    if (botaoCoord["relx"] > 0.14):
        botaoCoord["relx"] = 0.01
        botaoCoord["rely"] += 0.06
    
    


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

botaoCoord = {"relx":0.01, "rely":0.55}
botaoBarra = []
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

# FUNCOES RELATIVAS A CRIACAO DE IMAGENS NO CANVAS
imgEngaste = ImageTk.PhotoImage(Image.open("./ENGASTE.png"))
imgArticulacao = ImageTk.PhotoImage(Image.open("./ARTICULACAO.png"))
imgApoioSimples = ImageTk.PhotoImage(Image.open("./APOIOSIMPLES.png"))

def adicionarEngaste(x, y):
    canvas.create_image(x,y,anchor=N,image=imgEngaste)

def adicionarArticulacao(x, y):

    canvas.create_image(x,y,anchor=N,image=imgArticulacao)

def adicionarApoioSimples(x, y):
    canvas.create_image(x,y,anchor=N,image=imgApoioSimples)

root.mainloop()



