'''Faça um script para receber um número qualquer e informar na tela se é par ou ímpar'''

def verificar_paridade(num):
    if num % 2 == 0:
        return 'Par'
    
    else:
        return 'Ímpar'

num = int(input(f'Digite um número: '))

resultado = verificar_paridade(num)

print(f'Seu número é {resultado}')