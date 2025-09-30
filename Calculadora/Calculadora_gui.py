import tkinter as tk
from tkinter import ttk
import re

#Funções de cálculo
def logica(resultado, partes):
    i = 0
    while i < len(partes): #Realiza os cálculos de multiplicação e divisão primeiro
        parte = partes[i]
        
        if parte.startswith("*") or parte.startswith("/"):
            n_esq = float(partes[i-1])
            n_dir = float(parte[1:])
            
            if parte.startswith("*"):
                novo = n_esq * n_dir
            else:  
                novo = n_esq / n_dir
            partes[i-1] = str(novo)
            partes.pop(i)
        else:
            i += 1
    
    resultado = float(partes[0]) #Realiza os cálculos de soma e subtração
    for parte in partes[1:]:
        if parte.startswith("+"):
            resultado += float(parte[1:])
        elif parte.startswith("-"):
            resultado -= float(parte[1:])
        elif parte.startswith("*") or parte.startswith("/"):
            continue
        else:
            resultado += float(parte)
            
    return(resultado)

def calcular(resultado, calculo): #Função que verifica se o valor será substituído ou somado ao resultado
    partes = re.findall(r'[+\-*/]?\d+', calculo) #Separar partes por sinais
    
    if not partes[0].startswith(("+", "-", "*", "/")):
        resultado = float(partes[0])
        return logica(resultado, partes) #Chama a função logica para continuar o cálculo
    
    elif partes[0].startswith(("+", "-", "*", "/")):
        partes.insert(0, str(resultado))
        return logica(resultado, partes)

#Funções da interface gráfica
def exe_calcular(): #Responsável por executar o cálculo ao clicar no botão
    global resultado
    entrada = ent_entrada.get()
    result = lbl_resultado.cget("text")
    resultado = calcular(resultado, entrada)
    lbl_resultado.config(text=str(resultado))

def exe_zerar():
    global resultado
    resultado = 0
    lbl_resultado.config(text=str(resultado))
    ent_entrada.delete(0, tk.END) 
    
def exe_deletar():
    texto_atual = ent_entrada.get()
    ent_entrada.delete(0, tk.END)
    ent_entrada.insert(0, texto_atual[:-1]) 

    
def inserir_valor(valor): #Insere o valor clicado na entrada
    ent_entrada.insert(tk.END, valor)

#Interface gráfica
resultado = 0

app = tk.Tk()
app.title("Calculadora")
app.resizable(False, False) 

lbl_resultado = tk.Label(app, text=str(resultado), font=("Arial", 24), bg="#e0e0e0", width=14, anchor='e')
lbl_resultado.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

ent_entrada = tk.Entry(app, font=("Arial", 20), justify='right')
ent_entrada.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

# Layout dos botões
botoes = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
    ('C', 6, 0)
]

for (texto, linha, coluna) in botoes:
    if texto == '=':
        tk.Button(app, text=texto, width=5, height=2, font=("Arial", 18), bg="#90ee90", command=exe_calcular).grid(row=linha, column=coluna, padx=5, pady=5)
    elif texto == 'C':
        tk.Button(app, text='C', width=5, height=2, font=("Arial", 18), bg="#f08080", command=exe_zerar).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(app, text='DEL', width=5, height=2, font=("Arial", 18), bg="#ffa500", command=exe_deletar).grid(row=6, column=1, padx=5, pady=5)
    else:
        tk.Button(app, text=texto, width=5, height=2, font=("Arial", 18), command=lambda t=texto: inserir_valor(t)).grid(row=linha, column=coluna, padx=5, pady=5)

app.mainloop()