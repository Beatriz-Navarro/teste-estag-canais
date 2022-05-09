from classes import Cliente, Transferencia

arquivo = open(r'C:\Users\Beatriz\PycharmProjects\transf_bancaria\teste-estag-canais\my_program\entrada.txt', 'r')
conteudo = arquivo.read()
dados = conteudo.split("|")
id = dados[10]
val = dados[11]
tp = dados[12]
nome_em = dados[13]
agencia_em = dados[14]
conta_em = dados[15]
cpf_em = dados[16]
nome_rp = dados[17]
agencia_rp = dados[18]
conta_rp = dados[19]
cpf_rp = dados[20]
print(id)
print(tp)
arquivo.close()

emissor = Cliente(nome_em, agencia_em, conta_em, cpf_em)
receptor = Cliente(nome_rp, agencia_rp, conta_rp, cpf_rp)
transf = Transferencia(id, val, tp, emissor, receptor)

transf.valida_tipo()
transf.valida_clientes(emissor.cpf, receptor.cpf, emissor.conta, receptor.conta)
#transf.transferir(emissor.saldo, receptor.saldo, transf.valor, emissor, receptor)
