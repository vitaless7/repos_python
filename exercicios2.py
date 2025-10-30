# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
resultado_soma = num1 + num2
print("A soma é:", resultado_soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

num = int(input("Digite um número: "))
resultado_resto = num % 5
print("O resto da divisão por 5 é:", resultado_resto)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado_multiplicacao = num1 * num2
print("O resultado da multiplicação é:", resultado_multiplicacao)
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
resultado_divisao_inteira = num1 // num2
print("O resultado da divisão inteira é:", resultado_divisao_inteira)
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

num = int(input("Digite um número: "))
resultado_quadrado = num ** 2
print("O quadrado do número é:", resultado_quadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

num1 = float(input("Digite um número flutuante: "))
num2 = float(input("Digite o segundo número flutuante: "))
resultado_soma = num1 + num2
print("A soma é:", resultado_soma)
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

num1 = float(input("Digite o primeiro número flutuante: "))
num2 = float(input("Digite o segundo número flutuante: "))
media = (num1 + num2) / 2
print("A média é:", media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
potencia = base ** expoente
print("O resultado da potência é:", potencia)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celcius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celcius}ºC é igual a {fahrenheit}ºF")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio do círculo: "))
area = 3.14159 * raio ** 2
print("A área do círculo é:", area)


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = input("Digite um texto: ")
texto_maiusculas = texto.upper()
print(f"Texto em maiuscula é: {texto_maiusculas}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = input("Digite seu nome completo: ")
nome_minusculas = nome_completo.lower()
print("Nome em minúsculas:", nome_minusculas)
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
frase_sem_espacos = frase.strip()
print("Frase sem espaços no início e no final:", frase_sem_espacos)
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

parte1 = input("Digite a primeira parte do texto: ")
parte2 = input("Digite a segunda parte do texto: ")
texto_concatenado = parte1 + parte2
print("Texto concatenado:", texto_concatenado)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor1 = True
valor2 = False
resultado_and = valor1 or valor2
print("Resultado do AND lógico:", resultado_and)
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor1 = False
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

num1 = 5
num2 = 5
resultado_igualdade = (num1 != num2)
print("Resultado da igualdade:", resultado_igualdade)

# #### try-except e if

# 21: Conversor de Temperatura
try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F.")
except ValueError:
    print("Por favor, digite um número válido para a temperatura.")
# 22: Verificador de Palíndromo
entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")
# 23: Calculadora Simples
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero")
        resultado = None  # evita erro se resultado não for definido

    if resultado is not None:
        print(f"Resultado: {resultado}")

except ValueError:
    print("Entrada inválida! Você não inseriu os números corretamente.")

# 24: Classificador de Números
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido!!!")

