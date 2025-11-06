# testes_sistema_notas.py
from projext5 import login_aluno, login_professor, adicionar_nota, consultar_nota, carregar_notas

print("\n=== TESTES DO SISTEMA DE NOTAS ===\n")

# CT01 — Caixa Preta: login de aluno
print("CT01 — Login de Aluno (Caixa Preta)")
print("Entrada: login_aluno('joao', '1234')")
print("Resultado:", login_aluno("joao", "1234"))
print("-" * 40)

# CT02 — Caixa Branca: adicionar nota
print("CT02 — Adicionar Nota (Caixa Branca)")
print("Entrada: adicionar_nota('joao', 8.5)")
print("Resultado:", adicionar_nota("joao", 8.5))
print("Entrada: adicionar_nota('fake', 7.0)")
print("Resultado:", adicionar_nota("fake", 7.0))
print("Entrada: adicionar_nota('maria', 11.0)")
print("Resultado:", adicionar_nota("maria", 11.0))
print("-" * 40)

# CT03 — Caixa Cinza: persistência
print("CT03 — Persistência (Caixa Cinza)")
carregar_notas()
print("Resultado da consulta após salvar:", consultar_nota("joao"))
print("-" * 40)

# CT04 — Erro esperado: aluno sem nota
print("CT04 — Consulta de Aluno sem Nota (Erro Esperado)")
print("Entrada: consultar_nota('maria')")
print("Resultado:", consultar_nota("maria"))
print("-" * 40)

# CT05 — Erro esperado: nome em maiúsculas
print("CT05 — Login de Professor com Nome em Maiúsculas (Erro Esperado)")
print("Entrada: login_professor('ARMANDO', 'prof123')")
print("Resultado:", login_professor("ARMANDO", "prof123"))
print("-" * 40)

print("\n=== FIM DOS TESTES ===\n")
