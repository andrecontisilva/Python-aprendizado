"""
Aprendendo Python:
Gerador de jogadas de d10 para Vampiro - A Máscara
(Projetinho bobo apenas para brincar com o código)

Autor: André Conti Silva
Data de início: 27/10/2019
Versão Python: 3.8.0
"""

# Importando o random para gerar números aleatórios:
from random import random


def d10():
    """
    Função que gera 1d10 com valor aleatório.
    Converte os floats do random em int, de 0 a 9, e transforma os 0 do random em 10.
    :return: O valor da jogada de 1d10, entre 1 a 10.
    """
    valor_d10 = int(random() * 10)
    if valor_d10 == 0:
        valor_d10 = 10
    return valor_d10


# Dados e dificuldade:
dados = int(input("Quantidade de dados: "))  # Define quantos d10 serão lançados
dificuldade = int(input("Dificuldade: "))  # Define a dificuldade da jogada.
# TODO: 1) Definir sucesso/falha conforme valor de dificuldade
# TODO: 2) Excluir sucessos conforme número de falhas críticas (valor_d10 == 1)

# Lança "x"d10 conforme definido pelo usuário (v2 - List Comprehension):
jogadas = [d10() for jogada in range(dados)]  # Insere todas as jogadas de d10 em uma lista
print(f"{len(jogadas)}d10:{jogadas}")  # Exibe o número de dados e os valores da lista

sucessos = filter(lambda jogada: jogada >= dificuldade, jogadas)
print(f"Sucessos: {list(sucessos)}")
# TODO: Ver finalzinha da aula 62 do curso de Python (Filter()), para usar juntamente com Map()

"""
-- AREA DE TESTES --
"""

# list_comprehension = [funçao(param) for numero in Lista_numeros]

"""
# Testando várias jogadas para ver se dá mais do que 10 no d10
for dado in range(10):
    dado = d10()
    if dado > 10:
        dado = "Maior que 10"
    print(dado)
"""

"""
# Lança "x"d10 conforme definido pelo usuário (v1 - Loop for):
for i in range(dados):
    jogada = d10()
    print(jogada)
"""

"""
print(dados) # Testa o valor de dados colocado no input
print(type(dados)) # Testa se o tipo de valor gerado no input é int
"""
