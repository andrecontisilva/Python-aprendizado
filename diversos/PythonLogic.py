# Questão 1
# A lógica abaixo é um exemplo de sequência de Fibonacci.
# A questão queria saber qual seria o resultado de print(f(10)) [== 55]
# Mais detalhes em: http://www.devfuria.com.br/logica-de-programacao/recursividade-fibonacci/
"""
def f(i):
    if i == 1 or i == 2:
        return 1
    return f(i-1) + f(i-2)


print(f(10))
"""
#Questão 2
"""
frutas = ["banana", "laranja", "manga", "uva"]

for k in range(-1, -4, -2):
    print(frutas[k])

print("\n")  # Só pra pular linha para deixar o teste abaixo mais legível:
print(frutas[-4])
"""
# Questão 3
# A lógica é um exemplo de cálculo Fatorial, neste caso 4! = 24
# (isto é, 4! = 4 x 3 x 2 x 1 = 24)
# Exemplos em: http://www.devfuria.com.br/logica-de-programacao/recursividade-fatorial/
"""
def foo(n):
    if n > 1:
        return n * foo(n-1)
    return n


print(foo(4))
"""

# Questão 4
# Exemplo de troca de posições de variáveis.
# A questão queria a resposta do 'print(a)' [cujo resultado é 6].
# Ou seja, a = 3 e b = 6, porém, em a, b = b, a, ambos trocam de posição [a = 6 e b = 3]
"""
a = 3
b = a * 2
a, b = b, a
print(a)
print(b)
"""
