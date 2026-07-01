from Paciente import Paciente

class Paciente_conv(Paciente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str, nome_convenio: str, numero_carteirinha: str):
        super().__init__(nome, cpf, data_nascimento, telefone, tipo_sanguineo, numero_prontuario)
        self.nome_convenio = nome_convenio
        self.numero_carteirinha = numero_carteirinha

    def registrar_autorizacao(self, procedimento: str, valor_glosa = False) -> None:
        print(f"Procedimento {procedimento} coberto pelo convênio")

        if valor_glosa:
            print(f"O valor da glosa foi de R$ {valor_glosa}")
        else:
            valor_glosa = 0
            print(f"O valor da glosa foi de R$ {valor_glosa}")

    def exibir_informacoes(self, detalhado = False):
        if detalhado == False:
            print(f"Nome: {self.nome}")
            print(f"Número de Prontuári: {self.numero_prontuario}")
            print(f"Tipo samguíneo: {self.tipo_sanguineo}")
        else:
            print(f"Nome: {self.nome}")
            print(f"Cpf: {self._cpf}")
            print(f"Data de nascimento: {self._data_nascimento}")
            print(self._telefone)
            print(f"Tipo samguíneo: {self.tipo_sanguineo}")
            print(f"Número de Prontuári: {self.numero_prontuario}")
            print(f"Nome do Convênio: {self.nome_convenio}")
            print(f"Número da carteirinha: {self.numero_carteirinha}")
