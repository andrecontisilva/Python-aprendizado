"""
Aprendendo Python:
Gerador de jogadas de d10 para Vampiro - A Máscara
(Projetinho bobo apenas para brincar com o código)
"""
# Importando o random para gerar números aleatórios:
from random import random


# Função que gera 1d10 com valor aleatório:
def d10():
    valor = int(random() * 10)  # Converte os floats do random em int, de 0 a 9
    if valor == 0:  # transforma os 0 do random em 10
        valor = 10
    return valor


"""
# Testando várias jogadas para ver se dá mais do que 10 no d10
for dado in range(10):
    dado = d10()
    if dado > 10:
        dado = "Maior que 10"
    print(dado)
"""

# Dados e dificuldade:
dados = int(input("Quantidade de dados: "))  # Define quantos d10 que serão lançados
# dificuldade = int(input("Dificuldade: "))  # Define a dificuldade da jogada
"""
print(dados) # Testa o valor de dados colocado no input
print(type(dados)) # Testa se o tipo de valor gerado no input é int
"""

# Lança "x"d10 conforme definido pelo usuário:
for i in range(dados):
    jogada = d10()
    print(jogada)
