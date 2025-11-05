import os
import sys
from rich.console import Console
from rich.theme import Theme

# Tema personalizado (você pode ajustar cores aqui)
custom_theme = Theme(
    {
        "title": "bold magenta",
        "menu": "cyan",
        "prompt": "bold bright_blue",
        "success": "green",
        "error": "bold red",
        "warning": "yellow",
        "info": "cyan",
        "highlight": "bold bright_blue",
    }
)

console = Console(theme=custom_theme)

# ____________________________________________________________________

alunos = {
    "joao": {"senha": "1234", "nota": None},
    "maria": {"senha": "abcd", "nota": None},
}

professores = {"Armando": {"senha": "prof123"}}


notasfile = os.path.join(os.path.dirname(__file__), "notas.txt")
# ____________________________________________________________________


def _find_key(mapping, name):
    """Retorna a chave real em `mapping` que case-insensitivamente corresponde a `name`.
    Ex.: _find_key(alunos, 'Joao') -> 'joao' se existir.
    """
    if not name:
        return None
    target = name.strip().lower()
    for k in mapping:
        if k.lower() == target:
            return k
    return None


def login_aluno(nome, senha):
    key = _find_key(alunos, nome)
    return bool(key and alunos[key]["senha"] == senha)


def login_professor(nome, senha):
    # permite correspondência case-insensitive para professores também
    key = _find_key(professores, nome)
    return bool(key and professores[key]["senha"] == senha)


def carregar_notas():
    if not os.path.exists(notasfile):
        return

    with open(notasfile, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(":")
            if len(partes) == 2:
                nome, nota = partes
                if nome in alunos:
                    try:
                        alunos[nome]["nota"] = float(nota)
                    except ValueError:
                        console.print(
                            f"Aviso: nota inválida no arquivo para {nome}: {nota}",
                            style="warning",
                        )


def salvar_notas():
    with open(notasfile, "w", encoding="utf-8") as arquivo:
        for nome, dados in alunos.items():
            if dados["nota"] is not None:
                arquivo.write(f"{nome}:{dados['nota']}\n")


def adicionar_nota(nome_aluno, nota):
    key = _find_key(alunos, nome_aluno)
    if not key:
        return False
    if nota < 0 or nota > 10:
        return False
    alunos[key]["nota"] = nota
    salvar_notas()

    return True


def consultar_nota(nome):
    key = _find_key(alunos, nome)
    if not key:
        return None
    return alunos[key]["nota"]

# ____________________________________________________________________


def main():
    console.print("== SISTEMA DE NOTAS ==", style="title")

    while True:
        console.print()
        console.print("1 - login como professor", style="menu")
        console.print("2 - login como aluno", style="menu")
        console.print("3 - sair", style="menu")
        option = console.input("[prompt]Escolha uma opção[/prompt]: ")

        if option == "1":
            nome = console.input("[prompt]Nome do Professor[/prompt]: ")
            senha = console.input("[prompt]Senha[/prompt]: ")
            if login_professor(nome, senha):
                console.print("Professor Loggado", style="success")
                nome_aluno = console.input("[prompt]digite o nome do Aluno[/prompt]: ")
                nota_str = console.input("[prompt]digite a nota (0 a 10)[/prompt]: ")
                try:
                    nota = float(nota_str)
                except ValueError:
                    console.print("Nota inválida. Use um número entre 0 e 10.", style="error")
                    continue

                if adicionar_nota(nome_aluno, nota):
                    console.print("nota registrada", style="success")
                else:
                    console.print("Erro ao registrar nota", style="error")
            else:
                console.print("usuário ou senha incorretos", style="error")

        elif option == "2":
            nome = console.input("[prompt]nome do Aluno[/prompt]: ")
            senha = console.input("[prompt]senha[/prompt]: ")
            if login_aluno(nome, senha):
                console.print("Aluno Loggado", style="success")
                nota = consultar_nota(nome)
                if nota is None:
                    console.print("nenhuma nota foi registrada", style="info")
                elif nota >= 6:
                    console.print(f"Nota: {nota} (Aprovado)", style="success")
                else:
                    console.print(f"Nota: {nota} (Reprovado)", style="warning")
            else:
                console.print("usuário ou senha incorretos", style="error")

        elif option == "3":
            console.print("fechando...", style="info")
            break

        else:
            console.print("opção inválida", style="error")


if __name__ == "__main__":
    carregar_notas()

    # Modo demo: mostra exemplos de estilos e encerra — útil para testar
    if "--demo" in sys.argv:
        console.print("== DEMO DE CORES E ESTILOS ==", style="title")
        console.print("Mensagem de sucesso", style="success")
        console.print("Mensagem informativa", style="info")
        console.print("Mensagem de aviso", style="warning")
        console.print("Mensagem de erro", style="error")
        console.print("Prompt exemplo", style="prompt")
        sys.exit(0)

    main()