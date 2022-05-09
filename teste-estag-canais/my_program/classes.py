import sys
class Cliente:
    def __init__(self, nome, agencia, conta, cpf, saldo = 0):
        self.nome = nome
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    def setSaldo(self, x):
        self.saldo=x
    def getNome(self, nome):
        self.nome=nome
    def getCPF(self, cpf):
        self.CPF
    def getAgencia(self, agencia):
        self.agencia=agencia
    def getConta(self, conta):
        self.conta=conta
    def getSaldo(self, saldo):
        self.saldo=saldo

class Transferencia:
    def __init__(self, id, valor, tipo, emissor, receptor):
        self.id=id
        self.valor=valor
        self.tipo=tipo
        self.emissor = emissor
        self.receptor = receptor
    def setId(self, id):
        self.id=id

    def valida_tipo(self):
        val = int(self.valor)
        if self.tipo == 'PIX' and val > 5000:
            try:
                sys.exit()
            except SystemExit:
                print('Sua transferência não foi completada pois o limite para transações PIX é 5 mil.')
        elif self.tipo == 'TED' and (val < 5000 or val > 10000):
            try:
                sys.exit()
            except SystemExit:
                print('Sua transferência não foi completada pois os valores para transações TED devem ser maiores que 5 mil e menores ou iguais a 10 mil')
        elif self.tipo == 'DOC' and val <= 10000:
            try:
                sys.exit()
            except SystemExit:
                print('Sua transferência não foi completada pois os valores para transações DOC devem ser maiores que 10 mil')

    def valida_clientes(self, cpf1, cpf2, conta1, conta2):
        if cpf1 == cpf2 and conta1 == conta2:
            try:
                sys.exit()
            except SystemExit:
                print('Não é possível realizar uma transferência para a mesma conta')

    def transferir(self, saldo_emissor, saldo_receptor, valor, cli1: Cliente, cli2: Cliente):
        if saldo_emissor < valor:
            try:
                sys.exit()
            except SystemExit:
                print('Sua transferência não foi completada por saldo insuficiente')
        else:
            x = saldo_emissor - valor
            cli1.setSaldo(x)
            print(saldo_emissor)
            y = saldo_receptor - valor
            cli2.setSaldo(y)
            print(saldo_receptor)
            saldo_receptor(y)
            print('Sua transferência foi realizada com sucesso:/n Saldo Emissor: ' + saldo_emissor + '/n Saldo Receptor: ' + saldo_receptor)

