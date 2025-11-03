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
