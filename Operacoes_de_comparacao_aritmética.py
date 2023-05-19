'''<<<Expressões Booleanas>>>'''

'''Exemplos de Operações de comparação Aritmética.'''

idade = 15

resultado = idade >= 18 
print(resultado)


#Exemplo: 02

prod_vendidos = 100
prod_estoque = 90

print(f'igual a (==):{prod_vendidos == prod_estoque}')
print(f'diferente de (!=): {prod_vendidos != prod_estoque}')
print(f'menor que (<):{prod_vendidos < prod_estoque}')
print(f'menor ou igual a (<=): {prod_vendidos <= prod_estoque}')
print(f'maior que (>): {prod_vendidos > prod_estoque}')
print(f'maior ou igual a (>=): {prod_vendidos >= prod_estoque}')


'''Operadores Lógicos'''

numero = 65

if numero > 60 and numero % 2 == 1:
    print('Número maior do que 60 e ímpar!')


#Exemplo: 02

combinacoes = [
    (True, True),
    (True, False),
    (False, True),
    (False, False),
]

for x, y in combinacoes:
    print(f'{x} and {y} -> {x == y}')


#Exemplo: 03

combinacoes = [
    (True, True),
    (True, False),
    (False, True),
    (False, False),  
]

for x, y in combinacoes:
    print(f'{x} or {y} -> {x or y}')


#Exemplo: 04

combinacoes = [
    True,
    False
]

for x in combinacoes:
    print(f'not {x} -> {not x}')


#Exemplo: 05

pode_parcelar = True
valor = 1500
limite = 1400

if (pode_parcelar or valor < 2000) and limite >= valor:
    print('vou comprar')

else:
    print('puts, ainda não posso comprar')
