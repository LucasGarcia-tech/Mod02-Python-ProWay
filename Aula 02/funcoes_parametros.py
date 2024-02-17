# print("Olá Mundo")

def dados(nome,sobrenome,apelido,qtde_filhos =0,email =""):
    print(nome)
    print(apelido)
    print(sobrenome)
    print(qtde_filhos)
    if(email != ""):
        print(email)
        return
    print('E-mail não informado')
        


def msg():
    print('Olá Mundo')

def proway():
    print('Proway')

def parametro(valor = any):
    print(valor)


def argumentos(p1,p2,p3):
    print(p1)
    print(p2)
    print(p3)


dados("Lucas","Garcia","Luquinhas",5,"lucas@lucas.com")



# parametro(2)
# parametro("Proway")
# parametro(10 + 10)

# proway()
# msg()

#Com valor padrão nao pode ter valor obrigatorio depois dele
    
