from Paciente import Paciente
from paciente_particular import Paciente_part
from paciente_convenio import Paciente_conv



print("=====================================")
# Paciente
pacient01 = Paciente("Ana Lima", "123", "13/06/1998", "21 99786-5566", "O-", "38572")

pacient01.exibir_info()   
print(pacient01.registrar_atendimento("oftalmo", 80))
print("----------------")
pacient01.exibir_info(True)
print(pacient01.registrar_atendimento("oftalmo", 80))

print("=====================================")
# Paciente_particular

paciente02 = Paciente_part("Daniel", "432", "07/08/2000", "21 99776-6959", "AB", "33449", "Crédito",0.10)

paciente02.exibir_informacoes()
paciente02.calcular_valor_final(200,0)
print("-------------------------------")
paciente02.exibir_informacoes(True)
paciente02.calcular_valor_final(200,30,True)

print("=====================================")
#Paciente_convenio

paciente03 = Paciente_conv("Luanne", "354", "25/02/2000", "21 44562-5421", "O+", "54880", "Saude+", "1113593")

paciente03.exibir_informacoes()
paciente03.registrar_autorizacao("Remoção de gesso")

print("------------------------------")

paciente03.exibir_informacoes(True)
paciente03.registrar_autorizacao("Cirurgia de Ernia",150)

print("=====================================")  