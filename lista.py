# Exemplo - 1

# Crie uma lista com números inteiros e imprima o menor número da lista.
#  Minha resposta: 

# numeros = [32, 48, 19, 51]

# numeros.sort()

# print(numeros[0])
 
# Chatgpt
# numeros = [32, 48, 19, 51]
# print(min(numeros))

# ----------------------------------------------------------------------------------

# # Exemplo - 2 
# # Crie uma lista com palavras e imprima a palavra com mais caracteres.

# palavras = ["banana", "abacaxi", "laranja", "mamão", "uva", "baleia-jubarte"]

# maior_palavra = ""

# for palavra in palavras:
#     if len(palavra) > len(maior_palavra):
#         maior_palavra = palavra

# print("A maior palavra é:", maior_palavra)

# ----------------------------------------------------------------------------------

# # Exemplo - 3 
# Crie uma lista com nomes de pessoas e ordene os nomes em ordem alfabética.
# key=str.upper == converte as letras para maiusculas antes de ordenar

# palavras = ["barbara", "afonso", "Larissa", "Martha!", "Uriel", "Baleia-jubarte"]

# palavras.sort(key=str.upper)


# print(palavras)

# -------------------------------------------------------------------------------------

# # Exemplo - 4
# Crie duas listas com números e crie uma terceira lista com a soma dos elementos das duas primeiras listas.
# Minha resposta: 

# numeros_A = [32, 48, 19, 51]

# numeros_B = [20, 28, 3, 2023, 103]

# numeros_Soma = []

# numeros_Soma = (sum(numeros_A) + sum(numeros_B))

# print(numeros_Soma)

# Chat - gpt

# numeros_A = [32, 48, 19, 51]
# numeros_B = [20, 28, 3, 2023, 103]

# numeros_Soma = []
# for i in range(len(numeros_A)):
#     soma = numeros_A[i] + numeros_B[i] if i < len(numeros_B) else numeros_A[i]
#     numeros_Soma.append(soma)

# print(numeros_Soma)

# A diferença é que o chatgpt interpretou que os valores da lista seriam somados indvidualmente e proporcionalmente
# aos valores da outra lista.

# -----------------------------------------------------------------------------------------------------------------------------
# Exemplo - 5
# Crie uma lista com notas de alunos e imprima a média das notas.

# notas = [2, 8, 3, 10, 7]

# soma = ((sum(notas))/len(notas))

# print (soma)

# -----------------------------------------------------------------------------------------------------------------------------

# # Exemplo - 6
# # Crie uma lista com nomes de frutas e verifique se "banana" está na lista.

# frutas = ["banana", "maçã", "morango", "limão", "pera", "abacate"]

# fruta_usuario = str(input("Escreva o nome de uma fruta: "))

# if fruta_usuario in frutas:
#     print("Tem essa fruta na lista")
# else:
#     print("Não tem essa fruta na lista")

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 7
# Crie uma lista com números inteiros e remova todos os números pares da lista.
# Minha versão

# lista_numeros = [2, 5, 10, 7, 20, 15, 4, 8, 11, 12, 17, 22, 33, 14, 26]

# for i in lista_numeros:
#     if i % 2 != 0:
#         print(i)
#     else:
#         lista_numeros.remove

# Versão do chatgpt: 

# lista_numeros = [2, 5, 10, 7, 20, 15, 4, 8, 11, 12, 17, 22, 33, 14, 26]

# for i in lista_numeros:
#     if i % 2 == 0:
#         lista_numeros.remove(i)

# print(lista_numeros)

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 7
# Crie uma lista com nomes de cidades e crie uma segunda lista com as cidades que começam com a letra "S".
# O método startswith() é um método de string em Python que retorna True se a string começa com um determinado prefixo especificado 
# e False caso contrário. O método tem a seguinte sintaxe:


# cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Recife", "Fortaleza", "Salvador", "Brasília"]
# cidades_S = []

# for cidade in cidades:
#     if cidade.startswith("S"):
#         cidades_S.append(cidade)

# print(cidades_S)

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 8
# Crie uma lista com números inteiros e crie uma segunda lista apenas com os números que são múltiplos de 3.

# lista_numeros = [2, 5, 10, 7, 20, 15, 4, 8, 11, 12, 21, 60]

# lista_por_3 = []

# for i in lista_numeros:
#     if (i % 3) == 0:
#         lista_por_3.append(i)

# print(lista_por_3)

# ------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 9
# Crie uma lista com números inteiros e crie uma segunda lista com o quadrado de cada número.

# lista_numeros = [2, 5, 10, 7, 20, 15, 4, 8, 11, 12, 21, 60]

# lista_quadrado = []

# for i in lista_numeros:
#     lista_quadrado.append(i ** 2) 

# print(lista_quadrado)
