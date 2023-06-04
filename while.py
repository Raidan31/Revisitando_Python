# Exemplo - 1 
# Sorteio de um número 
# numero_sorteado = 15   

# numero_escolhido = int(input("Informe um número entre 1 e 20: "))

# while numero_escolhido != numero_sorteado:
#     print("Tente novamente")

#     numero_escolhido = int(input("Informe um número entre 1 e 20: "))
# if numero_escolhido == numero_sorteado:
#     print("Parabens você acertou!")

# -------------------------------------------------------------------------------

# Exemplo - 2
# Contador
# contador = 0

# while contador < 5:
#     print(contador)

#     contador = contador + 1
# -------------------------------------------------------------------------------
# Exemplo - 3
# Contador com números pares
# Faça um programa que imprima na tela todos os números pares de 0 a 20.

# contador = 0

# while contador <= 20:
#         print(contador) 
#         contador += 2  //cadência da contagem indo de dois em dois
# -------------------------------------------------------------------------------
# Exemplo - 4
# Faça um programa que leia um número e imprima na tela todos os seus divisores.
# numero = int(input("Digite um número: "))
# divisor = 1

# while divisor <= numero:
#     if numero % divisor == 0:
#         print(divisor)
#     divisor += 1
# -------------------------------------------------------------------------------
# # Exemplo 5
# # Faça um programa que leia um número e imprima na tela a sequência de Fibonacci até esse número.
# num = int(input("Informe um número: "))

# fibonacci = [0, 1]
# prox_num = 1

# while prox_num <= num:
#     fibonacci.append(prox_num)
#     prox_num = fibonacci[-1] + fibonacci[-2]

# print(f"Sequência de Fibonacci até {num}: {fibonacci}")