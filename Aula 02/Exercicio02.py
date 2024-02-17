num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")


soma = (num1 + num2)

subtracao = (num1 - num2)

multiplicacao = (num1 * num2)

divisao = (num1 / num2)

opcao = input("Digite algumas das opções > ")

if opcao == '1':
    resultado = num1 + num2
    print("Resultado da soma:", resultado)

elif opcao == '2':
    resultado = num1 - num2
    print("Resultado da subtração:", resultado)

elif opcao == '3':
    resultado = num1 * num2
    print("Resultado da multiplicação:", resultado)

elif opcao == '4':
    if num2 != 0: 
        resultado = num1 / num2
        print("Resultado da divisão:", resultado)

    else:
        print("Zero não divide")

else:
    print("Volte a escola")





n1 = float(input("Informe "))





