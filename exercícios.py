#Exercício1
n1 = int(input('Digite o seu número da sorte:'))
n2 = int(input('Digite um número qualquer:'))
soma = n1 + n2
multiplicação = n1 * n2
divisão = n1 / n2
subtração = n1 - n2
print(f'A soma dos número digitados é: {soma}, 
      a multiplicação dos números digitados é: {multiplicação}, 
      a divisão dos números digitados é{divisão} e a subtração dos números digitados é: {subtração}')



#Exercício 2
ano_atual = int(2024)
ano_nascimento = int(input('Digite o ano do seu nascimento:'))
idade = ano_atual - ano_nascimento
print(f'Sua idade atual é: {idade}')


#Exercício 3
km = float(input('Digite a quantidade de quilometros'))
metros = km * 1000
centimetros = km * 100000
milimetros = km * 1000000


#Exercício 4
litros = float(input('Quantos litros foram consumidos? '))
distancia = float(input('Qual a distância percorrida em km? '))
if litros != 0:
      consumo_medio = distancia / litros
else:
      consumo_medio = 'Consumo não pode ser calculado com 0 litros.'

print(f'O consumo médio é: {consumo_medio:.3f} km/l')


#Exercício 5
peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = calcular_imc(peso, altura)
print(f'Seu Índice de Massa Corporal (IMC) é: {imc:.2f}')
      


#Exercício 6
ganho_por_hora = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas = float(input('Digite o número de horas trabalhadas no mês: '))
salario_total = ganho_por_hora * horas_trabalhadas
print(f'O seu salário total no mês é: R$ {salario_total:.2f}')



#Exercício 7
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite a cidade onde você mora: ")
profissao = input("Digite sua profissão: ")
    



#Exercício 8
print(f'Olá, {nome}! É um prazer te conhecer. 
          Vejo que você tem {idade} anos e mora em {cidade}. 
          Eu também sou de {cidade} e estou na mesma área de {profissao}. 
          Que coincidência incrível!')

#Exercícios Python tomada de decisão
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))         
if num1 > num2:
      maior = num1
elif num2 > num1:
      maior = num2
else:
      maior = None

if maior is not None:
      print(f'O maior número é: {maior}')
else:
      print('Os números são iguais.')


#Exercício 2
turno = input("Em que turno você estuda? Digite M para Matutino, V para Vespertino ou N para Noturno: ").upper()
if turno == 'M':
      print('Bom Dia!')
elif turno == 'V':
      print('Boa Tarde!')
elif turno == 'N':
      print('Boa Noite!')
else:
      print('Valor Inválido!')