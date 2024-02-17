class Veiculo:
    cor = 'Vermelho'
    ligado = False

    #Métodos

    def __init__(self,pCor):
        self.cor = pCor
        self.ligado = False
        #self.portas = 4
    

    def ligar(self):
        if(self.ligado):
            print("O carro já está ligado")
            return
        self.ligado = True
        print("O carro foi ligado")
    
    def desligar(self):
        if(not(self.ligado)):
            print("O carro já está desligado")
            return

        self.ligado = False
        print("O carro foi desligado")

class Carro(Veiculo):
    def marchaRe(self):
        print("Engatou a marcha ré")

class Moto(Veiculo):
    def pezinho(self):
        print("Botou o pezinho no chão")


gol = Carro("Amarelo")
print(gol.ligado)
gol.marchaRe()

cg = Moto("Preta")
print(cg.ligado)
cg.pezinho()






#Instanciar um objeto > Criar o objeto propriamente dito
    
# carro = Veiculo()
# print(carro.cor)
# print(carro.ligado)

# carro.ligar()
# print(carro.ligado)
# carro.desligar()
# print(carro.ligado)

# carro = Veiculo("Preto")
# print(carro.cor)
# print(carro.ligado)

# carro2 = Veiculo("Branco") #Nascendo cor preto
# print("A cor do carro 2 é :" + carro2.cor)
# print(carro2.ligado)

# carro3 = Veiculo("Azul") 
# print(carro3.cor)
# print(carro3.ligado)

