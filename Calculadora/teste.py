import re

#Precisa entrar um calculo
#Se a parte[0] do calculo não tiver nenhum sinal, ela substitui o resultado
#Se a parte[0] do calculo tiver um sinal, ela faz a operação com o resultado
def logica(resultado, partes):
    i = 0
    while i < len(partes[1:]):
        parte = partes[i]
        
        if parte.startswith("*") or parte.startswith("/"):
            n_esq = int(partes[i-1])
            n_dir = int(parte[1:])
            
            if parte.startswith("*"):
                novo = n_esq * n_dir
            if parte.startswith("/"):
                novo = n_esq / n_dir
            partes[i-1] = str(novo)
            partes.pop(i)
        else:
            i += 1
    for parte in partes[1:]:
        if parte.startswith("+"):
            resultado = resultado + float(parte)
        elif parte.startswith("-"):
            resultado = resultado - float(parte)
        elif parte.startswith("*"):
            resultado = resultado * float(parte)
        elif parte.startswith("/"):
            nparte = int(parte[1:])
            resultado = resultado / nparte
        else:
            resultado += float(parte)
            
    return(resultado)

def calcular(resultado, calculo):
    partes = re.findall(r'[+\-*/]?\s*\d*d?\d+', calculo)
    if not partes[0].startswith(("+", "-", "*", "/")):
        resultado = float(partes[0])
        resultado = logica(resultado, partes)
        return(resultado)
    elif partes[0].startswith(("+", "-", "*", "/")):
        partes.insert(0, str(resultado))
        resultado = 0
        resultado = logica(resultado, partes)
        return(resultado)

                
calculo = "20+4*3/1"
resultado = 10

resultado = calcular(resultado, calculo)

print(resultado)