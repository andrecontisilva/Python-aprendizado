""""
Primeiro script em Python para aprendizado.
-*- coding: utf-8 -*-
"""

var1 = "Hello Muthafucka!"
var2 = "Fala aê feladapúlta"

print(var1)

print(var2)

if "a" in "banana":
    print("tem 'a' em banana!")

# Loop de 2 em 2 com while:
num = 2
while num <= 10:
    print(num)
    num += 2

# Loop de 2 em 2 com for (mesmo resultado do loop com while):
for num in range(2, 12, 2):
    print(num)

# List Comprehension
amigos = ["huguinho, zezinho, luizinho"]
print([amigo.title() for amigo in amigos])
