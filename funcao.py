#Função x Classe
#Função: bloco de código que executa uma palavra 
#Classe: modelo para criar objetos
#Objeto: estrutura que representa uma entidade do mundo real
#Conceito abstrato dentro de um programa

class ContaBancaria:
    def _init_ (self, titular, saldo_inicial = 0):
#Quando utilizar _init_: quando precisa inicializar 
#O objeto com algum valor ou configuração
        self.titular = titular #instância atual do objeto
        self.saldo = saldo_inicial

        def depositar (self,valor):
            if valor > 0: 
                self.saldo += valor #self.saldo = self.saldo + valor
                print(f"Déposito de R$ {valor:.2f}")
            else:
                print("Valor de déposito inválido!")

#criar funções sacar e consultar_salário

        def sacar (self,saque): 
            if 0 < saque <= self.saldo:
                self.saldo -= saque
                print(f"Saque de R${saque:.2f} realizado com sucesso!")

        def consultar_saldo(self):
            print(f"Saldo atual: R$ {self.saldo:.2f}")

conta = ContaBancaria("José, 1000")
conta.consultar_saldo()
conta.depositar(500)
conta.sacar(200)
conta.consultar_saldo()