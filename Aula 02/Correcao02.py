n1 = float(input("Informe um valor númerico: "))
n2 = float(input("Informe outro valor númerico: "))

print("Seleciona a operação desejada: ")
opcao = int(input("1- Adição 2- Subtração 3- Multiplicação 4- Divisão :   "))


match opcao :
    case 1 :
            print(n1 + n2)
    case 2 :
            print(n1 - n2)
    case 3 :
            print(n1 * n2)
    case 4 :
        if (n2 == 0):
            print("Zero não divide")
        else:
            print(n1 / n2)
    case _:
        print("Opção Inválida")