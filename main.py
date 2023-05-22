from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk

global botaoNum, botaoCoord

def pegaTamanho(tamanho):
    tamanho = float(tamanho.get())
    print(tamanho)


def pegaForca(forca):
    forca = float(forca.get())
    print(forca)
    

def mudarCoords(num, x, y, x2, y2):
    x = 20*int(x.get()) 
    y = 20*int(y.get())
    x2 = 20*int(x2.get())
    y2 = 20*int(y2.get())
    canvas.coords(lines[num], x, y, x2, y2)
    
    
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
    difX = abs(coords["x"] - coords["x2"])
    difY = abs(coords["y"] - coords["y2"])
    if difY < 20:
        coords["y2"] = coords["y"]
    if difX < 20:
        coords["x2"] = coords["x"]
    
    canvas.itemconfigure(text1, text="x1: {}".format(coords["x"]/20))
    canvas.itemconfigure(text2, text="y1: {}".format(coords["y"]/20))
    canvas.itemconfigure(text3, text="x2: {}".format(coords["x2"]/20))
    canvas.itemconfigure(text4, text="y2: {}".format(coords["y2"]/20))
    
    canvas.coords(lines[-1], coords["x"], coords["y"], coords["x2"], coords["y2"])


def excluirBarra(num, janela):
    print(num)
    global botaoNum  
    global botaoCoord
    canvas.delete(lines[num])
    lines[num] = None
    botaoBarra[num].destroy()
    botaoBarra[num] = None
    janela.destroy()

    botaoCoord = {"relx":0.01, "rely":0.55}

    for i in range(botaoNum):
        if type(botaoBarra[i]) != type(None):
            botaoBarra[i].config(text="Botao {}".format(i + 1))
            botaoBarra[i].place(relx=botaoCoord["relx"], rely=botaoCoord["rely"], relwidth=0.05, relheight=0.04, anchor='w')        
            botaoCoord["relx"] += 0.06 
            if (botaoCoord["relx"] > 0.14):
                botaoCoord["relx"] = 0.01
                botaoCoord["rely"] += 0.06
            
    
def botaoMenu(num):
    janela = Toplevel(root)
    janela.title("Barra {}".format(num + 1))
    janela.geometry('360x200')
    janela.minsize(360, 200)
    janela.maxsize(360, 200)
    
    xVar = tk.StringVar()
    # x label
    xLabel = tk.Label(janela, text='Coordenada x1')
    
    xLabel.grid(row=0, column=0, padx=5)
    
    # x entry
    xEntry = tk.Entry(janela, textvariable=xVar, borderwidth=5, width=10, relief=tk.FLAT)
    xEntry.insert(0, coords["x"]/20)
    xEntry.grid(row=1, column=0, padx=5, pady=5)
    
    yVar = tk.StringVar()
    # y label
    yLabel = tk.Label(janela, text='Coordenada y1')
    yLabel.grid(row=0, column=1, padx=5)
    
    #y entry
    yEntry = tk.Entry(janela, textvariable=yVar, borderwidth=5, width=10, relief=tk.FLAT)
    yEntry.insert(0, coords["y"]/20)
    yEntry.grid(row=1, column=1, padx=5, pady=5)
    
    x2Var = tk.StringVar()
    # x2 label
    x2Label = tk.Label(janela, text='Coordenada x2')
    x2Label.grid(row=2, column=0, padx=5)
    
    # x2 entry
    x2Entry = tk.Entry(janela, textvariable=x2Var, borderwidth=5, width=10, relief=tk.FLAT)
    x2Entry.insert(0, coords["x2"]/20)
    x2Entry.grid(row=3, column=0, padx=5, pady=5)
    
    y2Var = tk.StringVar()
    # y2 label
    y2Label = tk.Label(janela, text='Coordenada y2')
    y2Label.grid(row=2, column=1, padx=5)

    # y2 entry
    y2Entry = tk.Entry(janela, textvariable=y2Var, borderwidth=5, width=10, relief=tk.FLAT)
    y2Entry.insert(0, coords["y2"]/20)
    y2Entry.grid(row=3, column=1, padx=5, pady=5)
    
    # aplicar button
    aplicar = tk.Button(janela, text="Aplicar", command=lambda: mudarCoords(num, xVar, yVar, x2Var, y2Var))
    aplicar.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    
    # excluir button
    aplicar = tk.Button(janela, text="Excluir Barra", command=lambda: excluirBarra(num, janela))
    aplicar.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

    

def adicionaBarraBotao():
    global botaoNum
    global botaoCoord
    botaoBarra.append(tk.Button(root, text="Barra {}".format(botaoNum + 1), command=lambda num=botaoNum: botaoMenu(num)))
    botaoBarra[-1].place(relx=botaoCoord["relx"], rely=botaoCoord["rely"], relwidth=0.05, relheight=0.04, anchor='w')
    botaoNum += 1
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

text1 = canvas.create_text(50, 50, text="x1: ", fill="black", font='Calibri 12')
text2 = canvas.create_text(50, 80, text="y1: ", fill="black", font='Calibri 12')
text3 = canvas.create_text(110, 50, text="x2: ", fill="black", font='Calibri 12')
text4 = canvas.create_text(110, 80, text="y2: ", fill="black", font='Calibri 12')

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



