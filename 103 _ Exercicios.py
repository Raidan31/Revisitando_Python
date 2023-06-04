# Exemplo - 1
# Faça uma função que receba uma lista de números e retorne o maior valor encontrado.

# def maior_num (list1):
#       list1.sort()
    
# list1 = [42, 2, 51, 17, 29]

# resultado = maior_num (list1)

# print(list1[0])

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 2
# Crie uma função que receba um número inteiro e 
# retorne uma lista com os primeiros números primos até esse número.

# def primeiros_primos(num):
#     primos = []
#     for i in range(2, num+1):
#         eh_primo = True
#         for j in range(2, i):
#             if i % j == 0:
#                 eh_primo = False
#                 break
#         if eh_primo:
#             primos.append(i)
#     return primos

# num = int(input("Informe o número inteiro: "))
# resultado = primeiros_primos(num)
# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 3
# Faça uma função que receba uma lista de nomes e ordene essa lista em ordem alfabética.
# Ordenar Strings em ordem crescente

# nomes = ["Raidan", "Alicia", "Lucas", "Igor", "Kelly", "Paulinho", "Gigi"]


# def name (nomes):
#     nomes_ordenado = sorted(nomes)
#     return nomes_ordenado


# resultado = name(nomes)
# print(resultado)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 4
# Escreva uma função que receba um dicionário e verifique se um determinado valor existe dentro desse dicionário.


# def verificador(dicionario, valor):
#     for v in dicionario.values():
#         if str(v).lower() == str(valor).lower():
#             return True
#     return False

# dicionario = {"a": 1, "b": 2, "c": 3}
# valor = str(input("Informe o valor: "))

# resultado = verificador(dicionario, valor)
# print(resultado)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 5
# Crie uma função que receba uma lista de números e retorne apenas os números pares dessa lista.

# def listando (lista):
#     pares = []
#     for i in lista:
#         if(i % 2) == 0:
#             pares.append(i)
#     return pares


# lista = [21, 45, 82, 25, 4]

# resultado = listando(lista)

# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 6
# Escreva um programa que receba um número inteiro e imprima "Fizz" se o número for divisível por 3, 
# "Buzz" se o número for divisível por 5 e "FizzBuzz" se o número for divisível por 3 e por 5.

# def verificador (num_int):     
#         if num_int % 3 == 0 and num_int % 5 != 0:
#             return ("Fizz")
#         elif num_int % 5 == 0 and num_int % 3 != 0:
#             return ("Buzz")
#         elif num_int % 3 == 0 and num_int % 5 == 0:
#             return("FizzBuzz")
#         else:
#              return str("O número digitado não corresponde aos requisitos")
        
# num_int = int(input("Numero inteiro: "))
# resultado = verificador(num_int)

# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 7
# Crie uma função que receba uma string e conte quantas vezes cada palavra aparece nessa string.

# def contador (string, palavra):
#     valor = string.count(palavra)
#     return valor

# string = str(input("Informe uma letra ou palavra: "))

# palavra = str(input("Informe uma letra ou palavra a ser contada: "))

# resultado = contador(string, palavra)

# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 8
# Faça uma função que receba uma lista de números e retorne uma lista com os números ordenados em ordem crescente.

# def crescente (lista):
#     lista.sort()
#     return lista

# lista = [31, 45, 12, 48, 69, 589]
# resultado = crescente(lista)

# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 9
# Escreva um programa que leia dois números inteiros e imprima todos os números primos entre esses dois números.

# def primos_verificador (num1, num2):
#     primos = []
#     for i in range(2+num1, num2+1):
#         eh_primo = True
#         for j in range(2, i):
#             if i % j == 0:
#                 eh_primo = False
#                 break
#         if eh_primo:
#             primos.append(i)
#     return primos

# num1 = int(input("Informe o número inteiro: "))
# num2 = int(input("Informe o número inteiro: "))

# resultado = primos_verificador (num1, num2)
# print(resultado)



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 10
# Faça uma função que receba uma lista de strings e retorne uma lista com as strings que possuem mais de 5 caracteres.

# def contador_carc (nomes):
#         resultado = []
#         for i in nomes:
#                 if len(i) > 5:
#                         resultado.append(i)
#         return resultado
        

# nomes = ["Ana", "Beto", "Carlos", "Débora"]

# resultado = contador_carc(nomes)

# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 11
# Crie uma função que receba uma lista de números e retorne o segundo menor número dessa lista.

# Minha solução

# def segundo_menor (lista):
#     penultimo = []
#     lista.sort()
#     penultimo.append(lista[1])
#     return penultimo

# lista = [31, 45, 12, 48, 69, 589]

# resultado = segundo_menor(lista)

# print(resultado)

# Chatgpt

# def segundo_menor(lista):
#     lista_ordenada = sorted(lista)
#     return lista_ordenada[1]

# lista = [31, 45, 12, 48, 69, 589]
# segundo_menor = segundo_menor(lista)
# print(segundo_menor)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 12
# Escreva um programa que leia uma string e verifique se ela é um palíndromo 
# (ou seja, se pode ser lida da mesma forma da esquerda para a direita e da direita para a esquerda).

# def verificador (string):
#     if string == string[::-1]:
#         return "É palindromo"
#     elif string != string[::-1]:
#         return "Não é palindromo"


# string = str(input("Informe uma palavra: "))

# resultado = verificador(string)

# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 13
# # Faça uma função que receba uma lista de números e retorne a média aritmética desses números.


# def media (lista):
#       valor =  (sum(lista))/(len(lista))
#       return round (valor, 2)  # Metódo para reduzir a quantida de casas decimais.      



# lista = [31, 45, 12, 48, 69, 589]

# resultado= media(lista)
# print(resultado)

# -------------------------------------------------------------------------------------------------------------------

# Exemplo - 14
# Escreva uma função que receba uma string e verifique se ela contém apenas caracteres alfanuméricos.

# def alpha (string):
#         if  string.isalnum():
        #          return "É alphanumérico"
#         else:
#                 return "Num é"
   


# string = input("Letras e Números: ")

# resultado = alpha (string)

# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 15
# Crie uma função que receba uma lista de strings e retorne uma lista com as strings em ordem crescente de tamanho.

# def tamanho (strings):
#         return sorted(strings, key=len)

    


# strings = [ "Carlos - Army of Lovers", "Débora Matadora", "Beto Henriqueto" ,"Eduardo", "Fernanda Juliana Alberta de Manaus", "Ana Banana"]
# resposta = tamanho(strings)
# print(resposta)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 16
# Escreva uma função que receba uma lista de números e retorne uma lista com os números pares da lista original.

# def volta_par (lista):
#     lista_par = []
#     for pares in lista:
#         if pares % 2 == 0:
#             lista_par.append(pares)    
#     return lista_par

# lista = [31, 45, 12, 48, 69, 589, 120, 26]
# resultado = volta_par (lista)
# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 17
# Faça uma função que receba um número inteiro e 
# retorne uma lista com todos os números primos menores que o número dado.


# def primos (num_int):
#     primos_recebidos = []
#     for i in range(2, num_int+1):
#         eh_primo = True
#         for j in range(2, i):
#             if i % j == 0:
#                 eh_primo = False
#                 break
#         if eh_primo:
#             primos_recebidos.append(i)
#     return primos_recebidos

# num_int = int(input("Informe o número inteiro: "))

# resultado = primos(num_int)
# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exemplo 18
# Crie uma função que receba uma lista de números e retorne a soma dos números pares da lista.

# def somador (lista):
#     pares_somados = []
#     for numeros_lista in lista:
#         if numeros_lista % 2 == 0: 
#                 pares_somados.append(numeros_lista)            
#     return sum(pares_somados)


# lista = [31, 45, 12, 48, 69, 589, 120, 26]
# resultado= somador(lista)
# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 19
# Faça uma função que receba uma lista de números e retorne uma lista com os números únicos da lista original, ou seja, removendo os números repetidos.

# Minha forma de resolver

# def unicos (lista):
#         lista_unica = []
#         for numeros in lista:
#                 if lista.count(numeros) == 1:
#                         lista_unica.append(numeros)
#         return lista_unica


# lista = [10,10, 11, 12, 12, 15, 16, 16]
# resultado = unicos (lista)
# print(resultado)

# Chatgpt 

# def unicos(lista):
#     return [num for num in lista if lista.count(num) == 1]

# lista = [10,10, 11, 12, 12, 15, 16, 16]
# resultado = unicos (lista)
# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo - 20
# Escreva uma função que receba uma lista de nomes e retorne uma lista com os nomes em ordem alfabética.


# def nomes(strings):
#     return sorted(strings)





# strings = [ "Carlos - Army of Lovers", "Débora Matadora", "Beto Henriqueto" ,"Eduardo", "Fernanda Juliana Alberta de Manaus", "Ana Banana"]
# resultado = nomes (strings)
# print(resultado)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Exemplo - 21
# # Crie uma função que receba uma lista de números e retorne o segundo maior número da lista.

# # Minha versão

# def secundo(lista):
#     segundo = []
#     lista.sort()
#     segundo.append(lista[1])
#     return segundo

# lista = [31, 45, 12, 48, 69, 589, 120, 26]
# resultado= secundo(lista)
# print(resultado)


# # Chatgpt

# def segundo_maior(lista):
#     lista.sort()
#     return lista[-2]

# lista = [31, 45, 12, 48, 69, 589, 120, 26]
# resultado= secundo(lista)
# print(resultado)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exemplo - 22
# Faça uma função que receba uma lista de números e retorne a média aritmética desses números.

# def media(lista):
#     media = sum(lista)/len(lista)
#     return media





# lista = [31, 45, 12, 48, 69, 589, 120, 26]
# resultado= media(lista)
# print(resultado)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 23
# Faça uma função que receba uma lista de dicionários com informações sobre funcionários de uma empresa (nome, salário e cargo) e retorne uma lista com os nomes dos funcionários que ganham mais de R$ 10.000,00.

# def funca(funcionarios):
#     nomes = []
#     for f in funcionarios:
#         salario = f.get("salario")
#         if salario > 10000:
#             nomes.append(f.get("nome"))
#     return nomes





# funcionarios = [    {"nome": "João", "salario": 25000, "cargo": "Analista de Sistemas"},    
#                     {"nome": "Maria", "salario": 32000, "cargo": "Coordenadora de Marketing"},    
#                     {"nome": "Pedro", "salario": 1800, "cargo": "Assistente Administrativo"},    
#                     {"nome": "Ana", "salario": 2200, "cargo": "Analista de RH"},    
#                     {"nome": "Lucas", "salario": 2800, "cargo": "Gerente de Vendas"}]

# resultado= funca (funcionarios)
# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 24
# Escreva uma função que receba uma lista de números e retorne um dicionário com a contagem de cada número na lista.

# def contagem(lista,):
#     dic_contagem = { }
#     for numero in lista:
#         dic_contagem[numero] = lista.count(numero) #[numero] está recebendo as chaves E (numero) está recebendo o valor do dicionário
#     return dic_contagem

    

# lista = [1, 3, 3, 4, 4, 4, 5]

# resultado = contagem (lista)
# print(resultado)



# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exemplo 25
# Crie uma função que receba um dicionário com as notas de um aluno em diferentes matérias (português, matemática, ciências, etc.) e retorne a média ponderada dessas notas, 
# considerando que a nota de português tem peso 2, a nota de matemática tem peso 3 e a nota de ciências tem peso 1.

# def media_avançada (notas):
#     peso_port = 2
#     peso_mat = 3
#     peso_cie = 1
#     peso = peso_mat + peso_cie + peso_port 
#     notas_agregadas = ((notas["portugues"] * peso_port) + ( notas["matematica"] * peso_mat) + notas["ciencias"]*peso_cie) / peso
#     return notas_agregadas


# notas = {
#   "portugues": 7.5,
#   "matematica": 8.0,
#   "ciencias": 6.5
# }

# res = round (media_avançada(notas), 2)
# print(res)

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exemplo 26
# Faça uma função que receba uma lista de dicionários com informações sobre produtos de uma loja (nome, preço e quantidade em estoque) e retorne o nome e a quantidade em estoque do produto mais barato.


# def produto_mais_barato(produtos):
#     menor_preco = float('inf')  # (float('inf')), para garantir que a primeira comparação de preços sempre resulte em um valor menor do que menor_preco
#     produto_mais_barato = None
#     for produto in produtos:
#         preco = produto['preco']
#         if preco < menor_preco:
#             menor_preco = preco
#             produto_mais_barato = produto
#     return produto_mais_barato['nome'], produto_mais_barato['estoque']



# produtos = [
#     {"nome": "Camisa Polo", "preco": 49.99, "estoque": 50},
#     {"nome": "Calça Jeans", "preco": 89.99, "estoque": 30},
#     {"nome": "Tênis Esportivo", "preco": 119.99, "estoque": 20},
#     {"nome": "Camiseta Básica", "preco": 29.99, "estoque": 100},
#     {"nome": "Saia Midi", "preco": 69.99, "estoque": 15}
# ]

# res = produto_mais_barato(produtos)
# print (res)


####################### Sem Float("inf") ##############################################

# def produto_mais_barato(produtos):
#     menor_preco = None
#     produto_mais_barato = None
#     for produto in produtos:
#         preco = produto['preco']
#         if menor_preco is None or preco < menor_preco:
#             menor_preco = preco
#             produto_mais_barato = produto
#     return produto_mais_barato['nome'], produto_mais_barato['estoque']


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Quando usar float("inf")?
# Por exemplo, em um problema em que se deseja encontrar o menor valor de uma lista de números, pode-se inicializar a variável que armazenará o menor valor com float("inf"), 
# pois não há nenhum número que seja maior que esse valor. 
# Dessa forma, quando um valor menor for encontrado na lista, ele substituirá o valor inicial de float("inf").

# Outra situação em que se pode usar float("inf") é quando se precisa fazer uma comparação entre valores numéricos que possam ser nulos. 
# Por exemplo, se tivermos uma lista de números e quisermos encontrar o maior valor, mas sabemos que a lista pode conter valores nulos, podemos inicializar a variável que armazenará o maior valor com float("-inf"). 
# Dessa forma, quando um valor não nulo for encontrado, ele substituirá o valor inicial de float("-inf").

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 27
# Escreva uma função que receba um dicionário com os nomes de países e suas respectivas capitais e retorne uma lista com os nomes dos países em ordem alfabética.

# def ordenador (paises_capitais):
#     paises_ordem = []
#     valores_ordenados = sorted(paises_capitais.keys())
#     paises_ordem.extend(valores_ordenados)
#     return paises_ordem
    

# paises_capitais = {
#     "Brasil": "Brasília",
#     "Estados Unidos": "Washington, D.C.",
#     "França": "Paris",
#     "Inglaterra": "Londres",
#     "Japão": "Tóquio",
#     "Itália": "Roma",
#     "Alemanha": "Berlim"
# }

# res = ordenador (paises_capitais)
# print (res)

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 28
# Crie uma função que receba um dicionário com informações sobre filmes (título, diretor, ano de lançamento e gênero) e retorne uma lista com os títulos dos filmes de um determinado gênero.

# def filmes_por_genero(filmes, genero):
#     titulos = []
#     for titulo, info in filmes.items():
#         if info["genero"] == genero:
#             titulos.append(titulo)
#     return titulos


# filmes = {
#     "O Poderoso Chefão": {
#         "diretor": "Francis Ford Coppola",
#         "ano_lancamento": 1972,
#         "genero": "Drama"
#     },
#     "Cidadão Kane": {
#         "diretor": "Orson Welles",
#         "ano_lancamento": 1941,
#         "genero": "Drama"
#     },
#     "Star Wars: Episódio IV - Uma Nova Esperança": {
#         "diretor": "George Lucas",
#         "ano_lancamento": 1977,
#         "genero": "Ficção Científica"
#     },
#     "E.T.: O Extraterrestre": {
#         "diretor": "Steven Spielberg",
#         "ano_lancamento": 1982,
#         "genero": "Aventura"
#     }
# }

# genero = str(input("Informe o Gênero do filme: "))
# titulos = filmes_por_genero(filmes, genero) 
# print(f"Filmes de {genero}: {', '.join(titulos)}")

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 29
# Faça uma função que receba um dicionário com informações sobre o clima em diferentes cidades (temperatura máxima, temperatura mínima e umidade) e retorne o nome da cidade com a menor temperatura máxima.

# def cidade_menor_temp_max(clima):
#     menor_temp = float('inf')
#     cidade_menor_temp = None
#     for cidade, dados in clima.items():
#         temp_max = dados['temperatura_maxima']
#         if temp_max < menor_temp:
#             menor_temp = temp_max
#             cidade_menor_temp = cidade
#     return cidade_menor_temp



# clima = {
#     "Rio de Janeiro": {
#         "temperatura_maxima": 35,
#         "temperatura_minima": 25,
#         "umidade": 70
#     },
#     "São Paulo": {
#         "temperatura_maxima": 30,
#         "temperatura_minima": 20,
#         "umidade": 65
#     },
#     "Belo Horizonte": {
#         "temperatura_maxima": 28,
#         "temperatura_minima": 18,
#         "umidade": 60
#     },
#     "Curitiba": {
#         "temperatura_maxima": 25,
#         "temperatura_minima": 12,
#         "umidade": 75
#     }
# }

# res = cidade_menor_temp_max(clima)
# print (res)

####################### Sem Float("inf") ##############################################

# def menor_temp_max(clima):
#     menor_temp = None
#     cidade_menor_temp = None
#     for cidade, info_clima in clima.items():
#         temp_max = info_clima['temperatura_maxima']
#         if menor_temp is None or temp_max < menor_temp:
#             menor_temp = temp_max
#             cidade_menor_temp = cidade
#     return cidade_menor_temp


# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exemplo 30
# Escreva uma função que receba uma lista de dicionários com informações sobre alunos de uma turma (nome, notas em diferentes provas, média final e situação - aprovado ou reprovado)
#  e retorne uma lista com os nomes dos alunos aprovados.

# def alunos_aprovados (turma, situacao):
#     nome_situacao = []
#     for nome in turma:
#         if nome["situacao"] == situacao:
#             nome_situacao.append(nome["nome"])
#     return nome_situacao


# turma = [
#     {"nome": "João", "notas": [8, 7, 9], "media": 8, "situacao": "Aprovado"},
#     {"nome": "Maria", "notas": [6, 5, 7], "media": 6, "situacao": "Reprovado"},
#     {"nome": "Pedro", "notas": [9, 9, 8], "media": 8.66, "situacao": "Aprovado"},
#     {"nome": "Ana", "notas": [7, 6, 7], "media": 6.66, "situacao": "Reprovado"}
# ]

# situacao = "Aprovado"
# nome_situacao = alunos_aprovados (turma, situacao)
# print(f"Esses são os {len(nome_situacao)} alunos {situacao}: {', '.join(nome_situacao)}")

# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exemplo 31
# Crie uma função que receba um dicionário com as notas de diferentes alunos em diferentes disciplinas e retorne o nome do aluno com a maior média geral.

# def maior_media (turma):
#     maior_nota = float("-inf")
#     nome_aluno = None
#     for nome, notas in turma.items():
#         notas = sum(notas.values()) / len(turma)
#         if notas > maior_nota:
#             maior_nota = notas
#             nome_aluno = nome 
#     return nome_aluno

# turma = {
#     "João": {
#         "Matemática": 8.5,
#         "Português": 7.0,
#         "História": 9.2
#     },
#     "Maria": {
#         "Matemática": 9.0,
#         "Português": 8.5,
#         "História": 7.8
#     },
#     "Pedro": {
#         "Matemática": 7.2,
#         "Português": 6.5,
#         "História": 8.0
#     }
# }

# res =  maior_media (turma)
# print (res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exemplo - 32
# Crie uma função que receba um dicionário com os nomes e as idades das pessoas e retorne a média de idade dessas pessoas.



# def media (idades):
#     var_idades = sum (idades.values())
#     divisor = len(idades)
#     return var_idades / divisor      


# idades = {
#     "João": 25,
#     "Maria": 30,
#     "Pedro": 18,
#     "Ana": 22,
#     "Lucas": 28
# }

# resultado = media (idades)
# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 33 
# Crie uma função que receba um dicionário com informações sobre carros (marca, modelo, ano de fabricação e preço) e retorne o modelo do carro mais caro.


# def modelo_caro (carros):
#     preco_carro = float("-inf")
#     modelo_mais_caro = None
#     for modelo, preco in carros.items():
#         maior_valor = preco["preco"]
#         if maior_valor > preco_carro:
#             preco_carro = maior_valor
#             modelo_mais_caro = modelo
#     return modelo_mais_caro
        

# carros = {
#     "Carro A": {
#         "marca": "Chevrolet",
#         "modelo": "Onix",
#         "ano_fabricacao": 2022,
#         "preco": 75000.00
#     },
#     "Carro B": {
#         "marca": "Ford",
#         "modelo": "Ka",
#         "ano_fabricacao": 2021,
#         "preco": 62000.00
#     },
#     "Carro C": {
#         "marca": "Volkswagen",
#         "modelo": "Gol",
#         "ano_fabricacao": 2021,
#         "preco": 58000.00
#     },
#     "Carro D": {
#         "marca": "Fiat",
#         "modelo": "Uno",
#         "ano_fabricacao": 2022,
#         "preco": 55000.00
#     }
# }


# res =  modelo_caro (carros)
# print (res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 34
# Crie uma função que receba um dicionário com informações sobre times de futebol (nome, cidade, número de torcedores e posição no ranking) e retorne o nome do time com o maior número de torcedores.

# def maior_time (times_futebol):
#     numero_torcedores = float("-inf")
#     nome_maior_time = None
#     for nome_time, torcedores in times_futebol.items():
#         n_torcedores = torcedores["torcedores"]
#         if n_torcedores > numero_torcedores:
#           numero_torcedores = n_torcedores
#           nome_maior_time = nome_time
#     return nome_maior_time

# times_futebol = {
#     "São Paulo": {
#         "cidade": "São Paulo",
#         "torcedores": 17_000_000,
#         "ranking": 8
#     },
#     "Corinthians": {
#         "cidade": "São Paulo",
#         "torcedores": 33_000_000,
#         "ranking": 5
#     },
#     "Palmeiras": {
#         "cidade": "São Paulo",
#         "torcedores": 16_000_000,
#         "ranking": 3
#     },
#     "Santos": {
#         "cidade": "Santos",
#         "torcedores": 6_500_000,
#         "ranking": 11
#     },
#     "Flamengo": {
#         "cidade": "Rio de Janeiro",
#         "torcedores": 41_000_000,
#         "ranking": 1
#     }
# }

# res =  maior_time (times_futebol)
# print (res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Exemplo 35
# Jogo da forca: Crie um programa que permite que o usuário jogue o jogo da forca, adivinhando letras de uma palavra secreta.

# def jogo_forca(palavra_secreta):
#     num_tentativas = 6
#     letras_certas = set()

#     while True:
#         for letra in palavra_secreta:
#             if letra in letras_certas:
#                 print(letra, end=' ')
#             else:
#                 print('_', end=' ')
#         print()

#         if set(palavra_secreta) == letras_certas:
#             print('Parabéns, você acertou a palavra secreta!')
#             return

#         if num_tentativas == 0:
#             print(f'Você não conseguiu adivinhar a palavra secreta ({palavra_secreta})')
#             return

#         entrada = input('Digite uma letra: ').upper()

#         if entrada in letras_certas:
#             print('Você já tentou essa letra antes.')
#         elif entrada in palavra_secreta:
#             print('Letra correta!')
#             letras_certas.add(entrada)
#         else:
#             print('Letra incorreta.')
#             num_tentativas -= 1

# palavra_secreta = 'BANANA'
# resposta = jogo_forca (palavra_secreta)
# print(resposta)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##### O que é Set() ########

# O set() é uma estrutura de dados em Python que armazena um conjunto de elementos únicos. 
# Ou seja, quando você adiciona um elemento a um set, ele verifica se já existe na coleção e, caso exista, ele não adiciona novamente. 
# Dessa forma, o set() é muito útil quando você precisa armazenar elementos únicos e não se importa com a ordem em que eles aparecem.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##### Metodo Add ########

# O método add() é um método utilizado em objetos do tipo set no Python e tem a finalidade de adicionar um elemento ao conjunto. 
# Se o elemento já estiver presente no conjunto, não é adicionado um novo elemento, mas sim mantido apenas um elemento com o mesmo valor no conjunto. 
# A sintaxe para utilizar o método add() é a seguinte:

                                        # conjunto.add(elemento)

# "conjunto" é o objeto do tipo set ao qual o elemento será adicionado e "elemento" é o valor que será adicionado ao conjunto

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 36
# Crie uma função que recebe duas listas e retorna a lista com os elementos em comum entre elas utilizando o método set().

# def comuns (lista_1, lista_2):
#     set_1 = set(lista_1)
#     set_2 = set(lista_2)
#     set_comum = set_1 & set_2 # & - O operador & está sendo usado como a interseção de dois conjuntos, ou seja, ele retorna um conjunto que contém apenas os elementos comuns a ambos os conjuntos
#     lista_comum = list(set_comum) #list - Converteu o set_comum em lista 
#     return lista_comum


# lista_1 = [1, 2, 2, 3, 3, 4, 5, 5]

# lista_2 = [1, 22, 3, 34, 55]

# res = comuns (lista_1, lista_2)
# print (res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

################# O que set1 e set2 estão fazendo? ###########################

# As variáveis set1 e set2 estão criando objetos do tipo set a partir das listas lista1 e lista2, respectivamente.
# Em outras palavras, estão criando conjuntos com os elementos das listas, sem duplicatas.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 37
# Crie uma função que recebe duas listas e retorna a lista com os elementos que não se repetem em ambas utilizando o método set().

# def incomuns(lista_1, lista_2):
#     set_1 = set(lista_1)
#     set_2 = set(lista_2)
#     set_incomum = set_1.symmetric_difference(set_2)
#     lista_incomum = list(set_incomum)
#     return lista_incomum


# lista_1 = [1, 2, 2, 3, 3, 4, 5, 5]

# lista_2 = [1, 22, 3, 34, 55]

# res = incomuns (lista_1, lista_2)
# print (res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#################### symmetric_difference ###################################

# O método symmetric_difference é um método de conjunto em Python que retorna um novo conjunto que contém todos os elementos que são exclusivos em ambos os conjuntos em comparação. 
# Em outras palavras, ele retorna um conjunto com elementos que aparecem em apenas um dos dois conjuntos.


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 38
# Crie uma função que recebe duas listas e retorna a lista com os elementos que estão em apenas uma das listas utilizando o método set().

# def comuns(lista_1, lista_2):

#     set_1 = set(lista_1)
#     set_2 = set(lista_2)
#     set_comum = set_1.difference(set_2) ### metodo difference
#     lista_comum = list(set_comum)
#     return lista_comum

# lista_1 = [1, 2, 2, 3, 3, 4, 5, 5]

# lista_2 = [1, 22, 3, 34, 55]

# res = comuns (lista_1, lista_2)
# print (res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 39
# Crie uma função que recebe uma lista e remove os elementos duplicados utilizando o método set().

# def duplicados(lista_1):
#     set_1 = set(lista_1)
#     for numeros in lista_1:
#         num = lista_1.count(numeros)
#         if num > 1:
#             set_1.discard(numeros) 
#     lista_comum = list(set_1)
#     return list(set(lista_1))

# lista_1 = [1, 2, 2, 3, 3, 4, 5, 5]

# res = duplicados(lista_1)
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 40
# Crie uma função que recebe uma lista e retorna o número de elementos únicos utilizando o método set().

# def contar_elementos_unicos(lista_1):
#     return len(set(lista_1))

# lista_1 = [1, 2, 2, 3, 3, 4, 5, 5, 7, 58, 49, 152, 59, 59]

# res = contar_elementos_unicos(lista_1)
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 41
# Crie uma função que recebe duas listas e retorna uma lista com os elementos que estão em uma lista e não na outra utilizando o método set().


# def comuns(lista_1, lista_2):

#     set_1 = set(lista_1)
#     set_2 = set(lista_2)
#     return list(set_1.difference(set_2)) + list(set_2.difference(set_1))

# lista_1 = [1, 2, 2, 3, 3, 4, 5, 5]

# lista_2 = [1, 22, 3, 34, 55]

# res = comuns (lista_1, lista_2)
# print (res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 42
# Crie uma função que recebe duas listas e retorna uma lista com os elementos que estão nas duas listas, mas não em ambas utilizando o método set().

# def comuns(lista1, lista2):
#     set1 = set(lista1)
#     set2 = set(lista2)
#     return list(set1.symmetric_difference(set2))

# lista_1 = [1, 2, 2, 3, 3, 4, 5, 5]

# lista_2 = [1, 22, 3, 34, 55]


# res = comuns (lista_1, lista_2)

# print (res)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 43
# Escreva uma função que recebe uma lista de números e retorne a soma dos valores únicos na lista utilizando o método set().

# def somador(lista_1):
#     set_1 = set(lista_1)
#     for numeros in lista_1:
#         num = lista_1.count(numeros)
#         if num > 1:
#             set_1.discard(numeros) 
#     lista_comum = list(set_1)
#     return sum(lista_comum)

# lista_1 = [1, 2, 2, 3, 3, 4, 5, 5]

# res = somador(lista_1)
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 44
# Crie uma função que recebe duas strings e retorne uma lista com os caracteres que aparecem em ambas as strings usando o método set().


# def verificador (st1, st2):
#     set1 = set(st1)
#     set2 = set(st2)
#     ambos =  set1.intersection(set2)
#     return ambos

# st1 = "Raidane"
# st2 = "Tatakae"

# res = verificador (st1, st2)
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 45
# Crie uma função que recebe uma lista de números e retorne uma lista contendo apenas os números pares utilizando o método set().

# Minha função: utiliza o metódo set de maneira incorreta, ainda que retorne o resultado correto.
# O método set() é usado para converter a lista em um conjunto e assim remover elementos duplicados, 
# e não para adicionar ou remover elementos como está sendo feito nesta implementação. 

# def pares (lista1):
#     set1 = set(lista1)
#     for numeros in lista1:
#         if numeros % 2 == 0:
#             set1.add(numeros)
#         else:
#             set1.discard(numeros)
#     lista_pares = list(set1)
#     return lista_pares




# lista1 = [1, 2, 2, 3, 3, 4, 5, 5]
# res = pares (lista1)
# print(res)

# Versão Chatgpt: Retorna os mesmos resultados, porém utiliza o metódo set de maneira correta

# def pares(lista1):
#     set1 = set(lista1)
#     set_pares = set()
#     for num in set1:
#         if num % 2 == 0:
#             set_pares.add(num)
#     return list(set_pares)


# lista1 = [1, 2, 2, 3, 3, 4, 5, 5]
# res = pares (lista1)
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

################### set_pares = set() ############################################ 

# Está criando um conjunto vazio chamado set_pares. Conjuntos em Python são estruturas de dados que armazenam elementos únicos e não mantêm uma ordem definida. 
# Nesse caso, esse conjunto vazio será preenchido com números pares da lista lista1.


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 46
# Escreva uma função que recebe uma lista de palavras e retorne uma lista contendo apenas as palavras que começam com a letra "a" usando o método set().

# def palavra_a (string):
#     set1 = set(string)
#     a_set = set()
#     for palavras in string:
#         if palavras.startswith("a"):
#             a_set.add(palavras)
#     return list(a_set)

# string = ["amor", "amigo", "bola", "bebida", "bicicleta", "bom", "casa", "cachorro", "caneta", "carro"] 

# res = palavra_a (string)
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 47
# Crie uma função que recebe uma string e retorne uma lista com as palavras únicas presentes na string utilizando o método set().

# def unicas(string):
#     palavras = string.split()
#     set_unicas = set()
#     for palavra in palavras:
#         if palavras.count(palavra) == 1:
#             set_unicas.add(palavra)
#     return list(set_unicas)
           

# string = "amor casa bola amor cachorro gato cachorro"
# res = unicas (string)
# print(res)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

######### Split ############ metodo string

# Split separa a string em palavras usando o método split(). 
# Em seguida, ela itera sobre as palavras e adiciona aquelas que aparecem apenas uma vez a um conjunto (set_unicas). 
# Finalmente, ela converte esse conjunto em uma lista e retorna o resultado.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 48
# Escreva uma função que recebe uma lista de números e retorna um dicionário com a contagem de cada número.

# def contador(lista):
#     contagem = {}
#     for numero in lista:
#         if numero in contagem:
#             contagem[numero] += 1
#         else:
#             contagem[numero] = 1
#     return contagem

# lista = [1, 2, 2, 3, 3, 4, 5, 5]
# resultado = contador(lista)
# print(resultado)
        
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 49
# Crie uma função que recebe uma lista de strings e retorna um dicionário com a contagem de cada palavra, ou seja, com a quantidade vezes em que a palavra está presente na lista

# def contador(lista):
#     contagem = {}
#     for palavra in lista:
#         if palavra in contagem:
#             contagem[palavra] += 1
#         else:
#             contagem[palavra] = 1
#     return contagem

# string = ["amigo", "amigo", "bola", "bola", "bom", "bom","bom", "cachorro", "caneta", "carro"] 

# resultado = contador(string)
# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 50
# Escreva uma função que recebe duas listas de números e retorna uma lista com os números que aparecem em ambas as listas usando o método set e o método intersection().

# def ambas (lista1, lista2):
#     set1 = set(lista1)
#     set2 = set(lista2)
#     contagem = set()
#     for numeros in set1:
#         if numeros in set2:
#             contagem = set1.intersection(set2)
#     return list(contagem)


# lista1 = [1, 2, 2, 3, 3, 4, 5, 5]

# lista2 = [1, 22, 3, 34, 55]

# res = ambas (lista1, lista2)
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 51
# Crie uma função que recebe um dicionário com a contagem de cada palavra em um texto e retorna uma lista das palavras mais comuns.

# def valores (palavras):
#     min_ocorrencias = min(palavras.values())
#     comuns = []
#     for palavra, ocorrencias in palavras.items():
#         if ocorrencias >= min_ocorrencias + 2:
#             comuns.append(palavra)
#     return comuns

        


# palavras = {'a': 5, 'vida': 2, 'é': 2, 'uma': 3, 'viagem': 1, 'cheia': 1, 'de': 2, 'altos': 1, 'e': 7, 'baixos.': 1, 'devemos': 2, 
#             'estar': 1, 'preparados': 1, 'para': 2, 'enfrentar': 1, 'os': 1, 'desafios': 1, 'que': 3, 'surgem': 1, 'no': 2, 'caminho,': 1, 'pois': 1, 
#             'são': 2, 'eles': 1, 'nos': 1, 'fazem': 1, 'crescer': 1, 'evoluir.': 1, 'mas': 1, 'também': 1, 'desfrutar': 1, 'dos': 1, 'momentos': 1, 
#             'tranquilidade': 1, 'felicidade,': 1, 'essenciais': 1, 'nossa': 1, 'saúde': 1, 'mental': 1, 'emocional.': 1, 'dádiva': 1, 'cabe': 1, 'nós': 2, 
#             'aproveitá-la': 1, 'da': 1, 'melhor': 1, 'maneira': 1, 'possível,': 1, 'respeitando': 1, 'mesmos': 1, 'aos': 1, 'outros,': 1, 'deixando': 1, 
#             'marca': 1, 'positiva': 1, 'mundo.': 1}

# res = valores (palavras)
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 52
# Escreva uma função que recebe uma lista de tuplas, onde cada tupla contém um nome e uma idade, e retorna um dicionário com a média de idade para cada nome.


# def media(lista_tuplas):
#     dicio = {}
#     for nome, idade in lista_tuplas:
#         if nome in dicio:
#             dicio[nome][0] += idade
#             dicio[nome][1] += 1
#         else:
#             dicio[nome] = [idade, 1]
#     for nome, (soma_idades, qtd) in dicio.items():
#         dicio[nome] = soma_idades / qtd
#     return dicio


# lista_tuplas = [("João", 20), ("Maria", 30), ("Pedro", 25), ("Ana", 22), ("João", 10), ("Maria", 50 ), ("Maria", 0.1) ]

# res = media (lista_tuplas) 
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 53
# Crie uma função que recebe uma lista de palavras e retorna uma lista com as palavras que aparecem mais de uma vez usando o método set.

# def mais_vezes (lista):
#     set1 = set(lista)
#     set_fim = set()
#     for palavras in lista:
#        if lista.count(palavras) > 1:
#            set_fim.add(palavras)
#     return list(set_fim)


# lista = ["casa", "carro", "casa", "bicicleta", "carro", "avião", "casa", "moto"]

# res = mais_vezes(lista)
# print(res)

######################################### adição ao exemplo : retorna as palavras que são únicas #####################################

# def mais_vezes(lista_palavras):
#     set_palavras = set(lista_palavras)
#     repetidas = list(set([palavra for palavra in lista_palavras if lista_palavras.count(palavra) > 1]))
#     unicas = list(set_palavras - set(repetidas))
#     return (repetidas, unicas)

# lista_palavras = ["casa", "carro", "casa", "bicicleta", "carro", "avião", "casa", "moto"]
# res = mais_vezes (lista_palavras)
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Exemplo 54
# # Escreva uma função que recebe um dicionário com a contagem de cada palavra em um texto e retorna uma lista das palavras que aparecem apenas uma vez.

# # Nesta parte o código está realizando a contagem de cada palavra do texto e colocando em um dicionário {"palavra" : nº de vezes em que ela aparece} 

# def contagem (texto):
#     dicionario = {}
#     divisor = texto.lower().split()
#     for palavras in divisor: 
#         if palavras not in dicionario:
#             dicionario[palavras] = 1
#         else:
#             dicionario[palavras] += 1
#     return dicionario
    

# texto = "A paçoca café é um doce típico brasileiro que faz muito sucesso em todo o país. Principalmente junto com café É feita com amendoim torrado açúcar e sal e pode ser encontrada em diversos formatos e sabores Gosto de paçoca com café hummm café "

# res = contagem(texto)

# # No fim, pegou o dicionário elaborado no exercicío anterior e o colocou em uma lista apenas com as palavras que não se repetiam. 

# def unicas (res):
#     min_ocorrencias = min(res.values())
#     comuns = []
#     for palavra, ocorrencias in res.items():
#         if ocorrencias == 1:
#             comuns.append(palavra)
#     return comuns
   
# resultado = unicas(res)
# print(resultado)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 55
# Crie uma função que recebe uma lista de dicionários, onde cada dicionário contém informações sobre um aluno (nome, nota 1, nota 2, nota 3), 
# e retorna uma lista com os nomes dos alunos que tiveram média maior do que 7.0.

# def aprovados (alunos):
#     comuns = []

#     for nome in alunos:
#         if (nome["nota1"] + nome["nota2"] + nome["nota3"])/ 3 > 7:
#             comuns.append(nome["nome"])
#     return comuns

# alunos = [
#     {"nome": "João", "nota1": 7.5, "nota2": 8.0, "nota3": 6.5},
#     {"nome": "Maria", "nota1": 9.0, "nota2": 8.5, "nota3": 7.0},
#     {"nome": "Pedro", "nota1": 2.0, "nota2": 7.0, "nota3": 3.0},
#     {"nome": "Lucas", "nota1": 1.0, "nota2": 6.5, "nota3": 2.0}
# ]


# res = aprovados (alunos) 
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 56
# # Escreva uma função que recebe uma lista de strings e retorna um dicionário com a contagem de cada letra em todas as strings.

# def letras_numeros (nomes):
#     dicio = {}
#     for palavras in nomes:
#         for letras in palavras:
#             if letras.isalnum(): # Metodo string
#                 dicio[letras] = dicio.get(letras, 0) + 1
#     return dicio

# nomes = ["Ana", "João", "Maria", "Pedro"]
# res=  (letras_numeros (nomes))
# print(res)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 57
# Crie uma função que recebe uma lista de números e retorna um dicionário com a contagem de números pares e ímpares.


######################### Versão em que a função retorna se os números são pares ou ímpares #############################

# def pares_impares(lista):
#     dicio = {}
#     for numeros in lista:
#         if numeros % 2 == 0:
#             dicio[numeros] = "pares"
#         else: 
#             dicio[numeros] = "ímpares"
#     return dicio



# lista =  [10, 22, 31, 41, 58, 64, 47, 38, 79, 156801]
# res = pares_impares(lista)
# print(res)

##################### Versão correta #####################################################################################

# def pares_impares(lista):
#     dicio = {"pares": 0, "ímpares": 0}
#     for numeros in lista:
#         if numeros % 2 == 0:
#             dicio["pares"] += 1
#         else: 
#             dicio["ímpares"] += 1
#     return dicio

# lista = [10, 22, 31, 41, 58, 64, 47, 38, 79, 156801]
# res = pares_impares(lista)
# print(res) 

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exemplo 58
# Crie uma função que recebe uma lista de strings e retorna um dicionário com a contagem de letras em cada palavra.

# def contador(lista_palavras):
#     resultado = {}
#     for palavra in lista_palavras:
#         resultado[palavra] = len(palavra)
#     return resultado


# string = ["amor", "amigo", "bola", "bebida", "bicicleta", "bom", "casa", "cachorro", "caneta", "carro"] 

# resultado = contador(string)
# print(resultado)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 59
# Crie uma função que recebe duas listas de números e retorna a intersecção entre elas (os números que aparecem em ambas as listas).

# def intersec (lista, lista2):
#     set1 = set(lista)
#     set2 = set(lista2)
#     final = set()
#     for numeros in lista:
#         if numeros in lista2:
#             final = ( set1.intersection(set2))
#     return final


# lista = [10, 22, 31, 41, 58, 64, 47, 38, 79, 156801]
# lista2 = [10, 2, 3, 41, 5, 64, 47, 38, 79, 156801]

# res = intersec (lista, lista2)
# print(res)


########### Simplificação do Código ###########

# def intersec(lista1, lista2):
#     set1 = set(lista1)
#     set2 = set(lista2)
#     inter = set1 & set2
#     return list(inter)

# lista = [10, 22, 31, 41, 58, 64, 47, 38, 79, 156801]
# lista2 = [10, 2, 3, 41, 5, 64, 47, 38, 79, 156801]

# res = intersec (lista, lista2)
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 60
# Escreva uma função que recebe uma lista de palavras e retorna um dicionário com a contagem de cada letra de cada palavra.

# def strings (lista):
#     dicio = {}
#     for palavras in lista:
#             if palavras in lista: 
#                 dicio[palavras] = len(palavras)
#     return dicio


# lista = ["banana", "buga buga", "retorno", "dos", "que", "não", "foram"]

# res = (strings (lista))
# print(res)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 61
# Faça uma função que recebe uma lista de dicionários, onde cada dicionário contém informações sobre um aluno (nome, nota 1, nota 2, nota 3), 
# e retorna uma lista com os nomes dos alunos que tiveram média maior do çque 8.0.


# def media_8 (alunos):
#     lista_final = []
#     for notas in alunos:
#         if (notas["nota1"] +  notas["nota2"] +  notas["nota3"]) / 3 > 8:
#             lista_final.append(notas["nome"])
#     return lista_final



# alunos = [
#     {"nome": "João", "nota1": 7.5, "nota2": 8.0, "nota3": 6.5},
#     {"nome": "Maria", "nota1": 9.0, "nota2": 8.5, "nota3": 7.0},
#     {"nome": "Pedro", "nota1": 2.0, "nota2": 7.0, "nota3": 3.0},
#     {"nome": "Lucas", "nota1": 1.0, "nota2": 6.5, "nota3": 2.0}
# ]
# res = (media_8 (alunos))
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 62
# Crie uma função que recebe uma lista de strings e retorna um conjunto com as letras que aparecem em todas as strings.

# def conjuntos(lista):
#     set1 = set(lista[0]) # inicia com as letras do primeiro elemento
#     for palavra in lista:
#         set1 = set1.intersection(set(palavra))
#     return set1

# lista = ["banana", "buga buga", "retorna", "dosa", "qua", "nãoa", "foram"]
# res = conjuntos(lista)
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 63
# Escreva uma função que recebe uma lista de números e retorna um dicionário com a contagem de números pares e ímpares.

# def count_pares_impares(lista):
#     count_pares = 0
#     count_impares = 0
    
#     for num in lista:
#         if num % 2 == 0:
#             count_pares += 1
#         else:
#             count_impares += 1
    
#     dicio = {"pares": count_pares, "impares": count_impares}
#     return dicio

# lista = [10, 2, 3, 41, 5, 64, 47, 38, 79, 156801]
# res = count_pares_impares(lista)
# print(res)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 64
# Faça uma função que recebe uma lista de dicionários, onde cada dicionário contém informações sobre um produto (nome, preço, quantidade), e retorna o nome do produto mais caro.

# def produto_burges (produtos):
#     infinito_negativo = float("-inf")
#     dicio = None
#     for nome in produtos:
#         preço = nome["preço"]
#         if preço > infinito_negativo:
#             infinito_negativo = preço
#             dicio = nome
#     return dicio["nome"], dicio["preço"]


# produtos = [    {"nome": "Maçã", "preço": 8.50, "quantidade": 10},    {"nome": "Banana", "preço": 3.00, "quantidade": 8},    {"nome": "Abacaxi", "preço": 5.00, "quantidade": 5}]

# res = produto_burges (produtos)
# print(res)
 

########### Explicação do pq infinito_negativo = preço e dicio = nome #############

# Na função produto_burges, a variável infinito_negativo é inicializada com o menor valor possível, para garantir que o primeiro produto da lista seja comparado corretamente. 
# A variável dicio é inicializada com None porque ainda não sabemos qual produto tem o maior valor.

# Dentro do loop for, primeiro verificamos se o preço do produto atual (preço) é maior do que o valor mais alto encontrado até agora (infinito_negativo). 
# Se sim, atualizamos o valor mais alto (infinito_negativo) e o dicionário correspondente ao produto com o maior valor (dicio). Por isso, infinito_negativo é atualizado com preço e dicio é atualizado com nome. 
# Finalmente, a função retorna o nome e o preço do produto com o maior valor.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 65
# Crie uma função que recebe duas listas de números e retorna a união entre elas (todos os números que aparecem em pelo menos uma das listas).

# def union (lista1, lista2):
#     set1 = set(lista1)
#     set2 = set(lista2)
#     inter = set1.union(set2)
#     return list(inter)

# lista = [10, 22, 31, 41, 58, 64, 47, 38, 79, 156801]
# lista2 = [10, 2, 3, 41, 5, 64, 47, 38, 79, 156801]

# res = union (lista, lista2)
# print(res)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 66
# Escreva uma função que recebe uma lista de palavras e retorna um dicionário com as letras que aparecem em cada palavra e a contagem de vezes que elas aparecem.

# def contagem(lista):
#     dicio = {}
#     for palavra in lista:
#         dicio[palavra] = {}
#         for letra in palavra:
#             if letra in dicio[palavra]:
#                 dicio[palavra][letra] += 1
#             else:
#                 dicio[palavra][letra] = 1
#     return dicio

# lista = ['raidan', 'owuuu', 'nnrlx', 'doald', 'rdfnl', 'euqrc', 'okxrj', 'hudsj', 'xozbl', 'elgoj']
# res = contagem(lista)
# print(res)


### Explicação da condicional IF ####

# Essa parte do código verifica se a letra já existe no dicionário da palavra. Se a letra já existe, a contagem de sua ocorrência é incrementada em 1. 
# Caso contrário, a letra é adicionada ao dicionário da palavra com o valor 1, indicando que ela ocorreu pela primeira vez na palavra. 
# Em outras palavras, essa parte do código está atualizando a contagem de ocorrências de cada letra em cada palavra do dicionário. 
# O resultado final é um dicionário com as letras que aparecem em cada palavra e a contagem de vezes que elas aparecem.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 67
# Faça uma função que recebe uma lista de dicionários, onde cada dicionário contém informações sobre um aluno (nome, nota 1, nota 2, nota 3), e retorna a média da turma.


# def turma_media (lista):
#     soma_notas = 0
#     for i in lista:
#         soma_notas += i["nota1"] +  i["nota2"] +  i["nota3"]
#     return soma_notas / (len (lista)*3)



# lista = [
#     {"nome": "João", "nota1": 7.5, "nota2": 8.0, "nota3": 6.5},
#     {"nome": "Maria", "nota1": 6.0, "nota2": 5.5, "nota3": 8.5},
#     {"nome": "Pedro", "nota1": 9.0, "nota2": 9.5, "nota3": 7.0},
#     {"nome": "Ana", "nota1": 8.0, "nota2": 7.0, "nota3": 6.0},
#     {"nome": "Paulo", "nota1": 5.5, "nota2": 4.5, "nota3": 7.5}
# ]


# res = (turma_media (lista))

# print(res)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 68
# Crie uma função que recebe uma lista de números e retorna um conjunto com os números repetidos (que aparecem mais de uma vez na lista).


# def repetidos (lista):
#     lista2 = []
#     for numeros in lista:
#         if lista.count(numeros) > 1:
#             lista2.append(numeros)
#     return lista2
 
# lista = [10, 22, 31, 41, 58, 64, 47, 38, 79, 156801, 10, 22, 31, 41, 58]
# res = repetidos (lista)
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 69
# Crie um programa que pede para o usuário digitar o nome de um produto e seu preço, e armazena essas informações em um dicionário. 
# O programa deve continuar pedindo ao usuário que adicione novos produtos até que ele digite "sair". No final, o programa deve imprimir os produtos com seus preços.

# def dicio_produtos():
#     dicio = {}

#     while True:
#         produto = input("Digite o nome do produto ou 'sair' para encerrar: ")
#         if produto.lower() == "sair":
#             break
#         try:
#             preco = float(input("Informe o preço: "))
#         except ValueError:
#             print("Preço inválido. Por favor, digite um número válido.")
#             continue        
#         dicio[produto] = preco

#     return dicio


# saida = dicio_produtos()
# print(saida)


##### Explicação Try-except ######

# Neste exemplo o bloco foi utilizado para exibir uma mensagem de erro caso fosse digitado um valor na entrada de preço inválido, 
# desta forma o bloco except recebe o erro e imprime uma mensagem. 


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 70
# Crie um programa que simula um banco. Ele deve começar com um dicionário vazio, onde a chave é o número da conta e o valor é o saldo. O programa deve pedir ao usuário que escolha entre as seguintes opções:

# Adicionar uma nova conta com saldo inicial
# Fazer um depósito em uma conta existente
# Fazer um saque de uma conta existente
# Ver o saldo de uma conta existente
# Sair do programa
# O programa deve continuar pedindo ao usuário que faça uma escolha até que ele escolha "sair".

# def banco_dan ():
#     dicio = {}
    

#     while True:
#         entrada = int (input ( " 1 - Adicionar uma nova conta com saldo inicial; 2 - Fazer um depósito em uma conta existente; 3 -Fazer um saque de uma conta existent; 4 - Ver o saldo de uma conta existente; 5 - Sair do programa:  " ))
#         if  entrada == 1:
#             nova_conta = int(input("Informe o Nº da Conta: "))
#             saldo_inicial = int(input("Informe o valor do deposito do saldo inicial: "))
#             dicio[nova_conta] = saldo_inicial
#             print (f"Foi depositado na conta: {nova_conta} o valor de R$ {saldo_inicial},00   ////////// Operação Encerrada /////////// Retornando ao menu inicial ///////////")         
#         elif entrada == 2:
#             selecionar_conta =  int(input("Informe o número da conta que deseja realizar o deposito: "))
#             deposito_valor = int(input("Informe o valor que deseja depositar: "))
#             dicio[selecionar_conta] = dicio.get(selecionar_conta) + deposito_valor
#             print(f"Foi depositado na conta {selecionar_conta}, o valor de {deposito_valor},00   ////////// Operação Encerrada /////////// Retornando ao menu inicial ///////////")
#         elif entrada == 3:
#             conta_saque =  int(input("Informe o número da conta que deseja realizar o saque: "))
#             valor_saque = int(input("Informe o valor que deseja sacar: "))
#             if valor_saque >  dicio.get(conta_saque):
#                 print("Saldo Insuficiente!")
#             else:
#                  dicio[conta_saque] = dicio.get(conta_saque) - valor_saque
#                  saldo = dicio.get(conta_saque) 
#                  print(f"A conta {conta_saque}, foi realizado o saque de {valor_saque},00, saldo atual {saldo}  ////////// Operação Encerrada /////////// Retornando ao menu inicial ///////////")
#         elif entrada == 4:
#             conta_saldo = int(input("Informe o número da conta que deseja verificar o saldo: "))
#             saldo_conta = dicio.get(conta_saldo)
#             print (f"O saldo da conta {conta_saldo} é de R$ {saldo_conta},00 ")
#         elif entrada == 5:
#             print("Obrigado por ser nosso cliente! Volte Sempre!!")  
#             break
#         else:
#             print("Valor inválido, selecione um outro número!") 
            

# saida = banco_dan ()
# print (saida)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 71
# Crie um programa que pede ao usuário que digite uma frase e conta quantas vezes cada palavra aparece na frase. 
# O programa deve armazenar essas informações em um dicionário e imprimir a contagem no final.

# def cont_palavras (entrada):
#     dicio = {}
#     divisor = entrada.split()
#     for palavras in divisor:
#         dicio[palavras] = divisor.count(palavras)
#     return dicio



# entrada = input("Informe uma frase: ")
# res = cont_palavras (entrada) 
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 72
# Crie um programa que simula um jogo de cartas. O programa deve começar com um baralho completo (todas as cartas de um baralho de 52 cartas) e uma lista vazia para cada jogador. 
# Em seguida, o programa deve pedir ao usuário que digite o número de jogadores. O programa deve distribuir as cartas igualmente entre os jogadores e imprimir a lista de cartas de cada jogador.

# import random

# def jogo_cartas():
#     baralho_completo = [  
#         "Ás de Espadas",
#         "2 de Espadas",
#         "3 de Espadas",
#         "4 de Espadas",
#         "5 de Espadas",
#         "6 de Espadas",
#         "7 de Espadas",
#         "8 de Espadas",
#         "9 de Espadas",
#         "10 de Espadas",
#         "Valete de Espadas",
#         "Rainha de Espadas",
#         "Rei de Espadas",
#         "Ás de Copas",
#         "2 de Copas",
#         "3 de Copas",
#         "4 de Copas",
#         "5 de Copas",
#         "6 de Copas",
#         "7 de Copas",
#         "8 de Copas",
#         "9 de Copas",
#         "10 de Copas",
#         "Valete de Copas",
#         "Rainha de Copas",
#         "Rei de Copas",
#         "Ás de Ouros",
#         "2 de Ouros",
#         "3 de Ouros",
#         "4 de Ouros",
#         "5 de Ouros",
#         "6 de Ouros",
#         "7 de Ouros",
#         "8 de Ouros",
#         "9 de Ouros",
#         "10 de Ouros",
#         "Valete de Ouros",
#         "Rainha de Ouros",
#         "Rei de Ouros",
#         "Ás de Paus",
#         "2 de Paus",
#         "3 de Paus",
#         "4 de Paus",
#         "5 de Paus",
#         "6 de Paus",
#         "7 de Paus",
#         "8 de Paus",
#         "9 de Paus",
#         "10 de Paus",
#         "Valete de Paus",
#         "Rainha de Paus",
#         "Rei de Paus" ]

#     random.shuffle(baralho_completo)
    
#     jogadores = []
#     while True: # while True: é uma estrutura de controle em Python que cria um loop infinito que só será interrompido quando ocorrer alguma condição de saída.

#         entrada = int(input("Informe o número de jogadores: "))
#         if entrada > 52:
#             print("Informe um número menor que 52")
#         elif entrada % 2 != 0:
#             print("Favor informa um número par")
#         else:
#             cartas_por_jog = len(baralho_completo) // entrada
#             for jogador in range(entrada):
#                 jogadores.append([])
#                 for carta in range(cartas_por_jog):
#                     jogadores[jogador].append(baralho_completo.pop())

#             for i, jogador in enumerate(jogadores):
#                 print(f"Cartas do jogador {i+1}: {jogador}")

#             return jogadores

# res = jogo_cartas()
# print(res)

######### Metodo Enumerate ###############

# O enumerate é uma função em Python que permite iterar sobre uma lista (ou outra estrutura de dados iterável) ao mesmo tempo em que acessa o índice do elemento atual da lista.


#### Explicação do Import Random e Metodo Shuffle ############

# random: é um módulo em Python que fornece funcionalidades para gerar valores aleatórios. Ele é usado para várias aplicações como jogos, simulações e análises estatísticas.

# shuffle(seq): Embaralha aleatoriamente a sequência seq.

# A função shuffle do módulo random é usada para embaralhar uma sequência. Ela pode ser usada para embaralhar qualquer tipo de sequência, como uma lista, tupla ou string.

# A função shuffle não retorna um valor. Em vez disso, ela altera a sequência original e a embaralha aleatoriamente. Ou seja, depois de usar a função shuffle, 
# a sequência original estará embaralhada e não poderá ser recuperada.

# A função shuffle trabalha de maneira determinística, o que significa que ela produz a mesma sequência de embaralhamento sempre que for chamada com a mesma sequência de entrada e com a mesma semente 
# (se a semente for especificada).

# A função shuffle é muito útil em jogos, como cartas e dados, quando se precisa de um embaralhamento aleatório dos elementos da sequência.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 73
# Contagem de letras
# Crie um programa que receba uma string do usuário e conte quantas vezes cada letra aparece na string. Armazene a contagem em um dicionário e imprima o resultado.


# def contagem():
    
#     dicio = {}
#     while True:
#         entrada = input("Informe uma frase: ")
#         divisor = entrada.split()
#         for palavras in divisor:
#             for letras in palavras:
#                 dicio[letras] = palavras.count(letras)
#         return dicio        

# res = contagem()
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 74
# Cadastro de clientes
# Crie um programa que permita o cadastro de clientes. O programa deve solicitar o nome, o e-mail e o telefone do cliente e armazená-los em um dicionário. 
# O programa deve continuar permitindo o cadastro de novos clientes até que o usuário decida encerrar o programa. Ao final, imprima todos os clientes cadastrados.

#**** Adição de dificuldade: coloque a opção de modificar os dados já inseridos no sistema.
#**** Adição de dificiculdade: coloque a opção de imprimir todos os dados sem encerrar o sistema

# def cadastro ():

#     dicio = {}
#     while True:
        
#         entrada_inicial = int (input ( " 1 - Adicionar um novo cliente; 2 - Correção de dados; 3 - Acessar Todos os dados; 4 - Acesse uma conta especifica; 0 - Sair do programa;  " ))

#         if entrada_inicial == 1:
#             entrada_nome = input("Infore o nome do cliente: ")
#             entrada_email = input("Informe o email do cliente: ")
#             entrada_tel = int(input("Informe o telefone do cliente: "))
#             nome_email_tel = (f"{entrada_nome} - {entrada_email} - {entrada_tel}")
#             chave = len(dicio)
#             dicio[chave] = nome_email_tel

#         elif entrada_inicial == 2:
#             verificação = int(input("Você tem certeza que deseja modificar os dados? Caso deseje continuar tecle (1). Caso deseje encerrar tecle (0):" ))
#             if verificação == 0:
#                 return
#             elif verificação == 1:
#                 dados_nome = int(input("Informe o número do cliente: "))
#                 cliente = dicio.get(dados_nome)
#                 del dicio[dados_nome]
#                 novo_nome = input("Infore o nome do cliente: ")
#                 novo_email = input("Informe o email do cliente: ")
#                 novo_tel = int(input("Informe o telefone do cliente: "))
#                 novos_dados = (f"{novo_nome} - {novo_email} - {novo_tel}")
#                 dicio[dados_nome] = novos_dados

#         elif entrada_inicial == 3:
#             print(dicio)

#         elif entrada_inicial == 4:
#             acesso_chave = int(input("Informe o número do cliente: "))
#             acesso_cliente = dicio.get(acesso_chave)
#             return acesso_cliente    

#         elif entrada_inicial == 0:
#             return (dicio)
#         else:
#             print("Opção Inválida! Tente Novamente")    
        
    
# res = cadastro ()
# print(res)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 75
# Jogo de adivinhação
# Crie um programa que simule um jogo de adivinhação. O programa deve sortear um número inteiro entre 1 e 10 e pedir para o usuário tentar adivinhar o número sorteado. 
# Se o usuário acertar, o programa deve imprimir uma mensagem de parabéns e encerrar. 
# Caso contrário, o programa deve imprimir uma mensagem dizendo se o número é maior ou menor do que o sorteado e permitir que o usuário tente novamente. 
# O programa deve continuar permitindo que o usuário tente adivinhar o número até que ele acerte.


# import random

# def sortear_numero():
#     return random.randint(1, 10)

# def adivinhar_numero():
#     numero_sorteado = sortear_numero()
#     tentativas = 0

#     while True:
#         try:
#             tentativa_usuario = int(input("Tente advinhar o número entre 1 e 10: "))
#         except ValueError:
#             print("Por favor, informe um número inteiro!")
#             continue

#         if tentativa_usuario < 1 or tentativa_usuario > 10:
#             print("Por favor, informe um número entre 1 e 10!")
#             continue

#         tentativas += 1

#         if tentativa_usuario == numero_sorteado:
#             print(f"Parabéns, você acertou em {tentativas} tentativas!")
#             break
#         elif numero_sorteado > tentativa_usuario:
#             print("O número é maior!")
#         else:
#             print("O número é menor!")

# adivinhar_numero()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 76
# Agenda de contatos
# Crie um programa que permita o cadastro de contatos. Cada contato deve ter um nome e um telefone.
#  O programa deve permitir que o usuário cadastre novos contatos, consulte os contatos existentes e encerre o programa. 
# O programa deve armazenar os contatos em um dicionário e permitir que o usuário consulte um contato pelo nome.


# def agenda ():

#         dicio = {}
#         while True:
                 
#             entrada = int(input("Selecione: 1 - Para cadastro de contatos; 2 - Consulta de Contatos; 3 - Encerra o programa; "))
#             if entrada == 1:
#                 nome_contato = (input("Informe o nome do contato: "))
#                 tel_contato = int(input("Informe o tel do contato: "))
#                 dicio[nome_contato] = tel_contato

#             elif entrada == 2:
#                 nome_consulta = (input("Informe o nome do contato: "))
#                 verifica = dicio.get(nome_consulta)
#                 if verifica:
#                     print(f"O telefone do(a) {nome_consulta} é {verifica}")
#                 else:
#                     print(f"O contato {nome_consulta} não foi encontrado.")
            
#             elif entrada == 3:
#                 print("Encerrando o programa...........")
#                 break
            
#             else:
#                 print("Opção Invalída!")    
# res = agenda()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 77
# Contador de vogais
# Escreva um programa que solicita ao usuário uma frase e conte quantas vezes cada vogal aparece nessa frase. Armazene os resultados em um dicionário e imprima o dicionário.

# def vogalizador():
#     vogais = "aeiouAEIOU"
#     dicio = {v: 0 for v in vogais}
#     frase = input("Informe uma frase: ")
#     for letra in frase:
#         if letra in vogais:
#             dicio[letra] += 1
#     return dicio

# res = vogalizador()
# print(res)

########## Explicação Dicio ############

# Aqui, o dicionário é inicializado com todas as vogais em zero. 
# Em seguida, a frase é lida letra por letra, e a contagem é incrementada sempre que uma vogal é encontrada. 
# Finalmente, o dicionário é retornado com as contagens de cada vogal. 
# Note que o código foi simplificado e ficou mais eficiente, pois elimina os loops desnecessários e a sobreposição de valores.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 78
# Jogo de adivinhação
# Crie um programa que escolha aleatoriamente uma palavra de uma lista e solicite ao usuário que adivinhe qual é a palavra. 
# A cada tentativa do usuário, o programa deve informar quantas letras da palavra foram acertadas e quantas ainda faltam acertar. 
# O jogo deve terminar quando o usuário acertar a palavra ou atingir um número máximo de tentativas.

# import random

# def sorteador():
#     palavras = ['amor', 'vida', 'paz', 'lux', 'orgulho', "pônei"]
#     return random.choice(palavras)

# def advinhador():
#     palavra_sorteada = sorteador()
#     acertou = False
#     tentativas = 0
    
#     while not acertou:
#         entrada = input("Adivinhe a palavra sorteada: ")
        
#         if entrada == palavra_sorteada:
#             print("Parabéns, você acertou!")
#             acertou = True
#             break

#         elif entrada != palavra_sorteada:     
#             tentativas += 1
#             if tentativas > 3:
#                 return("Acabou as tentativas")

#             else:
#                 letras_certas = set(palavra_sorteada) & set(entrada)
#                 tam_restante = len(palavra_sorteada) - len(letras_certas)
#                 print(f"Foram acertadas {len(letras_certas)} letra(s). Restam {tam_restante} letra(s). Você usou {tentativas} de 3 tentativas ")
        

        
            
#     return "Fim do jogo!"
        
# res = advinhador()
# print(res)



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 79
# Tabuada interativa
# Crie um programa que solicite ao usuário um número e imprima a tabuada desse número de 1 a 10. 
# O usuário deve poder escolher se quer continuar vendo a tabuada de outros números ou se deseja sair do programa. 
# Utilize um dicionário para armazenar as tabuadas já calculadas e permita que o usuário possa consultar essas tabuadas novamente.



# def tabuadando ():
#     dicio = {}

#     while True: 

#         entrada_menu = int(input(" 1 - Para processar um novo número; 2 - Consultar Tabuadas;  0 - Para sair do programa: ")   ) 
#         tabu = []
#         if entrada_menu == 1:
#             entrada_num = int(input("Informe um numero: "))
#             for numero in range(1, 11):
#                 calulador = entrada_num * numero
#                 chave = (f"{entrada_num} x {numero} = {calulador}")
#                 print(chave)
#                 tabu.append(chave)
#                 dicio[entrada_num] =  tabu

#         elif entrada_menu == 2:
#             entrada_consulta = int(input(f"Informe o número a ser consultado: "))
#             consulta = dicio.get(entrada_consulta)
#             if consulta:
#                 print(f" Resultado da consulta do número {entrada_consulta} é: {consulta}")
#             else:
#                 print(f"O número {entrada_consulta} não foi encontrado.")
           

#         elif entrada_menu == 0:
#             return("Encerrando o programa")
#         else: 
#             print("Opção inválida")
        
# res = tabuadando ()


######## Versão Chatgpt ###########

# def tabuada_interativa():
#     dicio_tabuadas = {}

#     while True:
#         entrada_menu = input("1 - Processar um novo número\n2 - Consultar tabuadas\n0 - Sair do programa\n>>> ")
        
#         if entrada_menu == '1':
#             entrada_num = int(input("Informe um número: "))
#             tabuada = []
#             for i in range(1, 11):
#                 resultado = entrada_num * i
#                 tabuada.append(f"{entrada_num} x {i} = {resultado}")
#             dicio_tabuadas[entrada_num] = tabuada
            
#         elif entrada_menu == '2':
#             entrada_consulta = int(input("Informe o número da tabuada que deseja consultar: "))
#             if entrada_consulta in dicio_tabuadas:
#                 tabuada_consulta = dicio_tabuadas[entrada_consulta]
#                 print(f"Tabuada do {entrada_consulta}:")
#                 for tabuada in tabuada_consulta:
#                     print(tabuada)
#             else:
#                 print(f"Tabuada do número {entrada_consulta} não encontrada.")
                
#         elif entrada_menu == '0':
#             return "Encerrando o programa."
        
#         else:
#             print("Opção inválida, tente novamente.")

# tabuada_interativa()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 80
# Crie um programa que simule um jogo de dados. 
# O programa deve permitir que o usuário jogue os dados quantas vezes quiser e mostrar o resultado de cada jogada. 
# O programa deve encerrar quando o usuário não quiser mais jogar.

# import random

# def tem_dado ():
   

#     while True:
#         entrada_menu = int(input("1 - Para iniciar o jogo\n 0 - Sair do programa\n>>> "))

#         if entrada_menu == 1:         
#             dado_1 = random.randint(1, 6)
#             dado_2 = random.randint(1, 6)
#             print( f"O resultado do primeiro dado é: {dado_1}\n O resultado do primeiro dado é: {dado_2} ")
            
        
#         elif entrada_menu == 0:
#             print("Encerrando o programa.")
#             return 
        
#         else:
#             print("Opção inválida, tente novamente.")

# tem_dado ()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 81
# Crie um programa que simule uma calculadora básica. O programa deve permitir que o usuário escolha a operação que deseja realizar (adição, subtração, multiplicação ou divisão) e solicitar os dois números necessários para realizar a operação. O programa deve encerrar quando o usuário não quiser mais realizar operações.

# Exemplo 81
# Crie um programa que simule uma calculadora básica. 
# O programa deve permitir que o usuário escolha a operação que deseja realizar (adição, subtração, multiplicação ou divisão) e solicitar os dois números necessários para realizar a operação. 
# O programa deve encerrar quando o usuário não quiser mais realizar operações.

# ***** Adição de dificuldade: Permitir o calculo com multiplo valores

# def calculadora ():

#     while True: 
#         entrada_menu = int(input(" 1 - Para somar valores\n 2 - Para subtrair o valores\n 3 - Para multiplicar valores\n 4 - Para dividir valores\n 0 - Sair do programa\n>>> "))

#         if entrada_menu == 1:
#             contador_soma = int(input(" Informe quantos valores serão colocados:  "))
#             print("Informe um valor maior que 0 (zero) e um número inteiro ")
#             slots_soma = 0
#             lista_soma = []

#             while slots_soma < contador_soma:
#                 entrada_soma_1 = float(input(" Informe o(s) valor(es):  "))
#                 slots_soma += 1
#                 lista_soma.append(entrada_soma_1)
#                 soma = sum(lista_soma)
#             print(f" O resultado da soma é: {soma}")

#         elif entrada_menu == 2: 

#             contador_sub = int(input(" Informe quantos valores serão colocados:  "))
    
#             slots_sub = 0
#             lista__sub = []

#             while slots_sub < contador_sub:

#                 entrada_sub = float(input(" Informe o(s) valor(es):  "))

#                 slots_sub += 1
#                 lista__sub.append(entrada_sub)
            
#             # O for percorre a lista e vai subtraindo cada elemento do valor anterior
    
#                 sub = lista__sub[0]

#             # Sub é inicializada com o primeiro resultado da lista
#             # O range é inicializado com o número na posição número 1 e finalizado com o tamanho da lista 

#                 for i in range(1, len(lista__sub)):
            
#             # Assim o valor[0] será subtraido pelos valores seguintes
             
#                     sub -= lista__sub[i]

#             print(f" O resultado da subtração é: {sub}")
                
#         elif entrada_menu == 3:

#             contador_mult = int(input(" Informe quantos valores serão colocados:  "))
    
#             slots_mult = 0
#             lista__mult = []

#             while slots_mult < contador_mult:
#                 entrada_mult = float(input(" Informe o(s) valor(es):  "))
#                 slots_mult += 1
#                 lista__mult.append(entrada_mult)
            
    
#                 mult = lista__mult[0]
#                 for i in range(1, len(lista__mult)):
             
#                     mult *= lista__mult[i]

#             print(f" O resultado da multiplicação é: {mult}")
        

#         elif entrada_menu == 4:

#             contador_div = int(input(" Informe quantos valores serão colocados:  "))
    
#             slots_div = 0
#             lista__div = []

#             while slots_div < contador_div:
#                 entrada_div = float(input(" Informe o(s) valor(es):  "))
#                 slots_div += 1
#                 lista__div.append(entrada_div)
            
    
#                 div = lista__div[0]
#                 for i in range(1, len(lista__div)):
             
#                     div /= lista__div[i]

#             print(f" O resultado da divisão é: {div}")

# calculadora ()

#### Versão ChatGpt ####
# def calculadora():
#     while True:
#         entrada_menu = int(input("1 - Para somar valores\n2 - Para subtrair valores\n3 - Para multiplicar valores\n4 - Para dividir valores\n0 - Sair do programa\n>>> "))

#         if entrada_menu == 0:
#             break

#         try:
#             contador = int(input("Informe quantos valores serão colocados: "))
#             if contador <= 0:
#                 raise ValueError
#         except ValueError:
#             print("Por favor, informe um valor inteiro positivo maior que zero.")
#             continue

#         valores = []
#         for i in range(contador):
#             try:
#                 valor = float(input(f"Informe o {i+1}º valor: "))
#             except ValueError:
#                 print("Por favor, informe um valor numérico.")
#                 continue
#             valores.append(valor)

#         if entrada_menu == 1:
#             resultado = sum(valores)
#             print(f"O resultado da soma é: {resultado}")
#         elif entrada_menu == 2:
#             resultado = valores[0] - sum(valores[1:])
#             print(f"O resultado da subtração é: {resultado}")
#         elif entrada_menu == 3:
#             resultado = 1
#             for valor in valores:
#                 resultado *= valor
#             print(f"O resultado da multiplicação é: {resultado}")
#         elif entrada_menu == 4:
#             if 0 in valores[1:]:
#                 print("Não é possível dividir por zero.")
#                 continue
#             resultado = valores[0] / (valores[1:])
#             print(f"O resultado da divisão é: {resultado}")

# calculadora ()



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 82
# Escreva um programa que simule um jogo de cartas. O programa deve permitir ao usuário jogar uma partida de blackjack contra a máquina. O programa deve começar dando duas cartas para o usuário e duas cartas para a máquina. O usuário deve escolher entre pedir mais cartas ou parar. Depois disso, a máquina deve jogar e o programa deve determinar o vencedor. O programa deve permitir que o usuário jogue várias partidas e encerrar quando o usuário quiser sair.

# import random

# def jogar_blackjack():
#     # Inicializando baralho e definindo valores das cartas
#     baralho = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#     valores_cartas = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    
#     # Inicializando mãos do jogador e do dealer
#     mao_jogador = [random.choice(baralho), random.choice(baralho)]
#     mao_dealer = [random.choice(baralho), random.choice(baralho)]
    
#     # Função para calcular o valor de uma mão
#     def calcular_valor(mao):
#         valor = sum(valores_cartas[carta] for carta in mao)
#         if 'A' in mao and valor > 21:
#             valor -= 10
#         return valor
    
#     # Mostrando a mão do jogador e a carta do dealer
#     print("Sua mão:", mao_jogador)
#     print("Carta do dealer:", mao_dealer[0])
    
#     # Verificando se o jogador tem blackjack
#     if calcular_valor(mao_jogador) == 21:
#         print("Você tem blackjack!")
#         return
    
#     # Pedindo cartas para o jogador
#     while True:
#         resposta = input("Quer mais uma carta? (s/n) ")
#         if resposta.lower() == 's':
#             nova_carta = random.choice(baralho)
#             mao_jogador.append(nova_carta)
#             print("Sua mão:", mao_jogador)
#             if calcular_valor(mao_jogador) > 21:
#                 print("Você estourou!")
#                 return
#         else:
#             break
    
#     # Jogada do dealer
#     while calcular_valor(mao_dealer) < 17:
#         nova_carta = random.choice(baralho)
#         mao_dealer.append(nova_carta)
    
#     # Mostrando mãos do jogador e do dealer
#     print("Sua mão:", mao_jogador)
#     print("Mão do dealer:", mao_dealer)
    
#     # Verificando resultados
#     valor_jogador = calcular_valor(mao_jogador)
#     valor_dealer = calcular_valor(mao_dealer)
#     if valor_jogador > 21:
#         print("Você perdeu!")
#     elif valor_dealer > 21:
#         print("Você ganhou!")
#     elif valor_jogador > valor_dealer:
#         print("Você ganhou!")
#     elif valor_jogador < valor_dealer:
#         print("Você perdeu!")
#     else:
#         print("Empate!")

# jogar_blackjack()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 83
# Crie um programa que peça ao usuário uma senha e verifique se ela é forte o suficiente. 
# Uma senha forte deve ter pelo menos 8 caracteres, incluindo pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.


# def verificador():
#     while True:
#         entrada_usuario = input("Informe uma senha: ")
#         tamanho = len(entrada_usuario) >= 8
#         special = any(caractere in entrada_usuario for caractere in "!@#$%&*")
#         alpha = any(caractere.isalpha() for caractere in entrada_usuario)
#         maiuscula = any(caractere.isupper() for caractere in entrada_usuario)
#         minuscula = any(caractere.islower() for caractere in entrada_usuario)
#         if tamanho and special and alpha and maiuscula and minuscula:
#             print ("Senha Forte")
#         else:
#             print ("Senha Fraca")

# verificador()


# Verificar a presença de um elemento em uma string

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 84
# Escreva um programa que calcule o fatorial de um número digitado pelo usuário. Use uma função do módulo math para fazer o cálculo.
# Fatorial


# import math

# def fatorial():

#     while True: 
#         entrada = int(input("Informe um número: "))

#         calculo = math.factorial(entrada)

#         print(calculo)

#         break


# fatorial()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 85
# Escreva um programa que pergunte ao usuário quantos números ele quer gerar e, em seguida, gere essa quantidade de números aleatórios entre 1 e 100. Armazene os números em um dicionário e imprima o dicionário.

# Na minha versão foram gerados multiplos dicionários

# import random 

# def numero_aleatorios():

#     contador = 0
#     entrada_numeros = int(input("Informe um número: "))
#     dicio = {}


#     while contador < entrada_numeros: 

#         aleatorios = random.randint(1, 100)
#         numeros = {}
#         numeros[f"Número de entrada {entrada_numeros}"] = aleatorios 
#         print(numeros)
#         contador += 1
#     return


       
# numero_aleatorios()

######### Versão ChatGpt #########

# Todos os números gerados permaneceram em apenas 1 dicionário.

# import random

# def gerar_numeros():
#     quantidade = int(input("Quantos números deseja gerar? "))
#     numeros = {}
#     for i in range(quantidade):
#         numeros[f"n{i+1}"] = random.randint(1, 100)
#     return numeros

# print(gerar_numeros())

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 86
# Crie um programa que calcule o valor de π utilizando o método de Monte Carlo. 
# O programa deve gerar aleatoriamente pontos em um quadrado de lado 1 e, em seguida, calcular quantos desses pontos estão dentro de um círculo de raio 1/2. 
# O valor de π é dado por 4 vezes a razão entre o número de pontos dentro do círculo e o número total de pontos gerados.

# import random

# def monte_carlo_pi(num_pontos):
#     dentro_circulo = 0
    
#     for i in range(num_pontos):
#         # Gerar ponto aleatório no quadrado de lado 1
#         x = random.uniform(0, 1)
#         y = random.uniform(0, 1)
        
#         # Calcular distância do ponto ao centro do círculo
#         distancia = (x-0.5)**2 + (y-0.5)**2
        
#         # Verificar se o ponto está dentro do círculo
#         if distancia <= 0.25:
#             dentro_circulo += 1
    
#     # Calcular valor de pi
#     pi = 4 * dentro_circulo / num_pontos
    
#     return pi

# # Exemplo de uso
# pi = monte_carlo_pi(1000000)
# print(pi)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Exemplo 87
# # Crie um programa que simule uma corrida de carros. O programa deve perguntar ao usuário quantos carros participarão da corrida e, em seguida, gerar aleatoriamente uma posição de largada para cada carro. 
# # A cada rodada, o programa deve atualizar a posição de cada carro de acordo com uma velocidade aleatória e imprimir a posição de cada carro.

# import random

# # Pergunta quantos carros participarão da corrida
# num_carros = int(input("Quantos carros participarão da corrida? "))

# # Gera aleatoriamente a posição de largada para cada carro
# posicoes = {}
# for i in range(num_carros):
#     posicoes[f"Carro {i+1}"] = random.randint(1, 10)

# # Define a distância total da corrida
# distancia_total = 100

# # Define a velocidade mínima e máxima de cada carro
# velocidade_minima = 1
# velocidade_maxima = 10

# # Define a duração de cada rodada da corrida
# duracao_rodada = 1

# # Inicia a corrida
# distancia_percorrida = {k: 0 for k in posicoes.keys()}
# rodada = 1
# while True:
#     print(f"Rodada {rodada}")
#     for carro, posicao in posicoes.items():
#         # Calcula a velocidade aleatória do carro
#         velocidade = random.randint(velocidade_minima, velocidade_maxima)
#         # Calcula a distância percorrida pelo carro nesta rodada
#         distancia_percorrida[carro] += velocidade * duracao_rodada
#         # Verifica se o carro chegou ao fim da corrida
#         if distancia_percorrida[carro] >= distancia_total:
#             print(f"{carro} chegou ao fim da corrida!")
#             # Remove o carro da lista de posições
#             del posicoes[carro]
#         else:
#             # Atualiza a posição do carro
#             nova_posicao = posicao + int(distancia_percorrida[carro] / distancia_total * 10)
#             posicoes[carro] = nova_posicao
#             print(f"{carro} está na posição {nova_posicao}")
#     # Verifica se a corrida terminou
#     if not posicoes:
#         print("Todos os carros chegaram ao fim da corrida!")
#         break
#     rodada += 1
    

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 88
# Crie um programa que solicite ao usuário uma data de nascimento (dia, mês e ano) e calcule a idade em anos, meses e dias. Utilize o módulo datetime para manipular as datas.

# import datetime

# dia = int(input("Informe o dia: "))
# mes = int(input("Informe o mês: "))
# ano = int(input("Informe o ano: "))



# data_nascimento = datetime.date(ano, mes, dia)

# data_hoje = datetime.date.today()

# idade_ano = data_hoje.year - data_nascimento.year

# idade_dias = (data_hoje - data_nascimento).days

# idade_meses = round(idade_dias/30.44) 


# print( f" Você tem: {idade_ano} anos" )
# print( f" Passaram {idade_meses} meses desde que vc nasceu" )
# print( f" Passaram {idade_dias} dias desde que vc nasceu" )


# Calculo da Idade

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 89
# Crie um programa que calcule o tempo gasto por uma pessoa para percorrer uma certa distância a uma certa velocidade. 
# Solicite a distância em quilômetros e a velocidade média em km/h. Utilize o módulo datetime para calcular o tempo gasto em horas, minutos e segundos.

#################### Sem Datetime ####################

# def velocimetro(): 

#     distancia = float(input("Informe a distância em km: "))
#     velocidade = float(input("Informe a velocidade média em km/h: "))

#     tempo_gasto = distancia/velocidade

#     print(f"{tempo_gasto} horas")
#     print(f"{tempo_gasto*60} minutos")
#     print(f"{tempo_gasto*3600} segundos")

#     return


# velocimetro()


################### Com Datetime ####################

# import datetime

# def velocimetro_2(): 

#     distancia = float(input("Informe a distância em km: "))
#     velocidade = float(input("Informe a velocidade média em km/h: "))

#     tempo_gasto = distancia/velocidade

#     # Calcula o tempo gasto em horas, minutos e segundos
#     tempo_gasto_horas = int(tempo_gasto)
#     tempo_gasto_minutos = int((tempo_gasto - tempo_gasto_horas) * 60)
#     tempo_gasto_segundos = int(((tempo_gasto - tempo_gasto_horas) * 60 - tempo_gasto_minutos) * 60)

#     # Cria um objeto timedelta com o tempo gasto em segundos
#     tempo_gasto_timedelta = datetime.timedelta(seconds=tempo_gasto_segundos, minutes=tempo_gasto_minutos, hours=tempo_gasto_horas)

#     print(f"Tempo gasto: {tempo_gasto_timedelta}")

#     return

# velocimetro_2()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 90
# Crie um programa que exiba a hora atual do sistema em um loop infinito. Utilize o módulo time para pausar o programa por 1 segundo a cada iteração do loop.


# import datetime
# import time

# def loop_hora():


#     while True:
#         hora_atual = datetime.datetime.now().time() 
#         hora_atual_formatada = hora_atual.strftime("%H:%M:%S")

#         print(hora_atual_formatada)

#         time.sleep(1)

# loop_hora()

# Apenas Horas Minutos e Segundos
# Arredondar

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 91
# Crie um programa que solicite ao usuário o tempo de duração de um evento em segundos e exiba o tempo em formato hh:mm:ss. Utilize o módulo datetime para manipular o tempo.

# import datetime

# def duracao():

#     segundos = int(input("Informe a duração do evento em segundos: "))

#     # Criando um objeto timedelta a partir do número de segundos
#     duracao = datetime.timedelta(seconds=segundos)

#     # Extraindo as informações de horas, minutos e segundos do objeto timedelta
#     horas, resto = divmod(duracao.seconds, 3600)
#     minutos, segundos = divmod(resto, 60)

#     # Imprimindo a duração em formato hh:mm:ss
#     print(f"Duração: {horas:02d}:{minutos:02d}:{segundos:02d}")

# duracao()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##### divimod ######

# divmod é uma função embutida do Python que retorna o quociente e o resto da divisão de dois números.
# Ela recebe dois argumentos, o dividendo e o divisor, e retorna uma tupla com o quociente e o resto, nessa ordem.

# Por exemplo, divmod(10, 3) retorna (3, 1), indicando que 10 dividido por 3 é igual a 3, com resto 1. 
# É possível usar divmod para realizar a divisão de inteiros de forma mais eficiente do que usando o operador /, 
# pois divmod realiza a divisão e a obtenção do resto em uma única operação.


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 92
# Crie um programa que solicite ao usuário uma data de início e uma data de fim e calcule a diferença de tempo entre elas em dias, horas, minutos e segundos. 
# Utilize o módulo datetime para manipular as datas.


# import datetime

# def calcular_diferenca_tempo():

#     # Solicita as datas de início e fim ao usuário
#     while True:
#         data_inicio_str = input("Digite a data de início (dd/mm/aaaa hh:mm:ss): ")
#         try:
#             data_inicio = datetime.datetime.strptime(data_inicio_str, "%d/%m/%Y %H:%M:%S")
#         except ValueError:
#             print("Formato de data inválido. Digite no formato dd/mm/aaaa hh:mm:ss.")
#             continue

#         data_fim_str = input("Digite a data de fim (dd/mm/aaaa hh:mm:ss): ")
#         try:
#             data_fim = datetime.datetime.strptime(data_fim_str, "%d/%m/%Y %H:%M:%S")
#         except ValueError:
#             print("Formato de data inválido. Digite no formato dd/mm/aaaa hh:mm:ss.")
#             continue

#         if data_fim < data_inicio:
#             print("A data de fim deve ser posterior à data de início.")
#             continue

#         break

#     # Calcula a diferença entre as datas
#     delta = data_fim - data_inicio

#     dias = delta.days
#     segundos = delta.seconds

#     horas, segundos = divmod(segundos, 3600)
#     minutos, segundos = divmod(segundos, 60)

#     # Imprime o resultado
#     print(f"A diferença entre as datas é de {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")


# calcular_diferenca_tempo()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 93
# Crie um programa que exiba um relógio analógico em tempo real na tela. Utilize o módulo import tkinter para desenhar o relógio e o módulo time para atualizar a hora a cada segundo.

#### Versão ChatGpt #######

# import tkinter as tk
# import time
# import math

# class Clock:
#     def __init__(self, master):
#         self.master = master
#         self.canvas = tk.Canvas(master, width=300, height=300)
#         self.canvas.pack()
#         self.draw_clock()

#     def draw_clock(self):
#         # Draw the clock face
#         self.canvas.create_oval(50, 50, 250, 250, width=2)

#         # Draw the hour markings
#         for i in range(1, 13):
#             x = 150 + 100 * math.cos(math.pi/6 * i)
#             y = 150 - 100 * math.sin(math.pi/6 * i)
#             self.canvas.create_text(x, y, text=str(i), font=('Arial', 12))

#         # Draw the minute markings
#         for i in range(0, 60, 5):
#             x = 150 + 120 * math.cos(math.pi/30 * i)
#             y = 150 - 120 * math.sin(math.pi/30 * i)
#             self.canvas.create_text(x, y, text='.', font=('Arial', 8))

#         # Draw the hour hand
#         self.hour_hand = self.canvas.create_line(150, 150, 150, 100, width=4)

#         # Draw the minute hand
#         self.minute_hand = self.canvas.create_line(150, 150, 150, 50, width=3)

#         # Draw the second hand
#         self.second_hand = self.canvas.create_line(150, 150, 150, 50, width=1, fill='red')

#     def update_clock(self):
#         current_time = time.localtime()
#         hour = current_time.tm_hour % 12
#         minute = current_time.tm_min
#         second = current_time.tm_sec

#         # Calculate the angles of the hands
#         hour_angle = math.pi/6 * hour + math.pi/360 * minute
#         minute_angle = math.pi/30 * minute
#         second_angle = math.pi/30 * second

#         # Rotate the hands to the correct angles
#         self.canvas.coords(self.hour_hand, 150, 150, 150 + 60 * math.sin(hour_angle), 150 - 60 * math.cos(hour_angle))
#         self.canvas.coords(self.minute_hand, 150, 150, 150 + 80 * math.sin(minute_angle), 150 - 80 * math.cos(minute_angle))
#         self.canvas.coords(self.second_hand, 150, 150, 150 + 80 * math.sin(second_angle), 150 - 80 * math.cos(second_angle))

#         # Update the clock every second
#         self.master.after(1000, self.update_clock)

# root = tk.Tk()
# root.title('Relógio Analógico')
# clock = Clock(root)
# clock.update_clock()
# root.mainloop()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 94
# Crie um programa que exiba um cronômetro na tela. O programa deve permitir que o usuário inicie, pare e reinicie o cronômetro. Utilize o módulo time para gerenciar o tempo.

# import time

# tempo = 0
# rodando = False

# while True:
#     # Exibe o tempo atual na tela
#     print(f"Tempo: {tempo}s")

#     # Espera um segundo
#     time.sleep(1)

#     # Incrementa o tempo se o cronômetro estiver rodando
#     if rodando:
#         tempo += 1

#     # Recebe um comando do usuário
#     comando = input("Digite 'i' para iniciar, 'p' para parar, 'r' para reiniciar, tecle qualquer digito para sair do cronmetro: ")

#     # Executa o comando correspondente
#     if comando == "i":
#         rodando = True
#     elif comando == "p":
#         rodando = False
#     elif comando == "r":
#         tempo = 0
#         rodando = False
#     else:
#         break

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 95
# Crie um programa que solicite ao usuário um horário de início e um tempo de duração e calcule o horário de término. 
# O horário deve ser exibido em formato hh:mm:ss. 
# Utilize o módulo datetime para manipular o tempo.



# import datetime 


# def horador():

#     while True:

#         hora_inicio = input("Digite a hora de início (hh:mm:ss): ")

#         try:
#             hora_inicio = datetime.datetime.strptime(hora_inicio, "%H:%M:%S").time()
#         except ValueError:
#             print("Formato de horá inválida. Digite no formato hh:mm:ss.")
#             continue


#         tempo_duracao = input("digite o tempo de duração (hh:mm:ss): ")

#         try:
#             tempo_duracao = datetime.datetime.strptime(tempo_duracao, "%H:%M:%S").time()
#         except ValueError:
#             print("Formato de horá inválida. Digite no formato hh:mm:ss.")
#             continue
#         break
    
    
#     data_inicio = datetime.datetime.combine(datetime.date.today(), hora_inicio)
#     delta = datetime.timedelta(hours=tempo_duracao.hour, minutes=tempo_duracao.minute, seconds=tempo_duracao.second)
#     data_fim = data_inicio + delta    
    
#     print(f"Horário de término: {data_fim.strftime('%H:%M:%S')}")
#     return



# horador()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 96
# Crie um programa que exiba a hora atual do sistema em diferentes fusos horários. 
# O programa deve solicitar ao usuário o fuso horário desejado e exibir a hora atual nesse fuso. 
# Utilize o módulo pytz para manipular os fusos horários.

# import pytz

# import datetime

# # Lista de fusos horários disponíveis
# timezones = pytz.all_timezones

# # Obtém a hora atual do sistema
# hora_atual = datetime.datetime.now()

# while True:
#     # Solicita o fuso horário desejado
#     entrada_fuso = input("Informe o fuso horário que deseja consultar(ex: America/Sao_Paulo): ")

#     # Verifica se o fuso horário informado está na lista de fusos horários disponíveis
#     if entrada_fuso in timezones:
#         # Converte a hora atual para o fuso horário desejado
#         fuso_horario = pytz.timezone(entrada_fuso)
#         hora_fuso_horario = hora_atual.astimezone(fuso_horario)

#         # Exibe a hora atual no fuso horário desejado
#         print("Hora atual no fuso horário {}: {}".format(entrada_fuso, hora_fuso_horario.strftime("%d/%m/%Y %H:%M:%S")))
#         break
#     else:
#         print("Fuso horário inválido. Informe um fuso horário da lista.")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 97
# Crie um programa que exiba a hora e a data atual do sistema em diferentes formatos. 
# O programa deve permitir que o usuário escolha o formato desejado. 
# Utilize o módulo datetime para manipular a data e a hora.


# import datetime 

# def formato_datetime():

#     while True: 

#         entrada_menu = int(input("1 - Ano com quatro dígitos\n2 - Ano com dois dígitos\n3 - Formato AM ou PM \n0 - Sair do programa\n>>> "))

#         if entrada_menu == 1: 

#             dt = datetime.datetime.now()
#             dt_str = dt.strftime("%d/%m/%Y %H:%M:%S")
#             print(dt_str)

#         elif entrada_menu == 2: 

#             dt = datetime.datetime.now()
#             dt_str = dt.strftime("%d/%m/%y %H:%M:%S")
#             print(dt_str)

#         elif entrada_menu == 3: 

#             dt = datetime.datetime.now()
#             dt_str = dt.strftime("%d/%m/%y %H:%M:%S:%I:%p")
#             print(dt_str)

#         elif entrada_menu == 0: 

#             print("Obrigado por usar o meu programa")
#             break
#         else:
#             print("Valor inválido tente novamente!")

# formato_datetime()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 98
# Crie um programa que solicite um número inteiro ao usuário e exiba sua raiz quadrada. 
# Certifique-se de que o programa não falhe se o usuário inserir um número negativo.


# import math

# def raizando():

#     while True: 
        
#         entrada_num = int(input("Informe um número inteiro: "))

#         try:
#             raiz_quadrada = math.sqrt(entrada_num)
#         except ValueError:
#             print("O valor informado é inválido tente novamente.")
#             continue



#         print(raiz_quadrada)
#         return

# raizando()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 99
# Escreva um programa que solicite ao usuário um número inteiro e, em seguida, divida o número 100 por esse número. 
# Certifique-se de que o programa não falhe se o usuário inserir 0 como entrada.


# def centenando():

#     while True: 

#         entrada_num = int(input("Informe um número inteiro (maior que 0): "))

#         try:
#             dividendo = 100/entrada_num
#         except ZeroDivisionError:
#             print("Número inválido!")
#             continue
        
#         print(dividendo)
#         return

# centenando()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 100
# Crie uma calculadora que permita somar, subtrair, multiplicar e dividir números. 
# Certifique-se de que o programa não falhe se o usuário inserir uma entrada inválida, como uma letra em vez de um número.


# def calculadora ():

#     while True: 

#         try:
#             entrada_menu = int(input(" 1 - Para somar valores\n 2 - Para subtrair o valores\n 3 - Para multiplicar valores\n 4 - Para dividir valores\n 0 - Sair do programa\n>>> "))
#         except ValueError:
#             print("Informe um número válido!")
#             continue

#         if entrada_menu == 1:
            
#             try: 
#                 contador_soma = int(input(" Informe quantos valores serão colocados:  "))
            
#                 slots_soma = 0
#                 lista_soma = []

#             except UnboundLocalError and ValueError: 
#                 print("Informe um número inteiro maior que 0 (zero) ")
#                 continue
            
#             try:
#                 while slots_soma < contador_soma:
#                     entrada_soma_1 = float(input(" Informe o(s) valor(es):  "))
#                     slots_soma += 1
#                     lista_soma.append(entrada_soma_1)
#             except ValueError and UnboundLocalError   :
#                 print("Informe um valor numérico")
#                 continue            


#             soma = sum(lista_soma)
#             print(f" O resultado da soma é: {soma}")



#         elif entrada_menu == 2: 

#             contador_sub = int(input(" Informe quantos valores serão colocados:  "))
    
#             slots_sub = 0
#             lista__sub = []

#             while slots_sub < contador_sub:

#                 entrada_sub = float(input(" Informe o(s) valor(es):  "))

#                 slots_sub += 1
#                 lista__sub.append(entrada_sub)
            
#             # O for percorre a lista e vai subtraindo cada elemento do valor anterior
    
#                 sub = lista__sub[0]

#             # Sub é inicializada com o primeiro resultado da lista
#             # O range é inicializado com o número na posição número 1 e finalizado com o tamanho da lista 

#                 for i in range(1, len(lista__sub)):
            
#             # Assim o valor[0] será subtraido pelos valores seguintes
             
#                     sub -= lista__sub[i]

#             print(f" O resultado da subtração é: {sub}")
                
#         elif entrada_menu == 3:

#             contador_mult = int(input(" Informe quantos valores serão colocados:  "))
    
#             slots_mult = 0
#             lista__mult = []

#             while slots_mult < contador_mult:
#                 entrada_mult = float(input(" Informe o(s) valor(es):  "))
#                 slots_mult += 1
#                 lista__mult.append(entrada_mult)
            
    
#                 mult = lista__mult[0]
#                 for i in range(1, len(lista__mult)):
             
#                     mult *= lista__mult[i]

#             print(f" O resultado da multiplicação é: {mult}")
        
#         elif entrada_menu == 4:
#             contador_div = int(input("Informe quantos valores serão colocados: "))
#             slots_div = 0
#             lista__div = []

#             while slots_div < contador_div:
#                 entrada_div = float(input("Informe o(s) valor(es): "))
#                 slots_div += 1
#                 lista__div.append(entrada_div)

#             try:
#                 div = lista__div[0]
#                 for i in range(1, len(lista__div)):
#                     div/= lista__div[i]
#                 print(f"O resultado da divisão é: {div}")
#             except ZeroDivisionError:
#                 print("O valor não pode ser dividido por zero!")
#                 continue

# calculadora ()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 101
# Escreva um programa que solicite ao usuário um arquivo e tente abri-lo. Se o arquivo não existir, exiba uma mensagem de erro ao usuário.


# def explorer():
    
    
#     while True:
        
#         lista_arquivo = ["arquivo.txt", "batata.txt", "bunda"]

#         entrada = input(str("Informe um arquivo: "))
        
#         if entrada in lista_arquivo:
#                 print("O arquivo existe")
#         elif entrada is not lista_arquivo:
#                 print("Arquivo não existe")
#         return
# explorer()

############ Versão ChatGPT ############## 

# def explorer():
#     while True:
#         nome_arquivo = input("Informe o nome do arquivo: ")
#         try:
#             arquivo = open(nome_arquivo, 'r')  # Abre o arquivo para leitura
#             arquivo.close() # Fecha o arquivo após a leitura
#             print("O arquivo existe.")
#         except FileNotFoundError:
#             print("O arquivo não existe. Verifique o nome e o caminho do arquivo.")
#         return

# explorer()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
######## Explicando open(), close() e read() #############################

# open(): é usada para abrir um arquivo no modo especificado e retorna um objeto de arquivo que pode ser usado para ler, gravar e manipular o arquivo. 
# Ela possui a seguinte sintaxe:
# open(nome_do_arquivo, modo)

# close(): Após abrir o arquivo usando open(), é importante fechá-lo quando você terminar de trabalhar com ele. (boa pratica) 
# Isso é feito chamando o método close() no objeto do arquivo. A função close() fecha o arquivo e libera os recursos do sistema associados a ele.

# read(): Com está função é possivel ler o arquivo aberto. Ela retorna uma string contendo todo o conteúdo do arquivo. 
# A função read() pode ser chamada sem argumentos ou com um argumento opcional que especifica o número máximo de caracteres a serem lidos. 
# Se nenhum argumento for fornecido, a função read() lerá todo o conteúdo do arquivo.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo 102
# Crie um programa que solicite ao usuário um número inteiro e, em seguida, tente converter a entrada em uma string. Se isso não for possível, exiba uma mensagem de erro.


# def coversor():
        
#         try: 

#             entrada = int(input("Informe um número inteiro: "))
#             stringer = f"{entrada}"
#             print(stringer)
#         except ValueError:

#             print("Valor inválido! Informe um número inteiro!")
#         return
    
# coversor()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exemplo 103

# Sistema bancário 2.0: Foi inserio a entrada do nome do cliente ao dicionário onde é armazenado os dados do cliente 
# Dicionário recebendo dois valores

# def banco_dan ():
#     dicio = {}
#     lista = dicio
    

#     while True:
#         entrada = int (input ( " 1 - Adicionar uma nova conta com saldo inicial; 2 - Fazer um depósito em uma conta existente; 3 -Fazer um saque de uma conta existent; 4 - Ver o saldo de uma conta existente; 5 - Sair do programa:  " ))
        
#         if  entrada == 1:
#             numero_conta = int(input("Informe o Nº da Conta: "))
#             nome_cliente = input("Infome o nome do cliente: ")
#             saldo_inicial = int(input("Informe o valor do deposito do saldo inicial: "))
#             dicio[numero_conta] = {'saldo': saldo_inicial, 'cliente': nome_cliente}
#             print (f"Foi depositado na conta do cliente: {nome_cliente}, número da conta: {numero_conta} o valor de R$ {saldo_inicial},00   ////////// Operação Encerrada /////////// Retornando ao menu inicial ///////////") 
#         elif entrada == 2:

#             selecionar_conta =  int(input("Informe o número da conta que deseja realizar o deposito: "))
#             deposito_valor = int(input("Informe o valor que deseja depositar: "))
#             dicio[selecionar_conta]['saldo'] += deposito_valor
#             print(f"Foi depositado na conta do cliente: {dicio[selecionar_conta]['cliente']} número da conta {selecionar_conta}, o valor de {deposito_valor},00   ////////// Operação Encerrada /////////// Retornando ao menu inicial ///////////")

#         elif entrada == 3:
#             conta_saque =  int(input("Informe o número da conta que deseja realizar o saque: "))
#             valor_saque = int(input("Informe o valor que deseja sacar: "))
#             if valor_saque >  dicio.get(conta_saque):
#                 print("Saldo Insuficiente!")
#             else:
#                  dicio[conta_saque] = dicio.get(conta_saque) - valor_saque
#                  saldo = dicio.get(conta_saque) 
#                  print(f"A conta {conta_saque}, foi realizado o saque de {valor_saque},00, saldo atual {saldo}  ////////// Operação Encerrada /////////// Retornando ao menu inicial ///////////")
        
#         elif entrada == 4:
#             conta_saldo = int(input("Informe o número da conta que deseja verificar o saldo: "))
#             saldo_conta = dicio.get(conta_saldo)
#             print (f"O saldo da conta {conta_saldo} é de R$ {saldo_conta},00 ")
        
#         elif entrada == 5:
#             print("Obrigado por ser nosso cliente! Volte Sempre!!")  
#             break
        
#         else:
#             print("Valor inválido, selecione um outro número!") 
            

# banco_dan ()



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    


