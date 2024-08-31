'''O IMC Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso/(altura)2

Elabore um script que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo.'''

def calc_imc(peso, altura):
    imc = peso/(altura)**2
    if imc < 18.5:
        return 'Abaixo do peso'
    
    elif 18.5 <= imc <= 25:
        return 'Peso Normal'
    
    elif 25 < imc < 30:
        return 'Acima do peso'
    
    else:
        return 'Obeso'

def introducao():
   return print(f'{"--"*10} Vamos medir seu IMC {"--"*10}')

introducao()
peso = float(input('Qual seu peso? '))
altura = float(input('Agora, qual sua altura? '))

resultado = calc_imc(peso, altura)

print(f'Segundo seu IMC vc se encaixa em {resultado}')
