# Luciano Paranhos (42324882)
# Exercício 05 - FCC

import os
from sys import platform

# Variavel que armazena o comando usado para limpar a tela.
# No linux ou macOS o comando é identico e considero como padrao.
# Se for windows o comando será trocado para cls
clear_cmd = "clear"
if platform == "win32":
    clear_cmd = "cls"

# Variavel usada na definição do sabor do sorvete
sabor_sorvete = ""

# Variaveis para somar o total de participantes na pesquisa
# A soma de participantes homem ou mulheres indica se a pesquisa foi realizada
total_participante_homem = 0
total_participante_mulher = 0

# Variavel que guarda a soma do total de mulheres maior de 20 anos que achou o sorvete bom
# Variavel que guarda a soma do total de mulheres maior de 30 anos que achou o sorvete ruim
# Variavel que guarda a soma do total de homens que achou o sorvete péssimo
total_homem_escolheu_pessimo = 0
total_mulher_escolheu_bom = 0
total_mulher_escolheu_ruim = 0

# Variavel de controle para determinar o fim da execução
fim = False
while not fim:
    # Limpa o conteúdo para melhorar a visualização dos dados
    os.system(clear_cmd)

    # Exibe o menu de opções
    print("--- MGX Sorvetes Especiais - Pesquisa de Satisfação ---")
    print("-------------------------------------------------------")
    print("")
    print("Escolha as opções para realizar a pesquisa:")
    print("1. Definir o sabor do sorvete")
    print("2. Realizar a pesquisa")
    print("3. Apresentar o resultado da pesquisa")
    print("4. Fechar o programa")
    print("")

    # Obtem a opção que o usuário escolheu
    opcao = int(input("Opção: "))

    # o programa continua a execução se a opção escolhida não foi a 4
    if opcao == 1:
        os.system(clear_cmd)

        print("Escreva o sabor do sorvete para a pesquisa")
        sabor_sorvete = input("Sabor: ")

    elif opcao == 2:
        os.system(clear_cmd)

        # Verifica se o sabor do sorvete foi definido para poder continuar com a pesquisa
        if sabor_sorvete == "":
            print("O sabor do sorvete precisa ser definido primeiro...")
            input("Aperte <Enter> para continuar")
        
        # Coleta os dados da pesquisa
        else:
            print(f"Opnião sobre o sorvete sabor {sabor_sorvete}")
            print("")

            print("Qual o gênero do participante?")
            print("H para homem ou M para mulher")
            participante_genero = input("Gênero: ")
            print("")

            print("Qual a idade do participante")
            participante_idade = int(input("Idade: "))
            print("")

            print("Opnião: (1) Bom, (2) Ruim ou (3) Péssimo")
            participante_opniao = int(input("O sorvete é: "))

            # Transforma o valor da variável em maiúscula para garantir a comparação
            if participante_genero.upper() == "H":
                total_participante_homem = total_participante_homem + 1

                if participante_opniao == 3:
                    total_homem_escolheu_pessimo = total_homem_escolheu_pessimo + 1

            else:
                total_participante_mulher = total_participante_mulher + 1

                if participante_idade > 30 and participante_opniao == 2:
                    total_mulher_escolheu_ruim = total_mulher_escolheu_ruim + 1

                if participante_idade > 20 and participante_opniao == 1:
                    total_mulher_escolheu_bom = total_mulher_escolheu_bom + 1

    elif opcao == 3:
        os.system(clear_cmd)

        # Soma o total de participantes homens e mulheres para obter o total geral de participantes
        total_geral = total_participante_homem + total_participante_mulher

        if sabor_sorvete == "":
            print("O sabor do sorvete precisa ser definido primeiro...")
        
        # Verifica se não houve participantes na pesquisa
        elif total_geral == 0:
            print("O pesquisa precisa ser realizada para exibir o resultado...")
        
        # Exibe as estatisticas
        else:
            print(f"Pesquisa realizada com {total_geral} participantes. {total_participante_homem} homens e {total_participante_mulher} mulheres")
            print("")
            print(f"Total de homens que indicou o sorvete como péssimo: ({total_homem_escolheu_pessimo})")
            print(f"Total de mulheres maiores de 20 anos indicaram o sorvete como bom: ({total_mulher_escolheu_bom})")
            print(f"Total de mulheres maiores de 30 anos indicaram o sorvete como ruim: ({total_mulher_escolheu_ruim})")
            print("")

        # Truque para o usuário consiga ver as estatisticas antes de voltar para o menu de opções
        input("Aperte <Enter> para continuar")

    elif opcao == 4:
        fim = True
        break

    else:
        os.system(clear_cmd)
        print("Opção invalida")
        input("Aperte <Enter> para continuar")

print("Fim da pesquisa. Obrigado")
