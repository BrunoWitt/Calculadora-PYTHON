#Calculadora
import re

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


#Definição inicial do resultado
resultado = 0
res_ant = 0

#"Tutorial"
print("Calculadora Iniciada.\n'sair' para encerrar. 'zerar' para zerar o resultado.\nAdicione sinal da frente da operação para somar ao resultado\nNumero solto substitui o resultado")

while True:
    print(f"Resultado anterior: {res_ant}")
    print(resultado)

    print("Insira sua operação. (ou 'sair' para encerrar): ") #Operação pode ser feita de forma livre. Ex: 5+5*2-10/2, 10/2*3+5-2, 5*5*5*5*5, etc.
    calculo = input()
    
    if calculo.lower() == 'sair':
        break
    if calculo.lower() == 'zerar':
        resultado = 0
        continue
    
    res_ant = resultado
    resultado = calcular(resultado, calculo) #Funções de cálculo
    
    
    
    