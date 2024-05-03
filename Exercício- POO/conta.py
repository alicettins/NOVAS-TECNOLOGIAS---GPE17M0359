from datetime import datetime

class ContaBancaria:
    def __init__(self, numero_agencia, tipo_conta, saldo, limite):
        self._numero_agencia = numero_agencia
        self._tipo_conta = tipo_conta
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        self._saldo = novo_saldo

    def consultar_saldo(self):
        return self.saldo

    def saca(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.historico.transacoes.append(f"Saque de {valor}")
            return True
        else:
            return False

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"Depósito de {valor}")

    def transfere_para(self, destino, valor):
        if self.saca(valor):
            destino.deposita(valor)
            self.historico.transacoes.append(f"Transferência de {valor} para {destino.numero_agencia}")
            return True
        else:
            return False

    def obter_extrato(self):
        return self.historico.imprime()

    def alterar_titular(self, novo_titular):
        self.titular = novo_titular

    def fechar_conta(self):
        self.titular = None
        self.historico.transacoes.append("Conta fechada")

class Historico:
    def __init__(self):
        self.data_da_abertura = datetime.now()
        self.transacoes = []

    def imprime(self):
        for transacao in self.transacoes:
            print(transacao)

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    @staticmethod
    def dados_cliente(nome, sobrenome, cpf):
        return f"Nome: {nome} {sobrenome}, CPF: {cpf}"

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, aniversario_conta):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.aniversario_conta = aniversario_conta

    def calcular_juros_mensal(self):
        pass

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, cheque_especial):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.cheque_especial = cheque_especial

    def utilizar_cheque_especial(self, valor):
        if valor <= self.limite:
            self.saldo -= valor
            self.historico.transacoes.append(f"O cheque especial no valor de {valor}")
            return True
        else:
            return False
