from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import math
import numpy as np

""" Implementações a serem consideradas """
# !!!VER POSSIBILIDADE DE MUDAR CÓDIGO PARA ORIENTAÇÃO A OBJETOS!!!

# ADICIONAR UM LABEL COM O NOME DA BARRA (exemplo: "Barra 1") AO LADO DE CADA 
# BARRA PARA UMA VISUALIZAÇÃO MELHOR NO CANVAS


""" Bugs a serem corrigidos """
# CORRIGIR ERRO ONDE A FLECHA DA FORÇA CONCENTRADA É ADICIONADA TODA VEZ QUE
# A JANELA É ABERTA NOVAMENTE. APENAS UMA FORÇA CONCENTRADA SERÁ APLICADA POR
# BARRA? VERIFICAR A POSSIBILIDADE DE ADICIONAR MAIS FORÇAS.

# CORRIGIR ERRO ONDE SLIDER DA FORÇA CONCENTRADA. O VALOR MÁXIMO DO SLIDER DA 
# FORÇA NÃO ATUALIZA SE O MÓDULO(r) DA BARRA É ALTERADO DO VALOR INICIAL.

# CORRIGIR ERRO EM QUE, SE O MÓDULO DA BARRA É ALTERADO APÓS UMA FORÇA É ADICIONADA
# NA BARRA, A FORÇA FICA APLICADA FORA DA BARRA. VER SE VALE A PENA SIMPLESMENTE EXLUIR
# A FORÇA SE ELA NÃO PERTENCE MAIS A BARRA OU IMPLEMENTAR UMA PROPORCIONALIDADE DA 
# POSIÇÃO DA FORÇA EM RELAÇÃO AO TAMANHO DA BARRA.


""" Implementações a serem feitas """
# IMPLEMENTAR FUNÇÕES EXTRAS AO EXCLUIR UMA BARRA. NO MOMENTO QUANDO UMA BARRA É EXCLUIDA
# A JANELA DA FORÇA CONCENTRADA NÃO SE FECHA E AS FLECHAS NÃO SÃO EXCLUIDAS DO CANVAS, ENTÃO
# É NECESSÁRIO IMPLEMENTAR ISSO.

# REMOVER FORÇA DISTRIBUIDA E VER POSSIBILIDADE DE AUMENTAR O NÚMERO DE FORÇAS CONCENTRADAS
# POR BARRA. CASO AUMENTAR O NÚMERO DE FORÇAS PRA MAIS DE 1, UMA LISTA DE FORÇAS PRECISA
# SER IMPLEMENTADA. 3 FORÇAS PARECE UM BOM NÚMERO.

# IMPLEMENTAR ANGULAÇÃO DA FORÇA CONCENTRADA, USAR FUNÇÃO TANGENTE E VER IMPLEMENTAÇÃO DE
# CÁLCULO DO ÂNGULO NA FUNÇÃO moduloTan() PARA FACILITAR A IMPLEMENTAÇÃO.

# IMPLEMENTAR A ADIÇÃO DE VÍNCULOS (DUPLO, SIMPLES, ENGASTE)


""" Tratamento de dados para serem enviados para o front """
# Forças (lista só de vínculos):
# componentes da força (X e Y)
# coordenadas de aplicação

# Momentos (lista só de momentos):
# index do momento
# valor (sentido já indicado no valor)

# Vínculos (lista só de vínculos):
# index do vínculo
# tipo de vinculo ("Apoio Duplo", "Apoio Simples", "Engaste") <- NOMES TEM QUE SER ASSIM
# posição do vinculo (X, Y)

# Barra (lista só de barras): 
# index da barra
# !!!começo e final da barra não é necessário!!!

def main():
    global botaoNum
    botaoNum = 0
    root = tk.Tk()
    root.title('Projeto de PEF')
    root.geometry('800x640')
    # dicionario das coordenadas das barras
    coords = {"x":0,"y":0,"x2":0,"y2":0}
    botaoCoord = {"relx":0.01, "rely":0.55}
    # lista que armazena todas as coordenadas das barras
    lines = []
    text = []
    botaoBarra = []
    forcas = []
    
    # label 1
    label1 = tk.Label(root, bg='#abaaa9')
    label1.place(relx=0, rely=0.5, relwidth=0.2, relheight=1, anchor='w')

    canvas = Canvas(root, bg="#ffffff")
    canvas.place(relx=1, rely=0.5, relwidth=0.8, relheight=1, anchor='e')

    text.append(canvas.create_text(50, 50, text="x1: ", fill="black", font='Calibri 12'))
    text.append(canvas.create_text(50, 80, text="y1: ", fill="black", font='Calibri 12'))
    text.append(canvas.create_text(130, 50, text="x2: ", fill="black", font='Calibri 12'))
    text.append(canvas.create_text(130, 80, text="y2: ", fill="black", font='Calibri 12'))

    barra = tk.Button(root, text='Adicionar barras', command=lambda: adicionaBarra(barra, coords, canvas, 
                                                                                   lines, text, botaoBarra, 
                                                                                   botaoCoord, root,
                                                                                   forcas))
    barra.place(relx=0.02, rely=0.05, relwidth=0.15, relheight=0.04, anchor='w')

    # vinculo = tk.Button(root, text='Adicionar vinculos')
    # vinculo.place(relx=0.02, rely=0.1, relwidth=0.15, relheight=0.04, anchor='w')

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
    
    
def adicionaBarra(barra, coords, canvas, lines, text, botaoBarra, botaoCoord, root, forcas):
    barra.config(relief=SUNKEN)
    canvas.bind("<ButtonPress-1>", lambda event: click(coords, canvas, lines, botaoBarra, 
                                                       botaoCoord, root, barra,
                                                       forcas, e=event))
    canvas.bind("<B1-Motion>", lambda event: drag(coords, canvas, lines, text, e=event))

    
def click(coords, canvas, lines, botaoBarra, 
          botaoCoord, root, barra, forcas, e):
    # define start point for line
    coords["x"] = e.x
    coords["y"] = e.y
    # create a line on this point and store it in the list
    for line in lines:
        if type(line) != type(None):
            coordenadas = canvas.coords(line)
            if abs(canvas.coords(line)[0] - coords["x"]) < 12 and abs(canvas.coords(line)[1] - coords["y"]) < 12:
                coords["x"] = canvas.coords(line)[0]
                coords["y"] = canvas.coords(line)[1]
    
    lines.append(canvas.create_line(coords["x"], coords["y"], coords["x"], coords["y"], fill="black", width=4))

    adicionaBarraBotao(botaoBarra, botaoCoord, root, barra, canvas, lines, forcas)
    
    
def adicionaBarraBotao(botaoBarra, botaoCoord, root, barra, canvas, lines, forcas): 
    global botaoNum
    botaoBarra.append(tk.Button(root, text="Barra {}".format(botaoNum + 1), 
                                command=lambda num=botaoNum: botaoMenu(num, root, barra, canvas, 
                                                                       lines, forcas, botaoBarra, 
                                                                       botaoCoord)))
    botaoBarra[-1].place(relx=botaoCoord["relx"], rely=botaoCoord["rely"], relwidth=0.05, relheight=0.04, anchor='w')
    botaoNum += 1
    botaoCoord["relx"] += 0.06
    
    if (botaoCoord["relx"] > 0.14):
        botaoCoord["relx"] = 0.01
        botaoCoord["rely"] += 0.06


def drag(coords, canvas, lines, text, e):
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
    
    for line in lines:
        if type(line) != type(None):
            coordenadas = canvas.coords(line)
            if abs(canvas.coords(line)[0] - coords["x"]) < 12 and abs(canvas.coords(line)[1] - coords["y"]) < 12:
                coords["x"] = canvas.coords(line)[0]
                coords["y"] = canvas.coords(line)[1]

            if abs(canvas.coords(line)[2] - coords["x2"]) < 12 and abs(canvas.coords(line)[3] - coords["y2"]) < 12:
                coords["x2"] = canvas.coords(line)[2]
                coords["y2"] = canvas.coords(line)[3]
    
    canvas.itemconfigure(text[0], text="x1: {}".format(coords["x"]))
    canvas.itemconfigure(text[1], text="y1: {}".format(coords["y"]))
    canvas.itemconfigure(text[2], text="x2: {}".format(coords["x2"]))
    canvas.itemconfigure(text[3], text="y2: {}".format(coords["y2"]))
    
    canvas.coords(lines[-1], coords["x"], coords["y"], coords["x2"], coords["y2"])   
   
    
def botaoMenu(num, root, barra, canvas, lines, forcas, botaoBarra, botaoCoord):
    barra.config(relief=RAISED)
    canvas.unbind("<ButtonPress-1>")
    canvas.unbind("<B1-Motion>")
    
    janela = Toplevel(root)
    janela.title("Barra {}".format(num + 1))
    janela.geometry('480x360')
    janela.minsize(390, 280)
    janela.maxsize(390, 280)
    
    # x label
    xVar = tk.StringVar()
    xLabel = tk.Label(janela, text='Coordenada x1')
    xLabel.grid(row=0, column=0, padx=5)
    
    # x entry
    xEntry = tk.Entry(janela, textvariable=xVar, borderwidth=5, width=10, relief=tk.FLAT)
    xEntry.insert(0, canvas.coords(lines[num])[0])
    xEntry.grid(row=1, column=0, padx=5, pady=5)
    
    # y label
    yVar = tk.StringVar()
    yLabel = tk.Label(janela, text='Coordenada y1')
    yLabel.grid(row=0, column=1, padx=5)
    
    #y entry
    yEntry = tk.Entry(janela, textvariable=yVar, borderwidth=5, width=10, relief=tk.FLAT)
    yEntry.insert(0, canvas.coords(lines[num])[1])
    yEntry.grid(row=1, column=1, padx=5, pady=5)
    
    # x2 label
    x2Var = tk.StringVar()
    x2Label = tk.Label(janela, text='Coordenada x2')
    x2Label.grid(row=2, column=0, padx=5)
    
    # x2 entry
    x2Entry = tk.Entry(janela, textvariable=x2Var, borderwidth=5, width=10, relief=tk.FLAT)
    x2Entry.insert(0, canvas.coords(lines[num])[2])
    x2Entry.grid(row=3, column=0, padx=5, pady=5)
    
    # y2 label
    y2Var = tk.StringVar()
    y2Label = tk.Label(janela, text='Coordenada y2')
    y2Label.grid(row=2, column=1, padx=5)

    # y2 entry
    y2Entry = tk.Entry(janela, textvariable=y2Var, borderwidth=5, width=10, relief=tk.FLAT)
    y2Entry.insert(0, canvas.coords(lines[num])[3])
    y2Entry.grid(row=3, column=1, padx=5, pady=5)
    
    mt = moduloTan(num, canvas, lines)
    modulo = mt[0]
    tan = mt[1]
    
    # r label
    rVar = tk.StringVar()
    rLabel = tk.Label(janela, text='r')
    rLabel.grid(row=0, column=2, padx=5)
    
    # r entry
    rEntry = tk.Entry(janela, textvariable=rVar, borderwidth=5, width=10, relief=tk.FLAT)
    rEntry.insert(0, "{:.2f}".format(modulo))
    rEntry.grid(row=1, column=2, padx=5, pady=5)

    # theta label
    thetaVar = tk.StringVar()
    thetaLabel = tk.Label(janela, text='θ')
    thetaLabel.grid(row=2, column=2, padx=5)

    # theta entry
    thetaEntry = tk.Entry(janela, textvariable=thetaVar, borderwidth=5, width=10, relief=tk.FLAT)
    thetaEntry.insert(0, "{:.2f}".format(tan))
    thetaEntry.grid(row=3, column=2, padx=5, pady=5)
    
    # aplicar coordenadas button
    aplicarCoord = tk.Button(janela, text="Mudar coordenadas", 
                             command=lambda: mudarCoords(num, xVar, yVar, x2Var, 
                                                         y2Var, rVar, thetaVar, canvas, 
                                                         lines, rEntry, thetaEntry))
    aplicarCoord.grid(row=4, column=0, padx=5, pady=5, sticky=tk.N, columnspan=2)
    
    # aplicar polares button
    aplicarPol = tk.Button(janela, text="Mudar Polares", 
                           command=lambda: mudarPol(num, xVar, yVar, x2Var, 
                                                    y2Var, rVar, thetaVar, canvas, 
                                                    lines, xEntry, yEntry, x2Entry, 
                                                    y2Entry))
    aplicarPol.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)
    
    spacer1 = tk.Label(janela, text=" ",)
    spacer1.grid(row=5, column=0)
    
    # adicionar forca button
    adicionarForca1 = tk.Button(janela, text="Força concentrada 1", 
                                command=lambda: addForca(num, mt[0], mt[1], canvas, root, lines, forcas))
    adicionarForca1.grid(row=6, column=0, padx=5, pady=5, sticky=tk.N)
    
    adicionarForca2 = tk.Button(janela, text="Força concentrada 2", 
                                command=lambda: addForca(num, mt[0], mt[1], canvas, root, lines, forcas))
    adicionarForca2.grid(row=6, column=1, padx=5, pady=5, sticky=tk.N)
    
    adicionarForca3 = tk.Button(janela, text="Força concentrada 3", 
                                command=lambda: addForca(num, mt[0], mt[1], canvas, root, lines, forcas))
    adicionarForca3.grid(row=6, column=2, padx=5, pady=5, sticky=tk.N)
    
    spacer2 = tk.Label(janela, text="")
    spacer2.grid(row=7, column=0, columnspan=3)
    
    # excluir button
    excluir = tk.Button(janela, text="Excluir Barra", 
                        command=lambda: excluirBarra(num, janela, canvas, 
                                                     botaoBarra, 
                                                     botaoCoord, lines))
    excluir.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W) 
    
    
def moduloTan (num, canvas, lines):
    a = canvas.coords(lines[num])[2] - canvas.coords(lines[num])[0]
    b = canvas.coords(lines[num])[1] - canvas.coords(lines[num])[3]
    modulo = math.hypot(a, b)

    if a == 0:
        tan = 90
    else:
        tan = abs(np.rad2deg(math.atan(b/a)))
        
    if b > 0 and a < 0:
        tan += 90
    elif b < 0 and a < 0:
        tan += 180
    elif b < 0 and a > 0:
        tan = 360 - tan
    
    return (modulo, tan)


def addForca(num, mod, theta, canvas, root, lines, forcas):
    janela = Toplevel(root)
    janela.title("Forca aplicada da barra {}".format(num + 1))
    janela.geometry('480x360')
    janela.minsize(220, 160)
    janela.maxsize(220, 160)
    
    x = canvas.coords(lines[num])[0]
    y = canvas.coords(lines[num])[1]
    forcas.insert(num, canvas.create_line(x, y-100, x, y, arrow=tk.LAST, width=2))
    
    # forca label
    forcaVar = tk.StringVar()
    forcaLabel = tk.Label(janela, text='Magnitude da forca aplicada:')
    forcaLabel.grid(row=0, column=0, padx=5, sticky=tk.W)
    
    # forca entry
    forcaEntry = tk.Entry(janela, textvariable=forcaVar, borderwidth=5, relief=tk.FLAT)
    forcaEntry.grid(row=1, column=0, padx=5, pady=5)
    
    # slider label
    sliderLabel = tk.Label(janela, text='Posição:')
    sliderLabel.grid(row=2, column=0, padx=2, sticky=tk.W)
    
    # slider
    sliderVar = tk.DoubleVar()
    slider = tk.Scale(janela, from_=0, to=mod, variable=sliderVar, orient='horizontal')
    slider.grid(row=3, column=0, ipadx=50)
    
    # aplicar forca button
    aplicar = tk.Button(janela, text="Aplicar Força", 
                        command=lambda: aplicarForca(num, theta, forcaVar, sliderVar, 
                                                     canvas, forcas, lines))
    aplicar.grid(row=4, column=0, padx=5, columnspan=2, pady=5, sticky=tk.W)
    
    
def aplicarForca(num, theta, forca, sliderVar, canvas, forcas, lines):
    slider = sliderVar.get()
    try:
        forca = float(forca.get())
    except:
        forca = 100

    newX = slider*(math.cos(np.deg2rad(theta)))
    newY = slider*(math.sin(np.deg2rad(theta)))

    newX = canvas.coords(lines[num])[0] + newX
    newY = canvas.coords(lines[num])[1] - newY

    canvas.coords(forcas[num], newX, newY-forca, newX, newY)
    
    
def mudarCoords(num, x, y, x2, y2, r, theta, canvas, lines, rEntry, thetaEntry):
    x = float(x.get()) 
    y = float(y.get())
    x2 = float(x2.get())
    y2 = float(y2.get())
    r = float(r.get())
    theta = float(theta.get())
    
    canvas.coords(lines[num], x, y, x2, y2)
    mt = moduloTan(num)
    updateModuloTan(mt[0], mt[1], rEntry, thetaEntry)


def mudarPol(num, x, y, x2, y2, r, theta, canvas, lines, xEntry, yEntry, x2Entry, y2Entry):
    x = float(x.get()) 
    y = float(y.get())
    x2 = float(x2.get())
    y2 = float(y2.get())
    r = float(r.get())
    theta = float(theta.get())
    
    theta = 360 - theta
    newX = r*(math.cos(np.deg2rad(theta)))
    newY = r*(math.sin(np.deg2rad(theta)))
    
    x2 = x + newX
    y2 = y + newY
    theta = 360 - theta
    canvas.coords(lines[num], x, y, x2, y2)
    updateCoords(x, y, x2, y2, xEntry, yEntry, x2Entry, y2Entry)


def updateModuloTan(modulo, tan, rEntry, thetaEntry):
    rEntry.delete(0, END)
    rEntry.insert(0, "{:.2f}".format(modulo))
    
    thetaEntry.delete(0, END)
    thetaEntry.insert(0, "{:.2f}".format(tan))
    
    
def updateCoords(x, y, x2, y2, xEntry, yEntry, x2Entry, y2Entry):
    xEntry.delete(0, END)
    xEntry.insert(0, "{:.2f}".format(x))
    
    yEntry.delete(0, END)
    yEntry.insert(0, "{:.2f}".format(y))
    
    x2Entry.delete(0, END)
    x2Entry.insert(0, "{:.2f}".format(x2))
    
    y2Entry.delete(0, END)
    y2Entry.insert(0, "{:.2f}".format(y2))
    

def excluirBarra(num, janela, canvas, botaoBarra, botaoCoord, lines):
    global botaoNum
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
    

main()