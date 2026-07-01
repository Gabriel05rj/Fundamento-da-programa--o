from Paciente import Paciente

class Paciente_part(Paciente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str, forma_pagamento: str, desconto_fidelidade: float):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.forma_pagamento = forma_pagamento
        self.desconto_fidelidade = desconto_fidelidade

    def calcular_valor_final(self, valor_consulta, taxa_urgencia, urgencia = False):
        if urgencia:
            valor = valor_consulta + taxa_urgencia
            desconto = (valor_consulta + taxa_urgencia) * self.desconto_fidelidade  
            valor_final = (valor) - desconto
            print(f"O valor final da consulta foi de R$ {valor_final}, somado aos R$ {taxa_urgencia} de taxa de urgência.")
              
        else:    
            valor = valor_consulta
            desconto = valor_consulta * self.desconto_fidelidade  
            valor_final = (valor) - desconto 
            print(f"O valor final da consulta foi de R$ {valor_final}.")     
            

    

    def exibir_informacoes(self, detalhado = False):
        if detalhado == False:
            print(f"Nome: {self.nome}")
            print(f"Número de Prontuário: {self.numero_prontuario}")
            print(f"Tipo sanguíneo: {self.tipo_sanguineo}")
        else:
            print(f"Nome: {self.nome}")
            print(f"Cpf: {self._cpf}")
            print(f"Data de nascimento: {self._data_nascimento}")
            print(f"Telefone: {self._telefone}")
            print(f"Tipo sanguíneo: {self.tipo_sanguineo}")
            print(f"Número de Prontuário: {self.numero_prontuario}")
            print(f"Forma de Pagamento: {self.forma_pagamento}")
            print(f"Desconto Fidelidade: {self.desconto_fidelidade:.0%}")
            