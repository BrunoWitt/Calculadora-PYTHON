"""letra_val = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}

def cesar(letra, num):
    letra_valor = letra_val[letra]
    nova_letra_valor = letra_valor + num
    letra_nova = [k for k, v in letra_val.items() if v == nova_letra_valor]
    return letra_nova   

palavra = "comida"
letras = list(palavra)

alfabeto = "abcdefghijklmnopqrstuvwxyz"
letras_alfabeto = list(alfabeto)

num = +1

for letra in letras:
    letra = cesar(letra, num)
    print(letra, end="")"""
    
"""import random

baralho = ['1♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
           '1♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
           '1♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣',
           '1♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']

def embaralhar(baralho):
    random.shuffle(baralho)
    return baralho

def mostrar(baralho):
    quant_baralho = len(baralho)
    return f"O baralho tem {quant_baralho} cartas e são elas: {baralho}"

def distribuir(baralho, num_jogadores, num_cartas):
    if num_jogadores * num_cartas > len(baralho):
        return "Não há cartas suficientes para distribuir"
    
    cartas = len(baralho)
    distribuicao = cartas/num_jogadores
    
    for i in range(num_jogadores):
        mao = []
        for j in range(num_cartas):
            carta = baralho.pop()
            mao.append(carta)
        print(f"Jogador {i+1}: {mao}")
    return f"Restaram {len(baralho)} cartas no baralho"

print("Opções: 1- Embaralhar, 2- Mostrar, 3- Distribuir")
opc = int(input("Escolha uma opção: "))

if opc == 1:
    print(embaralhar(baralho))
elif opc == 2:
    print(mostrar(baralho))
elif opc == 3:
    num_jogadores = int(input("Número de jogadores: "))
    num_cartas = int(input("Número de cartas por jogador: "))
    print(distribuir(baralho, num_jogadores, num_cartas))"""

"""carros = [
    ['Mustang', 120],
    ['Camaro', 110],
    ['Challenger', 115],
    ['Corvette', 130],
    ['Porsche', 140],
    ['Uno', 90],
    ['Celta', 85],
    ['Gol', 95],
    ['Fusca', 80],
    ['Opala', 100]
]

alugados = []


def mostrar_carros(carros):
    i = 0
    for carro in carros:
        print(f"[{i}]Carro: {carro[0]}, aluguel p/dia {carro[1]}")
        i+=1
    return

def alugar_carro(carros, escolha):
    if escolha < 0 or escolha >= len(carros):
        return "Escolha inválida"
    alugados.append(carros.pop(escolha))
    return f"Você alugou o carro {alugados[0][0]} por {alugados[0][1]} por dia"

def devolver_carro(carros, alugados, escolha):
    carros.append(alugados.pop(escolha))
    return "Carro devolvido com sucesso"

while True:

    print("Bem-vindo à locadora de carros!\Opções: 1- Mostrar carros, 2- Alugar carro 3- Devolver carro")
    opc = int(input("Escolha uma opção: "))
    match opc:
        case 1:
            mostrar_carros(carros)
        case 2:
            mostrar_carros(carros)
            escolha = int(input("Escolha o número do carro que deseja alugar: "))
            print(alugar_carro(carros, escolha))
        case 3:
            mostrar_carros(alugados)
            escolha = int(input("Escolha qual carro deseja devolver: "))
            print(devolver_carro(carros, alugados, escolha))"""