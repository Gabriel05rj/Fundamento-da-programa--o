idade = int(input("Informe sua idade: "))
vip = input("Informe se é um cliente vip: [sim], [não]: ")
cadastro = input("Informe se possue cadastro no shopping: [cadastrado], [sem cadastro]: ")
tipo_veiculo = input("Informe o tipo de veículo: [caminhão], [carro], [moto]: ")
# criar 3 regras de negocio
#tipo de veiculo(caminhão)
#ordem de prioridade para vips, cadastrados e sem cadastro
#menores de idade não entram



if idade < 18:
     print("Entrada Negada, motorista menor de idade.")
else:
    if vip == "sim":
        print("Entrada aprovada automaticamente, cliente vip!")
    elif cadastro == "cadastrado":
        print("Entrada aprovada, cliente cadastrado.")
    else:
        print("Cliente sem cadastro, aguarde autorização.")
        if tipo_veiculo == "caminhão":
            print("Entrada aprovada. Prioridade para entrega de carga.")
        elif tipo_veiculo == "carro" or tipo_veiculo == "moto":
            print("Entrada permitida.")

