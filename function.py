# Boas vindas

# Forçou a entrada de python no parametro
# def saudacao(nome, curso="python"): 
#     print(f"Seja bem vindo! {nome}")
#     print(f"É um prazer ter você fazendo parte do curso de {curso}!")

# saudacao("Raidan")

# ------------------------------------------------------------------------------------------------------------------------------

# Somador do 7

# def soma(num1, num2):
#     return num1 + num2
# # return para a função

# informe_n1 = float(input(f"Informe o valor que será somado com 7: "))

# resultado = soma(informe_n1, 7)

# print (resultado)

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 1 
# Escreva uma função que recebe um número como argumento e retorna o dobro desse número.


# def dobro(num1):
#     return num1*2


# numero_informe = float(input("Informe um número: "))

# resultado = dobro(numero_informe)

# print(resultado)

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 2
# Escreva uma função que recebe duas listas como argumento e retorna uma lista que contém apenas os elementos comuns entre as duas listas.

# def elementos_comuns(lista1, lista2):
#     lista3 = []
#     for item in lista1:
#         if item in lista2:
#             lista3.append(item)
#     return lista3

# lista1 = [2, "maçã", 5, "banana", 10, "laranja"]
# lista2 = [550, "maçã", 285, "banana", 41, "laranja"]
# lista3 = elementos_comuns(lista1, lista2)
# print(lista3)  # Saída: ['maçã', 'banana', 'laranja']

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 3
# Escreva uma função que recebe uma lista como argumento e retorna o menor elemento da lista.

# def menor (lista1):
#     resultado = min(lista1)
#     return resultado


# lista1 = [-1, 2, 5, 10, 147, 458]
# resultado = menor(lista1)
# print(resultado)

# versão atualizada chatgpt caso entre algum valor na lista que não seja um algarismo, irá retornar o resultado "none"

# def menor (lista1):
#     if all(isinstance(i, (int, float)) for i in lista1):
#         return min(lista1)
#     else:
#         return None  

# lista1 = [-1, 2, 5, 10, 147, 458, "potato"]
# resultado = menor(lista1)
# print(resultado)

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 4
# Escreva uma função que recebe uma string como argumento e retorna a mesma string com as letras em ordem reversa.
# O primeiro ":" indica que queremos pegar a string inteira, 
# e o "-1" indica que queremos percorrer a string de trás para frente, invertendo a ordem dos caracteres.


# def reversor(string):
#     return string[::-1]

# palavra = str(input("Escreva no inversor: "))
# resultado = reversor(palavra)
# print(resultado)

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 5
# Escreva uma função que recebe um número como argumento e retorna True se o número é par e False caso contrário.

# def verificador (num):
#     resultado = num % 2 
#     if resultado == 0:
#         return True
#     else:
#         return False

# num = int(input("Numero: "))
# resultado = (verificador(num))
# print(resultado)

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 6
# Escreva uma função que recebe um número como argumento e retorna True se o número é primo e False caso contrário.

# def verifica_primo(num):
#     if num <= 1:
#         return False
#     elif num == 2:
#         return True
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 7
# Escreva uma função que recebe uma lista como argumento e 
# retorna uma lista com os elementos da lista original em ordem inversa.

# def inversor (lista):
#         reversa = lista[::-1]
#         return reversa



# lista = [4, 7 , 940, 415, "batata", "planta"]

# reversa = inversor(lista)

# print (reversa)
# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 8
# Escreva uma função que recebe uma lista como argumento e retorna o maior elemento da lista.

# def maior (lista):
#     if all(isinstance(i, (int, float)) for i in lista):
#         return max(lista)
#     else:
#         return None  


# lista = [45, 789, 4562, 1587, 999999]

# great = maior(lista)

# print(great)


# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 9
# Escreva uma função que recebe uma string como argumento e retorna a mesma string sem espaços em branco.


# def unione (texto):
#     unidor = texto.replace(" ", "")
#     return unidor


# texto = str(input("Escreva o texto: "))

# unidor = unione(texto)

# print(unidor)

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 10
# Escreva uma função que recebe uma lista como argumento e 
# retorna uma lista contendo apenas os elementos únicos da lista original.

# def unicos(lista):
#     unicos = []
#     for elemento in lista:
#         if lista.count(elemento) == 1:
#             unicos.append(elemento)
#     return unicos

          


# lista = [1, 2, 3, 3, 4, 4, 5]
# unicador = unicos(lista)

# print(unicador)

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 11
# Escreva uma função que recebe uma lista de números e retorna a média aritmética desses números.

# def mediador(lista):
#     media = sum(lista)/len(lista)
#     return media

# lista = [10, 20, 52, 78, 90]

# final = mediador(lista)
# print(final)

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 12
# Escreva uma função que recebe uma string e retorna a string sem vogais.
# not in é usada em Python para verificar se um elemento não está presente em uma lista, 
# tupla, conjunto ou string.

# def remove_vogais(palavra):
#     vogais = "aeiouAEIOU"
#     resultado = ""
#     for letra in palavra:
#         if letra not in vogais:
#             resultado += letra
#     return resultado

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 13
# Escreva uma função que recebe uma lista de números e retorna uma nova lista contendo apenas os números pares da lista original.

# def par_impar (lista1):
#     lista2 = []
#     for i in lista1:
#      if (i % 2) == 0:
#         lista2.append(i)
#     return lista2

# lista1 = [10, 15, 30, 31, 23]

# lista2 = (par_impar(lista1))

# print(lista2)

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 14
# Escreva uma função que recebe uma lista de strings e um caractere, e retorna uma nova lista contendo apenas as strings que começam com o caractere especificado.

# def apenas (lista_palavra, letra):
#     nova_lista = []
#     for i in lista_palavra:
#         if i.startswith(letra):
#             nova_lista.append(i)
#     return nova_lista


# lista_palavra = ["batata", "camarão", "logica", "barata", "banana", "chingapura", "chiquititas"]

# letra = input("Digite um caractere: ")
# while len(letra) != 1:
#     letra = input("Por favor, digite apenas um caractere: ")


# nova_lista = (apenas(lista_palavra, letra))

# print(nova_lista)

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 15
# Escreva uma função que recebe uma lista de números e retorna uma nova lista contendo apenas os números que são primos.

# def primo (lista):
#     nova_lista = []
#     for numeros in lista: 
#         if numeros <= 1:
#             continue
#         elif numeros == 2:
#             nova_lista.append(numeros)
#         else:
#             for i in range(2, int(numeros**0.5)+1):
#                 if numeros % i == 0:
#                     break
#             else:
#                 nova_lista.append(numeros)
#     return nova_lista

# lista = [2, 4, 3, 6, 5, 8, 7, 9, 11, 10]

# nova_lista = primo(lista)

# print(nova_lista)

    



