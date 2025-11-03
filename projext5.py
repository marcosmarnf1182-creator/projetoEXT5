alunos = {
    "joao": {"senha": "1234", "nota": None},
    "maria": {"senha": "abcd", "nota": None},
}

professores = {
    "Armando": {"senha": "prof123"},
}

def login_aluno(nome, senha):
    if nome in alunos and alunos[nome]["senha"] == senha:
        return True
    else: 
        return False

def login_professsor(nome, senha):
    if nome in professores and professores[nome] == senha:
        return True
    else: 
        return False


def adicionar_nota(nome_aluno, nota):
    if nome_aluno not in alunos:
        return False
    if nota < 0 or nota > 10:
        return False    
    alunos[nome_aluno]["nota"] = nota
    return True

def consultar_nota(nome):
    if nome not in alunos:
        return None
    return alunos[nome]["nota"]

def main():
    print("== SISTEMA DE NOTAS ==")

    while True:
        print("\n1 - login como professor")
        print("2 - login como aluno")
        print("3 - sair")
        option = input("Escolha uma opção: ")

        if option == "1":
            nome = input("Nome do Professor: ")
            senha = input("Senha: ")
            if login_professsor(nome, senha):
                print("Professor Loggado")
                nome_aluno = input("digite o nome do Aluno")
                nota = float(input("digite a nota (0 a 10)"))
                if adicionar_nota(nome_aluno, nota):
                    print("nota registrada")
                else:
                    print("Erro ao registrar nota")
            else: