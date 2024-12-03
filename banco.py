import random
import os

class Conta:
    def __init__(self, nome_titular, numero_conta, senha, saldo_corrente=0, saldo_poupanca=0):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self._senha = senha
        self._saldo_corrente = saldo_corrente
        self._saldo_poupanca = saldo_poupanca

    @property
    def saldo_corrente(self):
        return self._saldo_corrente

    @property
    def saldo_poupanca(self):
        return self._saldo_poupanca

    def verificar_senha(self, senha):
        return self._senha == senha

    def sacar(self, valor):
        if self._saldo_corrente >= valor:
            self._saldo_corrente -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente para saque.")

    def depositar(self, valor):
        self._saldo_corrente += valor
        print("Depósito realizado com sucesso!")

    def aplicar(self, valor):
        if self._saldo_corrente >= valor:
            self._saldo_corrente -= valor
            self._saldo_poupanca += valor
            print("Aplicação realizada com sucesso!")
        else:
            print("Saldo insuficiente para aplicação.")

    def resgatar(self, valor):
        if self._saldo_poupanca >= valor:
            self._saldo_poupanca -= valor
            self._saldo_corrente += valor
            print("Resgate realizado com sucesso!")
        else:
            print("Saldo insuficiente para resgate.")

    def extrato(self):
        print(f"\n+------------------------------------------------+")
        print(f"| Titular: {self.nome_titular}")
        print(f"| Número da conta: {self.numero_conta}")
        print(f"| Saldo da Conta Corrente: R$ {self._saldo_corrente:.2f}")
        print(f"| Saldo da Conta Poupança: R$ {self._saldo_poupanca:.2f}")
        print("+------------------------------------------------+\n")

def gerar_numero_conta():
    return f"{random.randint(100, 999)}"

def criar_conta():
    nome_titular = input("Informe o seu nome completo: ")
    numero_conta = gerar_numero_conta()
    senha = input("Crie uma senha numérica de 4 dígitos: ")

    while len(senha) != 4 or not senha.isdigit():
        print("A senha deve conter exatamente 4 dígitos numéricos.")
        senha = input("Crie uma senha numérica de 4 dígitos: ")

    deposito_inicial = float(input("Realize seu primeiro depósito (mínimo R$ 10,00): "))
    while deposito_inicial < 10:
        print("O depósito inicial deve ser de, no mínimo, R$ 10,00.")
        deposito_inicial = float(input("Realize seu primeiro depósito (mínimo R$ 10,00): "))

    conta = Conta(nome_titular, numero_conta, senha, saldo_corrente=deposito_inicial)
    print(f"\nConta criada com sucesso!")
    print(f"Número da conta: {numero_conta}")
    return conta

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("Bem-vindo ao Banco!")
    conta = criar_conta()
    tentativas = 3

    while True:
        print("\nMENU DE OPERAÇÕES")
        print("1 - Sacar")
        print("2 - Depositar")
        print("3 - Aplicar (Corrente -> Poupança)")
        print("4 - Resgatar (Poupança -> Corrente)")
        print("5 - Extrato")
        print("0 - Sair")

        opcao = input("Escolha uma operação: ")
        if opcao == "0":
            print("Obrigado por utilizar nossos serviços!")
            break

        if opcao in ["1", "2", "3", "4", "5"]:
            if opcao != "5":
                senha_digitada = input("Digite sua senha: ")
                if not conta.verificar_senha(senha_digitada):
                    tentativas -= 1
                    print(f"Senha incorreta! Você tem {tentativas} tentativa(s) restante(s).")
                    if tentativas == 0:
                        print("Conta bloqueada. Dirija-se à agência com documento com foto.")
                        break
                    continue

            if opcao == "1":
                valor = float(input("Informe o valor para saque: "))
                conta.sacar(valor)
            elif opcao == "2":
                valor = float(input("Informe o valor para depósito: "))
                conta.depositar(valor)
            elif opcao == "3":
                valor = float(input("Informe o valor para aplicar na poupança: "))
                conta.aplicar(valor)
            elif opcao == "4":
                valor = float(input("Informe o valor para resgatar da poupança: "))
                conta.resgatar(valor)
            elif opcao == "5":
                conta.extrato()
        else:
            print("Opção inválida. Tente novamente.")

        input("Pressione Enter para continuar...")
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()
