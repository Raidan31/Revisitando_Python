# Conversor de temperatura: Crie um programa que converte temperaturas de Fahrenheit para Celsius e vice-versa.

def conversor_temperatura (temperatura_Fahrenheit):
    valor_Final = (temperatura_Fahrenheit - 32) / 1.8
    return valor_Final



temperatura_Fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
resposta = round (conversor_temperatura (temperatura_Fahrenheit), 2)
print(f"O valor convertido para Celsius será de {resposta} C ")