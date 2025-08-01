alunos = []

def cadastrar_aluno():
    nome = input('Qual o seu nome? ')
    nota1 = int(input('Qual a sua nota 1? '))
    nota2 = int(input('Qual a sua segunda nota?'))
    media = (nota1+nota2)/2

    aluno = {
        'Nome': nome,
        'Media': media,
    }

    alunos.append(aluno)
    print('Aluno {} foi registrado com media de {} pontos'.format(nome, media))

def mostrar_alunos():
    for aluno in alunos:
        situacao = "Aprovado" if aluno["media"] >= 7 else "Reprovado"
        print(f"Aluno: {aluno['nome']} | Média: {aluno['media']:.1f} | Situação: {situacao}")

while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar aluno")
    print("2 - Mostrar alunos")
    print("3 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        mostrar_alunos()
    elif opcao == "3":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida.")