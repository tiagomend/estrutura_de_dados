"""
    Criaremos um TAD a partir de uma necessidade identificada.
    Nosso programa precisa criar um tipo de dado que represente a
    conta-corrente de um banco. Esta conta deverá ser capaz de realizar
    saques, depósitos e consultar saldo atual.

    FONTE:
    Livro: Estrutura de dados
    Autor: Rafael Albuquerque Pinto
    Editora: SAGAH, 2019
"""


class ContaCorrente:
    def __init__(self, nome, Ag, CC, saldo): # Identificação das variáveis
        self.cliente = str(nome)
        self.agencia = int(Ag)
        self.conta = int(CC)
        self.saldo = float(saldo)
    
    # Identificação das operações
    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo = self.saldo - valor

    def verificar_saldo(self):
        print("O saldo atual é de {:.2f}".format(self.saldo))


# CLI para teste
escolha = 3
print("-" * 30)
print("BANCO DO TIAGO")
print("-" * 30)

while escolha != 0:
    print("1. Criar nova conta")
    print("2. Consultar minha conta")
    print("0. Sair")
    escolha = int(input("Escolha a opção: "))

    if escolha == 1: # Bloco para criação de CC
        nome = input("Nome: ")
        agencia = input("Ag: ")
        conta = input("CC: ")
        saldo = input("Saldo: ")
        CC = ContaCorrente(
            nome=nome, 
            Ag=agencia,
            CC=conta,
            saldo=saldo
            )
        print("CONTA CRIADA COM SUCESSO!\n")
        continue

    else:
        consulta = 1
        while consulta != 0: # Bloco para consulta de CC
            print("\nO QUE DESEJA FAZER?\n")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Consultar saldo")
            print("0. Voltar menu inicial")
            consulta = int(input("Sua escolha: "))
            if consulta == 1: # Se escolher "1. Depositar"
                valor = float(input("Valor do depósito: "))
                try:
                    CC.deposito(valor)
                except:
                    print("Sua conta não existe. Por favor, digite (1) para criar uma nova.")
                    break
                continuar = input("Deseja continuar? S/n ")
                if continuar == "S" or continuar == "s":
                    continue
                else:
                    break
            elif consulta == 2: # Se escolher "2. Sacar"
                valor = float(input("Valor do saque: "))
                try:
                    CC.saque(valor)
                except:
                    print("Sua conta não existe. Por favor, digite (1) para criar uma nova.")
                    break
                continuar = input("Deseja continuar? S/n ")
                if continuar == "S" or continuar == "s":
                    continue
                else:
                    break
            elif consulta == 3: # Se escolher "3. Consultar saldo"
                try:
                    CC.verificar_saldo()
                except:
                    print("Sua conta não existe. Por favor, digite (1) para criar uma nova.")
                    break
                continuar = input("Deseja continuar? S/n ")
                if continuar == "S" or continuar == "s":
                    continue
                else:
                    break
            else: # Se escolher "0. Voltar menu inicial"
                break
