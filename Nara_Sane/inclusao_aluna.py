# Incluir nova aluna
# Dados do dataset anterior

dataset = {
    ("Ana", "Silva"): {
        "Turma": "Turma A",
        "Notas": [7.5, 8.0, 9.0],
        "Presença": [True, True, False, True, True],
        "Participação": 8.5
    },
    ("Mariana", "Santos"): {
        "Turma": "Turma B",
        "Notas": [6.0, 7.5, 8.5],
        "Presença": [True, True, True, False, True],
        "Participação": 7.2
    },
    ("Carla", "Oliveira"): {
        "Turma": "Turma A",
        "Notas": [8.0, 7.5, 8.5],
        "Presença": [True, True, True, True, True],
        "Participação": 8.2
    },
    ("Juliana", "Ferreira"): {
        "Turma": "Turma C",
        "Notas": [9.0, 8.5, 7.0],
        "Presença": [True, True, True, True, True],
        "Participação": 8.7
    },
    ("Patrícia", "Souza"): {
        "Turma": "Turma B",
        "Notas": [7.0, 7.0, 7.5],
        "Presença": [True, False, True, True, True],
        "Participação": 7.2
    },
    ("Aline", "Martins"): {
        "Turma": "Turma A",
        "Notas": [8.5, 8.0, 9.0],
        "Presença": [True, True, True, True, True],
        "Participação": 8.5
    },
    ("Fernanda", "Costa"): {
        "Turma": "Turma C",
        "Notas": [6.5, 7.0, 8.0],
        "Presença": [True, True, True, False, True],
        "Participação": 7.2
    },
    ("Camila", "Pereira"): {
        "Turma": "Turma B",
        "Notas": [7.5, 8.0, 8.5],
        "Presença": [True, True, True, True, True],
        "Participação": 8.0
    },
    ("Luana", "Rodrigues"): {
        "Turma": "Turma A",
        "Notas": [9.0, 9.0, 8.5],
        "Presença": [True, True, True, True, True],
        "Participação": 8.8
    },
    ("Beatriz", "Lima"): {
        "Turma": "Turma C",
        "Notas": [8.0, 7.5, 7.0],
        "Presença": [True, True, True, False, True],
        "Participação": 7.5
    }
}

def incluir_nova_aluna():
    global dataset  # Usar a variável global para referenciar o dataset que armazena os dados das alunas
    
    # Pedir para o usuário digitar os dados da aluna
    nome = input("Digite o nome da aluna: ")
    sobrenome = input("Digite o sobrenome da aluna: ")
    turma = input("Digite a turma da aluna: ")
    nota1 = input("Digite a primeira nota da aluna: ")
    nota2 = input("Digite a segunda nota da aluna: ")
    nota3 = input("Digite a terceira nota da aluna: ")
    presenca1 = input("Digite a presença da primeira aula (True/False): ")
    presenca2 = input("Digite a presença da segunda aula (True/False): ")
    presenca3 = input("Digite a presença da terceira aula (True/False): ")
    presenca4 = input("Digite a presença da quarta aula (True/False): ")
    presenca5 = input("Digite a presença da quinta aula (True/False): ")
    participacao = input("Digite a nota de participação da aluna: ")
    
    # Converter notas e presenças
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)
    presenca1 = presenca1 == 'True'
    presenca2 = presenca2 == 'True'
    presenca3 = presenca3 == 'True'
    presenca4 = presenca4 == 'True'
    presenca5 = presenca5 == 'True'
    participacao = float(participacao)
    
    # Adicionar a nova aluna ao dataset
    dataset[(nome, sobrenome)] = {
        "Turma": turma,
        "Notas": [nota1, nota2, nota3],
        "Presença": [presenca1, presenca2, presenca3, presenca4, presenca5],
        "Participação": participacao
    }
    
    print(f"Aluna {nome} {sobrenome} adicionada com sucesso!")

def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---")
    print("Sistema de informações de alunas")
    
    incluir_nova_aluna()  # Chama a função para incluir uma nova aluna
    print(dataset)  # Verifica o dataset após adicionar a nova aluna
    
main()