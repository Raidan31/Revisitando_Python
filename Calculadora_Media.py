# Calculadora de média: Crie um programa que recebe uma lista de números e calcula a média dos valores.

def calc_media (lista):
        lista_final = []
        lista_numeros = (sum(lista)) / (len(lista))
        lista_final.append(lista_numeros)
        return  lista_final


numeros = input("Informe os números separados por vírgula: ")
lista = [float(num) for num in numeros.split(",")]
resposta = (calc_media(lista))
media_formatada = round(resposta[0], 2)
print(f"A média dos números informados é: {media_formatada:.2f}")
