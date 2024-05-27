import os

class Paciente:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

class Consulta:
    def __init__(self, codigo, data, hora):
        self.codigo = codigo  # Representa o paciente que irá marcar a consulta
        self.data = data      # Formato: 99/99/9999
        self.hora = hora      # Formato: 99:99

MAX = 5000

pacientes = []
consultas = []

# Função para verificar se um paciente existe pelo código
def cliente_existe(codigo):
    for paciente in pacientes:
        if paciente.codigo == codigo:
            return True
    return False

# Função para verificar se uma consulta já existe na data e hora fornecidas
def consulta_existe(data, hora):
    for consulta in consultas:
        if consulta.data == data and consulta.hora == hora:
            return True
    return False

# Funções para adicionar pacientes e consultas, que podem ser chamadas no menu
def cadastrar_paciente():
    while True:
        codigo = int(input("Digite o código do paciente: "))
        if cliente_existe(codigo):
            print("Paciente já cadastrado! Por favor, insira um novo código.")
        else:
            break
    nome = input("Digite o nome do paciente: ")
    pacientes.append(Paciente(codigo, nome))
    print("Paciente cadastrado com sucesso!")

def cadastrar_consulta():
    codigo = int(input("Digite o código do paciente para a consulta: "))
    if not cliente_existe(codigo):
        print("Paciente não encontrado!")
    else:
        while True:
            data = input("Digite a data da consulta (99/99/9999): ")
            hora = input("Digite a hora da consulta (99:99): ")
            if consulta_existe(data, hora):
                print("Consulta já marcada para esta data e hora! Por favor, escolha outra data e hora.")
            else:
                break
        consultas.append(Consulta(codigo, data, hora))
        print("Consulta cadastrada com sucesso!")

def alterar_paciente():
    codigo = int(input("Digite o código do paciente a ser alterado: "))
    if not cliente_existe(codigo):
        print("Paciente não encontrado!")
    else:
        novo_nome = input("Digite o novo nome do paciente: ")
        for paciente in pacientes:
            if paciente.codigo == codigo:
                paciente.nome = novo_nome
                print("Nome do paciente alterado com sucesso!")
                break

def alterar_consulta():
    codigo = int(input("Digite o código do paciente para alterar a consulta: "))
    if not cliente_existe(codigo):
        print("Paciente não encontrado!")
    else:
        consulta_encontrada = False
        for consulta in consultas:
            if consulta.codigo == codigo:
                consulta_encontrada = True
                while True:
                    nova_data = input("Digite a nova data da consulta (99/99/9999): ")
                    nova_hora = input("Digite a nova hora da consulta (99:99): ")
                    if consulta_existe(nova_data, nova_hora):
                        print("Já existe uma consulta marcada para essa data e hora! Por favor, escolha outra data e hora.")
                    else:
                        consulta.data = nova_data
                        consulta.hora = nova_hora
                        print("Consulta alterada com sucesso!")
                        break
                break
        if not consulta_encontrada:
            print("Nenhuma consulta encontrada para o paciente.")

def excluir_paciente():
    codigo = int(input("Digite o código do paciente a ser excluído: "))
    if not cliente_existe(codigo):
        print("Paciente não encontrado!")
    else:
        global pacientes
        global consultas
        pacientes = [paciente for paciente in pacientes if paciente.codigo != codigo]
        consultas = [consulta for consulta in consultas if consulta.codigo != codigo]
        print("Paciente e consultas associadas excluídos com sucesso!")

def listar_pacientes():
    while True:
        if not pacientes:
            print("Nenhum paciente cadastrado.")
        else:
            for paciente in pacientes:
                print(f"Código: {paciente.codigo}, Nome: {paciente.nome}")
        opcao = input("Pressione 'v' para voltar ao menu principal: ")
        if opcao.lower() == 'v':
            break

def listar_consultas():
    while True:
        if not consultas:
            print("Nenhuma consulta cadastrada.")
        else:
            for consulta in consultas:
                print(f"Código do paciente: {consulta.codigo}, Data: {consulta.data}, Hora: {consulta.hora}")
        opcao = input("Pressione 'v' para voltar ao menu principal: ")
        if opcao.lower() == 'v':
            break

def main():
    while True:
        print("\nBem Vindo à Doutora Janete")
        print('Escolha uma das opções abaixo:')
        print('1 - Cadastrar Pacientes')
        print('2 - Cadastrar Consultas')
        print('3 - Alterar Paciente')
        print('4 - Alterar Consulta')
        print('5 - Excluir Paciente')
        print('6 - Listar Pacientes')
        print('7 - Listar Consultas')
        print('8 - Sair')

        opcao = int(input("Escolha uma das opções: "))
        
        match opcao:
            case 1:
                cadastrar_paciente()
            case 2:
                cadastrar_consulta()
            case 3:
                alterar_paciente()
            case 4:
                alterar_consulta()
            case 5:
                excluir_paciente()
            case 6:
                listar_pacientes()
            case 7:
                listar_consultas()
            case 8:
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
