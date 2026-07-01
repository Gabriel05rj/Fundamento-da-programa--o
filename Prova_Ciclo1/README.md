Sistema de Gestão de Pacientes e Atendimentos - Clínicas +

Projeto desenvolvido em Python de forma objetiva a emular um sistema de gestão de pacientes de uma clínica médica, utilizando conceitos de Programação Orientada a Objetos (POO).
O sistema permite armazenar informações de pacientes, exibindo suas informações públicas e privadas quando necessárias.

Foram utilizados os seguintes conceitos:
. Classes e objetos
. Herança
. Encapsulamento
. Métodos
. Construtores (__init__)
. Polimorfismo

Estrutura das Classes

1- Classe Paciente:
É a superclass responsável por armazenar as informações comuns entre todos os tipos de pacientes da clínica

Atributos:

nome
data_nascimento
cpf
telefone
tipo_sanguineo
numero_prontuario

Métodos:

__init__
registrar_atendimento()
exibir_info()

2- Classe Paciente_part:
É uma subclasse que herda atributos da Classe Paciente e adiciona novos atributos pertinentes as suas características

Atributos:

forma_pagamento
desconto_fidelidade

Métodos:

__init__
calcular_valor_final()
exibir_informacoes() [sobrescrito]

3- Classe Paciente_conv
É uma subclasse que herda atributos da Classe Paciente e adiciona novos atributos pertinentes as suas características

Atributos:

nome_convenio
numero_carteirinha

Métodos:

__init__
registrar_autorizacao()
exibir_informacoes() [sobrescrito]


Exemplos de Saída no terminal:

Paciente Particular
Daniel
3349
AB

O valor final da consulta foi de R$ 180.0.
O valor final da consulta foi de R$ 207.0, somado aos R$ 30 de taxa de urgência.

Paciente Convênio
Luanne
54880
O+

Procedimento Remoção de gesso coberto pelo convênio.
O valor da glosa foi de R$ 0.


Aluno: Gabriel Regis Araújo

# Libertade ruma ao Hexa 