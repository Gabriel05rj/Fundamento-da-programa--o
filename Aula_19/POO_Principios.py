# Precisamos criar um molde de uma pessoa => class
# Características => atributos => variáveis
# Ações => métodos => funções

class Pessoa:
    #construct0r
    def __init__(self, nome:str, cpf:str):
        self.nome = nome
        self.cpf = cpf

    # Método de apresentação 
    def apresentar(self) -> str:
        return f"Olá. Meu nome é {self.nome}"
    
pessoa1 = Pessoa("Ana Lima", "123")
pessoa2 = Pessoa("Luis Silva", "975")

print(pessoa1.apresentar())
print(pessoa2.apresentar())