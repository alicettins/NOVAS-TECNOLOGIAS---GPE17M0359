import datetime

class ContaBancaria:
    _total_contas = 0

    def __init__(self, numero_agencia, tipo_conta, saldo, limite):
        self._numero_agencia = numero_agencia
        self._tipo_conta = tipo_conta
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        ContaBancaria._total_contas += 1
    
    def consultar_saldo(self):
        return self._saldo

    def saca(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            self._historico.registra_transacao(f"Saque de R$ {valor}")
        else:
            print("Saldo insuficiente para saque.")

    def deposita(self, valor):
        self._saldo += valor
        self._historico.registra_transacao(f"Depósito de R$ {valor}. Saldo atual: R$ {self._saldo}")

    def consultar_numero(self):
        return f"Número da conta: {self._numero_agencia}"

    def transfere_para(self, destino, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            destino.deposita(valor)
            self._historico.registra_transacao(f"Transferência de R$ {valor} para a conta {destino._numero_agencia}")
        else:
            print("Saldo insuficiente para transferência.")

    def obter_extrato(self):
        return self._historico.imprime()

    def alterar_titular(self, novo_titular):
        # Implemente a lógica para alterar o titular da conta
        pass

    def fechar_conta(self):
        # Implemente a lógica para fechar a conta
        pass

class Historico:
    def __init__(self):
        self.data_da_abertura = datetime.datetime.now()
        self.transacoes = []

    def registra_transacao(self, transacao):
        self.transacoes.append(transacao)

    def imprime(self):
        print(f"Data de abertura: {self.data_da_abertura}")
        print("Transações:")
        for t in self.transacoes:
            print("-", t)

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    def dados_cliente(self):
        return f"Nome: {self._nome} {self._sobrenome}, CPF: {self._cpf}"

class ContaPoupanca(ContaBancaria):
    _total_poupanca = 0

    def __init__(self, numero_agencia, tipo_conta, saldo, limite, aniversario_conta):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self._aniversario_conta = aniversario_conta
        ContaPoupanca._total_poupanca += 1

    def calcular_juros_mensal(self, taxa_juros):
        juros = self._saldo * (taxa_juros / 100)
        self.deposita(juros)
        self._historico.registra_transacao(f"Juros mensais de R$ {juros}")

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, cheque_especial):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.cheque_especial = cheque_especial

    def utilizar_cheque_especial(self, valor):
        if self.cheque_especial:
            if self._saldo + self._limite >= valor:
                self._saldo -= valor
                self._historico.registra_transacao(f"Utilização de cheque especial: R${valor}")
            else:
                print("Limite de cheque especial excedido.")
        else:
            print("Cheque especial não disponível.")
