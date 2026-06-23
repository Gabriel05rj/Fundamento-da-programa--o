# Precisamos criar um molde de uma pessoa => class
# Características => atributos => variáveis
# Ações => métodos => funções

class Pessoa: # Superclass poeque ofereça a herança
    #construct0r
    def __init__(self, nome:str, cpf:str, data_nascimento: str):
        self.nome = nome #atributo público
        self._cpf = cpf #atributo privado
        self.data_nascimento = data_nascimento #atributo público

    # Método de apresentação 
    def apresentar(self) -> str:
        return f"Olá. Meu nome é {self.nome}, {self._cpf}, {self.data_nascimento}"
    
pessoa1 = Pessoa("Ana Lima", "123", "13/06/1998")
pessoa2 = Pessoa("Luis Silva", "975","18/07/1994")

print(pessoa1.apresentar())
print(pessoa2.apresentar())