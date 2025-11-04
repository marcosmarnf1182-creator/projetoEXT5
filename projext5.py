import os

# ____________________________________________________________________

alunos = {
    "joao": {"senha": "1234", "nota": None},
    "maria": {"senha": "abcd", "nota": None},
}

professores = {
    "Armando": {"senha": "prof123"},
}


notasfile = os.path.join(os.path.dirname(__file__), "notas.txt")
# ____________________________________________________________________

def login_aluno(nome, senha):
    if nome in alunos and alunos[nome]["senha"] == senha:
        return True
    else: 
        return False


def login_professor(nome, senha):
    if nome in professores and professores[nome]["senha"] == senha:
        return True
    else: 
        return False


def carregar_notas():
    if not os.path.exists(notasfile):
        return
    
    with open(notasfile, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:

            partes = linha.strip().split(":")
            if len(partes) == 2:
                nome, nota = partes
                if nome in alunos:
                    alunos[nome]["nota"] = float(nota)


def salvar_notas():
    with open(notasfile, "w", encoding="utf-8") as arquivo:
        for nome, dados in alunos.items():
            if dados["nota"] is not None:
                arquivo.write(f"{nome}:{dados['nota']}\n")

def adicionar_nota(nome_aluno, nota):
    if nome_aluno not in alunos:
        return False
    if nota < 0 or nota > 10:
        return False    
    
    alunos[nome_aluno]["nota"] = nota
    salvar_notas()
    
    return True


def consultar_nota(nome):
    if nome not in alunos:
        return None
    return alunos[nome]["nota"]

# ____________________________________________________________________


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
            if login_professor(nome, senha):
                print("Professor Loggado")
                nome_aluno = input("digite o nome do Aluno: ")
                nota = float(input("digite a nota (0 a 10): "))
                if adicionar_nota(nome_aluno, nota):
                    print("nota registrada")
                else:
                    print("Erro ao registrar nota")
            else:
                print("usuário ou senha incorretos")

        elif option == "2":
            nome = input("nome do Aluno: ")
            senha = input("senha: ")
            if login_aluno(nome, senha):
                print("Aluno Loggado")
                nota = consultar_nota(nome)
                if nota is None:
                    print("nenhuma nota foi registrada")
                elif nota >= 6:
                    print(f"Nota: {nota} (Aprovado)")
                elif nota < 6:
                    print(f"Nota: {nota} (Reprovado)")
            else:
                print("usuário ou senha incorretos")

        elif option == "3":
            print("fechando...")
            break

        else:
            print("opção inválida")

if __name__ == "__main__":
    carregar_notas() 
    main()