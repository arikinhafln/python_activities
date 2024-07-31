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
print(f'Seu Índice de Massa Corporal (IMC) é: {imc:.2f')
      

      