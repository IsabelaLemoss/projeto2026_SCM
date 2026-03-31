# Cadastro de pets
pets = []

def cadastrar_pet(nome, raca, dono):
    pets.append({'nome': nome, 'raca': raca, 'dono': dono})
    print(f'Banho agendado para {nome_pet} em {data} as {hora}')
def agendar_banho(nome_pet, data, hora):
    print("Banho agendado para " + nome_pet + " em " + data + " as " + hora)

def listar_agendamentos():
    print("Listando todos os agendamentos do dia...")