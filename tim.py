def resumo():
    mensagem = "\nTimothy John Berners-Lee KBE, OM, FRS é um físico britânico, criador da World Wide Web, tendo feito a primeira proposta para sua criação a 12 de março de 1989."
    return mensagem


def doutorado():
    mensagem = "\nThe Queen's College, em Oxford, de 1973 a 1976, onde diplomou-se em Física."
    return mensagem


def contribuicoes():
    mensagem = "\nFundou Web (World Wide Web), foi uma voz pioneira a favor da neutralidade da rede, é uma voz presente e quer que a população tenha controle sobre seus próprios dados."
    return mensagem


def artigos():
    mensagem = "\nArtigo sobre a Web 3.0\n Artigo sobre as ameaças que pairam sobre a web\n Artigo sobre 30 anos da web, o que vem agora?"
    return mensagem


def citacoes():
    mensagem = "\nYou affect the world by what you browse."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Tim Berners-Lee.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
