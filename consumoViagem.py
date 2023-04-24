import math

# Define o preço médio do litro de combustível
preco_combustivel = float(input("Digite o preço médio do litro de combustível: "))

# Define a distância da viagem em quilômetros
distancia = float(input("Digite a distância da viagem em quilômetros: "))

# Define o consumo médio do veículo em litros por quilômetro
consumo_medio = float(input("Digite o consumo médio do veículo em litros por quilômetro: "))

# Define o valor do pedágio por trecho
valor_pedagio = float(input("Digite o valor do pedágio por trecho: "))

# Define o número de pessoas que irão na viagem
num_pessoas = int(input("Digite o número de pessoas que irão na viagem: "))

#Define o número de carros que farão a viagem
num_carros = int(input("Digite o número de carros que irão na viagem: "))

# Define o número de praças de pedágio na viagem
num_pedagios = int(input("Digite o número de praças de pedágio na viagem inlcuindo a volta: "))


# Calcula a quantidade de litros de combustível necessária para a viagem
litros_combustivel = (distancia / consumo_medio) * num_carros


# Calcula o valor total gasto em combustível
valor_combustivel = litros_combustivel * preco_combustivel

# Calcula o valor total gasto em pedágios
valor_pedagios = num_pedagios * valor_pedagio

# Calcula o valor total gasto em pedágios por carro
valor_pedagios_por_carro = valor_pedagios / num_carros

# Calcula o valor total gasto em combustível por carro
valor_combustivel_por_carro = valor_combustivel / num_carros

# Calcula o valor total da viagem por pessoa
valor_total_por_pessoa = (valor_combustivel_por_carro + valor_pedagios_por_carro) / num_carros

# Exibe o valor total da viagem para o usuário
print("O valor total da viagem por pessoa é R$", valor_total_por_pessoa)
