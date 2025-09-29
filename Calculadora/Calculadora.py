#Calculadora
import re

def logica(resultado, partes):
    i = 0
    while i < len(partes):
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
    
    resultado = float(partes[0])
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

def calcular(resultado, calculo):
    partes = re.findall(r'[+\-*/]?\d+', calculo)
    if not partes[0].startswith(("+", "-", "*", "/")):
        resultado = float(partes[0])
        return logica(resultado, partes)
    elif partes[0].startswith(("+", "-", "*", "/")):
        partes.insert(0, str(resultado))
        return logica(resultado, partes)

resultado = 0
res_ant = 0

while True:
    print(f"Resultado anterior: {res_ant}")
    print(resultado)

    print("Insira sua operação [Sinal][Numero]")
    calculo = input()
    
    res_ant = resultado
    resultado = calcular(resultado, calculo)
    
    
    
    