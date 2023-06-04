# Verificador de palíndromo: Crie uma função que verifica se uma string é um palíndromo 
# (ou seja, se pode ser lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda).

def verificador (string):
    if string == string[::-1]:
        return "É palindromo"
    else: 
        return "Não é palindromo"
    return



string = str(input("Informe a palavra a ser verificada: "))
resposta = verificador (string)
print(f"A palavra informada: {resposta}")
