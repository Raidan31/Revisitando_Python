# Exemplo - 1
# Escreva uma função que recebe um dicionário e uma chave, 
# e retorna o valor associado a essa chave, se ela existir no dicionário, ou uma mensagem de erro caso contrário.


# def associador(dicio, key):
#     valor = dicio.get(key, "Não consta")
#     return valor

# dicio = {
#     "chave1": "valor1",
#     "chave2": "valor2",
#     "chave3": "valor3",
#     "chave4": "valor4",
#     "chave5": "valor5"
# }

# key = str(input("Chave: "))

# resultado = (associador(dicio, key))

# print(resultado)

# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 2
# Escreva uma função que recebe uma lista de dicionários contendo informações sobre livros (título, autor, 
# ano de publicação) e um autor, e retorna uma nova lista contendo apenas os livros escritos por esse autor.


# def livros_por_autor(livros, autor):
#     nova_lista = []
#     for livro in livros:
#         if livro["autor"] == autor:
#             nova_lista.append(livro)
#     return nova_lista



# livros = [
#     {"titulo": "A insustentável leveza do ser", "autor": "Milan Kundera", "ano_publicacao": 1984},
#     {"titulo": "A casa dos espíritos", "autor": "Isabel Allende", "ano_publicacao": 1982},
#     {"titulo": "O apanhador no campo de centeio", "autor": "J.D. Salinger", "ano_publicacao": 1951},
#     {"titulo": "Memórias de minhas putas tristes", "autor": "Gabriel Garcia Marquez", "ano_publicacao": 2004},
#     {"titulo": "Sagarana", "autor": "João Guimarães Rosa", "ano_publicacao": 1946}]

# autor_input = str(input("autor: "))

# livros = livros_por_autor(livros, autor_input)
# print(livros)

# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 3
# Escreva uma função que recebe uma lista de dicionários contendo informações sobre alunos 
# (nome, nota 1, nota 2, nota 3) e retorna uma lista contendo as médias de cada aluno.


# def media_alunos(alunos):
#     medias = []
#     for aluno in alunos:
#         nome = aluno["nome"]
#         nota1 = aluno["nota1"]
#         nota2 = aluno["nota2"]
#         nota3 = aluno["nota3"]
#         media = (nota1*2 + nota2*3 + nota3*5) / 10
#         medias.append((nome, media))
#     return medias

# alunos = [
#     {"nome": "João", "nota1": 8.0, "nota2": 7.5, "nota3": 9.0},
#     {"nome": "Maria", "nota1": 7.5, "nota2": 9.0, "nota3": 6.5},
#     {"nome": "Pedro", "nota1": 6.0, "nota2": 8.0, "nota3": 7.0},
#     {"nome": "Ana", "nota1": 9.0, "nota2": 9.5, "nota3": 10.0},
#     {"nome": "Carlos", "nota1": 5.5, "nota2": 7.0, "nota3": 6.0}
# ]

# medias = media_alunos(alunos)
# for nome, media in medias:
#     print(f"{nome}: {media}")

# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 4

# Escreva uma função que recebe um dicionário contendo informações sobre uma pessoa (nome, idade, altura, peso) 
# e retorna uma mensagem indicando se essa pessoa está acima, abaixo ou no peso ideal, 
# com base em uma fórmula de cálculo do IMC.


# def imc (pessoa):
#     altura = pessoa.get("altura")
#     peso = pessoa.get("peso")
#     calculo = peso/(altura**2)
#     if calculo < 18.5:
#         print ("Abaixo do peso Normal")
#     elif calculo >= 18.5 and calculo <= 24.9:
#         print("Peso normal")
#     else: 
#         print("Acima do peso!")
#     return calculo

# pessoa = {
#     "nome": "João",
#     "idade": 25,
#     "altura": 1.80,
#     "peso": 80.5
# }

# resultado = imc(pessoa)
# print(resultado)

# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 5
# Escreva uma função que recebe uma lista de dicionários contendo informações sobre cidades 
# (nome, população, PIB per capita) e retorna o nome da cidade com a maior população

# def max_populi(cidades):
#     max_pop = 0
#     max_city = ""
#     for cidade in cidades:
#         pop = cidade["populacao"]
#         if pop > max_pop:
#             max_pop = pop
#             max_city = cidade["nome"]
#     return max_city
   

# cidades = [    {"nome": "São Paulo", "populacao": 12252023, "pib_per_capita": 74018.70},    {"nome": "Rio de Janeiro", "populacao": 6747815, "pib_per_capita": 54543.62},    {"nome": "Belo Horizonte", "populacao": 2523794, "pib_per_capita": 42235.44},    {"nome": "Porto Alegre", "populacao": 1488252, "pib_per_capita": 48692.61},    {"nome": "Curitiba", "populacao": 1948626, "pib_per_capita": 50292.14},]

# resultado = max_populi(cidades)

# print(resultado)


# -----------------------------------------------------------------------------------------------------------------------

# Exemplo - 6
# Crie uma função que receba um dicionário e remova todos os itens dele.

# def removedor (dicionario):
#     removido = dicionario.clear()
#     return removido


# dicionario = {"a": 1, "b": 2, "c": 3}
# removedor(dicionario)

# print (dicionario)


# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 7
# Crie uma função que receba um dicionário e retorne uma cópia desse dicionário.

# def copiador (dicionario):
#     copia = dicionario.copy()
#     return copia



# dicionario = {"a": 1, "b": 2, "c": 3}
# dicionado_copiado = copiador(dicionario)

# print(dicionado_copiado)


# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 7
# Crie uma função que receba uma lista de chaves e um valor e retorne um dicionário com as chaves especificadas 
# e o valor especificado para cada chave.
# fromkeys - adiciona um valor a uma lista


# def keys_value (lista, valor):
#     dicionario = {}
#     dicionario = dicionario.fromkeys(lista, valor)
#     return dicionario

# lista = ["a", "b", "c"]
# valor = 10

# resultado = keys_value(lista, valor)

# print(resultado)
      
# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 8
# Crie uma função que receba um dicionário e uma chave, e retorne o valor associado à chave especificada, 
# ou uma mensagem informando que a chave não existe.
# get serve pra imprimir uma chave especifica

# def funcao (dicionario, chave):
#             valor = dicionario.get(chave, "Chave não existe")
#             return valor


# dicionario = {"a": 1, "b": 2, "c": 3}

# chave = "a"

# resultado = funcao(dicionario, chave)

# print(resultado)

# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 9
# Crie uma função que receba um dicionário e retorne uma lista de tuplas 
# contendo todos os pares chave-valor desse dicionário.

# def turbando (dicionario):
#     tupla = dicionario.items()
#     return tupla

# dicionario = {"a": 1, "b": 2, "c": 3}

# resultado = turbando(dicionario)
# print(resultado)

# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 10
# Crie uma função que receba um dicionário e retorne uma lista contendo todas as chaves desse dicionário.

# def chaveando (dicionario):
#     keys = dicionario.keys()
#     return keys

# dicionario = {"a": 1, "b": 2, "c": 3}

# resultado = chaveando(dicionario)
# print(resultado)

# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 11
#  Crie uma função que receba um dicionário e uma chave, e remova a chave especificada do dicionário e 
# retorne o valor associado a essa chave, ou uma mensagem informando que a chave não existe.

# Exemplo - 11
#  Crie uma função que receba um dicionário e uma chave, e remova a chave especificada do dicionário e 
# retorne o valor associado a essa chave, ou uma mensagem informando que a chave não existe.
# Pop remove uma chave específica, porém mantem o valor no dicionário

# def popando (dicionario, chave):
#     keys = dicionario.pop(chave, "chave não existe")
#     return keys

# dicionario = {"a": 1, "b": 2, "c": 3}
# chave = "a"

# resultado = popando(dicionario, chave)
# print(resultado)
# o valor da chave que foi removida 

# print (dicionario) 
# Dicionario sem a chave, porem o valor continua a ser impresso



# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 12
# Exemplo - 12
# Crie uma função que receba um dicionário e remova e retorne um par chave-valor aleatório desse dicionário, 
# ou uma mensagem informando que o dicionário está vazio.

# def popi (dicionario):
#     if not dicionario:
#         return "Dicionário está vazio"
#     item = dicionario.popitem()
#     return item

# dicionario = {"a": 1, "b": 2, "c": 3}
# resultado = popi(dicionario)
# print("                                              ")
# print(f"Removeu a seguinte chave e valor: {resultado}")
# print("                                              ")
# print(f"Dicionário com um item a menos {dicionario}")
# print("                                              ")


# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 13
# Crie uma função que receba um dicionário, uma chave e um valor padrão, 
# e retorne o valor associado à chave especificada, ou o valor padrão se a chave não existir, 
# e adicione a chave com o valor padrão ao dicionário se a chave não existir.

# -------Explicação------------------

# O código está correto, a função retorna o valor associado à chave especificada se ela existir no dicionário, 
# ou retorna o valor padrão caso contrário, adicionando a chave com o valor padrão ao dicionário 
# se a chave não existir.

# def trople (dicionario, chave, valor_padrao):
#     chave_valor = dicionario.get(chave, valor_padrao)
#     return chave_valor


# dicionario = {"a": 1, "b": 2, "c": 3}

# chave = "a"

# valor_padrao = 3

# resultado = trople(dicionario, chave, valor_padrao)
# print(resultado)

# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 14
# Crie uma função que receba dois dicionários e 
# adicione todos os pares chave-valor do segundo dicionário ao primeiro dicionário.

# Adiciona todos os valores de um dicionário a outro.

# def dupla (dicio1, dicio2):
#     dicio1.update(dicio2)
#     return

# dicio1 = {"a": 1, "b": 2, "c": 3}

# dicio2 = {"chave1": "valor1", "chave2": "valor2", "chave3": "valor3"}

# dupla(dicio1, dicio2)

# print(dicio1)

# --------------------------------------------------------------------------------------------------------------------

# Exemplo - 15
# Crie uma função que receba um dicionário e retorne uma lista contendo todos os valores desse dicionário.

# ------ps:  é importante lembrar que a ordem dos valores na lista pode não ser a mesma ordem em que os pares chave-valor foram adicionados ao dicionário, 
# pois os dicionários em Python não garantem ordem na sua estrutura interna.

# Exemplo - 15
# Crie uma função que receba um dicionário e retorne uma lista contendo todos os valores desse dicionário.


# def listando (dicio):
#     value = dicio.values()    
#     return value

# dicio = {"chave1": "valor1", "chave2": "valor2", "chave3": "valor3"}

# resultado = listando(dicio)

# print(resultado)

# ------------------------------------------------------------------------------------------------------------------------------


