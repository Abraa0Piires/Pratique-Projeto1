#Usuário
usuario = input("DIGITE SEU NOME,PARA ACESSAR A CALCULADORA: ")
print(f"OLÁ, {usuario}! A SEGUIR DIGITE OS VALORES E EM SEGUIDA RECEBA OS RESULTADOS ! ")
numero_1 = int(input('DIGITE O PRIMERO NUMERO: '))
numero_2 = int(input('DIGITE O SEGUNDO NUMERO: '))

# SOMA
print('{} + {} = '.format(numero_1, numero_2))
print(numero_1 + numero_2)

# SUBTRAÇÃO
print('{} - {} = '.format(numero_1, numero_2))
print(numero_1 - numero_2)

# MULTIPLICAÇÃO
print('{} * {} = '.format(numero_1, numero_2))
print(numero_1 * numero_2)

# DIVISÃO
print('{} / {} = '.format(numero_1, numero_2))
print(numero_1 / numero_2)
