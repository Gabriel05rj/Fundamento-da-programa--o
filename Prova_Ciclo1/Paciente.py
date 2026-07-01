class Paciente:
    def __init__(self,nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str):
        self.nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._telefone = telefone
        self.tipo_sanguineo = tipo_sanguineo
        self.numero_prontuario = numero_prontuario

    def registrar_atendimento(self, tipo, custo):
        return f"O(a) paciente passor por um atendimento do tipo {tipo} e de custo R$ {custo} reais"

    def exibir_info(self, detalhado = False):
        if detalhado == False:
            print(f"Nome: {self.nome}")
            print(f"Número Prontuário: {self.numero_prontuario}")
            print(f"Tipo sanguíneo: {self.tipo_sanguineo}")
        else:
            print(f"Nome: {self.nome}")
            print(f"Cpf: {self._cpf}")
            print(f"Data de Nascimento: {self._data_nascimento}")
            print(f"Telefone: {self._telefone}")
            print(f"Tipo sanguíneo: {self.tipo_sanguineo}")
            print(f"Número Prontuário: {self.numero_prontuario}")
  