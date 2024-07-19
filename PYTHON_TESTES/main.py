# aula 592, 593
from calculadora import soma

# print(soma(10, 20))
# print(soma(-10, 20))
# print(soma(1.5, 2.5))

try:
    print(soma('15',15))
except AssertionError as e:
    print(f'Conta inválida: {e}')
# O programa não para de funcionar porque o erro foi tratado

print('Conta', soma(25,25))
