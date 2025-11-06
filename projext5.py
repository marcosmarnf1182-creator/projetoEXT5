import os
import sys

# Cores ANSI (sem dependências externas)
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Cores básicas
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Cores brilhantes
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Estilos personalizados (mantendo as mesmas cores do tema rich)
    @staticmethod
    def title(text):
        return f"{Colors.BOLD}{Colors.MAGENTA}{text}{Colors.RESET}"
    
    @staticmethod
    def menu(text):
        return f"{Colors.CYAN}{text}{Colors.RESET}"
    
    @staticmethod
    def prompt(text):
        return f"{Colors.BOLD}{Colors.BRIGHT_BLUE}{text}{Colors.RESET}"
    
    @staticmethod
    def success(text):
        return f"{Colors.GREEN}{text}{Colors.RESET}"
    
    @staticmethod
    def error(text):
        return f"{Colors.BOLD}{Colors.RED}{text}{Colors.RESET}"
    
    @staticmethod
    def warning(text):
        return f"{Colors.YELLOW}{text}{Colors.RESET}"
    
    @staticmethod
    def info(text):
        return f"{Colors.CYAN}{text}{Colors.RESET}"

def print_colored(text, style='info'):
    """Imprime texto colorido de acordo com o estilo"""
    styles = {
        'title': Colors.title,
        'menu': Colors.menu,
        'success': Colors.success,
        'error': Colors.error,
        'warning': Colors.warning,
        'info': Colors.info,
    }
    if style in styles:
        print(styles[style](text))
    else:
        print(text)

def input_colored(prompt_text):
    """Input com prompt colorido"""
    return input(Colors.prompt(prompt_text))

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
                        print_colored(
                            f"Aviso: nota inválida no arquivo para {nome}: {nota}",
                            style="warning"
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
    print_colored("== SISTEMA DE NOTAS ==", style="title")

    try:
        while True:
            print()
            print_colored("1 - login como professor", style="menu")
            print_colored("2 - login como aluno", style="menu")
            print_colored("3 - sair", style="menu")
            option = input_colored("Escolha uma opção: ")

            if option == "1":
                nome = input_colored("Nome do Professor: ")
                senha = input_colored("Senha: ")
                if login_professor(nome, senha):
                    print_colored("Professor Logado", style="success")
                    nome_aluno = input_colored("digite o nome do Aluno: ")
                    nota_str = input_colored("digite a nota (0 a 10): ")
                    try:
                        nota = float(nota_str)
                    except ValueError:
                        print_colored("Nota inválida. Use um número entre 0 e 10.", style="error")
                        continue

                    if adicionar_nota(nome_aluno, nota):
                        print_colored("nota registrada", style="success")
                    else:
                        print_colored("Erro ao registrar nota", style="error")
                else:
                    print_colored("usuário ou senha incorretos", style="error")

            elif option == "2":
                nome = input_colored("nome do Aluno: ")
                senha = input_colored("senha: ")
                if login_aluno(nome, senha):
                    print_colored("Aluno Logado", style="success")
                    nota = consultar_nota(nome)
                    if nota is None:
                        print_colored("nenhuma nota foi registrada", style="info")
                    elif nota >= 6:
                        print_colored(f"Nota: {nota} (Aprovado)", style="success")
                    else:
                        print_colored(f"Nota: {nota} (Reprovado)", style="warning")
                else:
                    print_colored("usuário ou senha incorretos", style="error")

            elif option == "3":
                print_colored("fechando...", style="info")
                break

            else:
                print_colored("opção inválida", style="error")
    except KeyboardInterrupt:
        print_colored("\n\nEncerrando o sistema... Até logo!", style="info")
    except EOFError:
        print_colored("\n\nEncerrando o sistema... Até logo!", style="info")


if __name__ == "__main__":
    carregar_notas()

    # Modo demo: mostra exemplos de estilos e encerra — útil para testar
    if "--demo" in sys.argv:
        print_colored("== DEMO DE CORES E ESTILOS ==", style="title")
        print_colored("Mensagem de sucesso", style="success")
        print_colored("Mensagem informativa", style="info")
        print_colored("Mensagem de aviso", style="warning")
        print_colored("Mensagem de erro", style="error")
        print(Colors.prompt("Prompt exemplo"))
        sys.exit(0)

    main()