import json
import os
import sys
from pathlib import Path
from random import randint

from src.models.aluno import alunos
from src.models.gerente import inf_Gerente
from src.models.professor import professores

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

caminhoAluno = 'C:\\Users\\HP\\Desktop\\ProjetosPYTHON\\Sistema_Preparatoria\\doc\\alunos.json'
caminhoProfessor = 'C:\\Users\\HP\\Desktop\\ProjetosPYTHON\\Sistema_Preparatoria\\doc\\professores.json'
""" 
COISAS A FAZER NA PROXIMA ACTUALIZACAO: 

. Meter as verificações e condiçoes antes de add o dado na BD. ex: verificar BI se é um BI correto segundo a lei, verificar se na idade n está -1/ 0 e etc e mais outros dados
. adicionar a parte do listar alunos e professores
. adicionar a parte do rem alunos e rem professores
. adicionar parte de editar um aluno ou professor
. cada aluno add deve ir em uma turma e cada professor deve dar aula nas turmas, devo pensar nisso e add novas funcoes e verificaçoes no programa

O RESTO PENSO, QUANDO FAZER AS COISAS LISTAS ACIMA

"""


def add_Professor():
    # meter as regras e as verificacoes aqui

    loop = True
    while loop:
        quantidade_de_professores = 0

        arquivo_vazio_ou_Nao = os.stat(caminhoProfessor).st_size == 0
        if (arquivo_vazio_ou_Nao):  # Se estiver vazio:

            nome = str(input('Nome do Professor: '))
            idade = int(input('idade do Professor: '))
            sexo = input('Sexo: ').upper()

            quantidade_de_professores += 1
            professores = [{'nome_P': nome, 'idade': idade, 'sexo': sexo, 'bI': ' ', 'senha_P': ' ', 'classe_que_dara_aulas': 0, 'disciplina': ' ', 'iD': 0},]

            numBI = str(input('Numero do BI: '))
            professores[0]['bI'] = numBI

            senhaP = str(input('Senha do Professor: '))
            professores[0]['senha_P'] = senhaP

            disc = str(input('Disciplina que Leciona: ').upper())
            professores[0]['disciplina'] = disc

            classe = int(input('A Classe que Leciona: '))
            professores[0]['classe_que_dara_aulas'] = classe

            iD = randint(2023000, 2024000)
            professores[0]['iD'] = iD

            with open(caminhoProfessor, 'w', encoding='utf8') as arquivo:
                json.dump(professores, arquivo, ensure_ascii=False, indent=2,)

            print(quantidade_de_professores, 'º PROFESSOR ADICIONADO AO SISTEMA.')

            resposta = str(input('DESEJA ADICIONAR MAIS PROFESSORES?[S/N]: ').upper())
            if resposta == 'SIM' or resposta == 'S':
                os.system('cls')
                continue
            else:
                os.system('cls')
                loop = False
                break

        else:
            nome = str(input('Nome do Professor: '))
            idade = int(input('idade do Professor: '))
            sexo = input('Sexo: ').upper()

            with open(caminhoProfessor, 'r') as arquivo:
                dados_professor = json.load(arquivo)

            dados_professor.append({'nome_P': nome, 'idade': idade, 'sexo': sexo, 'bI': ' ', 'senha_P': ' ', 'classe_que_dara_aulas': 0, 'disciplina': ' ', 'iD': 0})

            quantidade_de_professores, i = len(dados_professor), len(dados_professor)
            i -= 1

            def verifica_Existencia_de_BI(numbI):
                retorno = 0

                for dado in dados_professor:
                    if dado.get('bI') == numbI:
                        print('O numero do BI "{}", ja existe registrado. Com o professor "{}".'.format(dado.get('bI'), dado.get('nome_P')))
                        retorno = 1

                if retorno == 1:
                    resposta = str(input('ADICIONAR NOVO NUMERO DE BI PARA O NOVO PROFESSOR?[S/N] ').upper())
                    if resposta == 'S' or resposta == 'SIM':
                        return 1
                    else:
                        return 2
                else:
                    return 0

            ciclo_Repeticao = True
            while ciclo_Repeticao:
                bI = str(input('Numero do BI: ').upper())
                resposta = verifica_Existencia_de_BI(bI)
                if resposta == 1:
                    continue
                elif resposta == 2:
                    print('OPERACAO CANCELADA!')
                    return
                else:
                    dados_professor[i]['bI'] = bI
                    ciclo_Repeticao = False
                    break

            senhaP = str(input('Senha do Professor: '))
            dados_professor[i]['senha_P'] = senhaP

            disc = str(input('Disciplina que Leciona: ').upper())
            dados_professor[i]['disciplina'] = disc

            classe = int(input('A Classe que Leciona: '))
            dados_professor[i]['classe_que_dara_aulas'] = classe

            iD = randint(2023000, 2024000)  # Sera permitido apenas o cadastro de 1000 professores.
            for dado in dados_professor:
                while dado.get('iD') == iD:
                    iD = randint(202300, 202400)
                else:
                    dados_professor[i]['iD'] = iD

            with open(caminhoProfessor, 'w', encoding='utf8') as arquivo:
                json.dump(dados_professor, arquivo, ensure_ascii=False, indent=2, )

            print(quantidade_de_professores, 'º ALUNO ADICIONADO AO SISTEMA.')

            resposta = str(input('DESEJA ADICIONAR MAIS PROFESSORES?[S/N]: ').upper())
            if resposta == 'SIM' or resposta == 'S':
                os.system('cls')
                continue
            else:
                os.system('cls')
                loop = False
                break


def add_aluno():
    # criar regras para verificar os dados antes de seres add na lista.
    loop = True
    while loop:
        quantidade_de_alunos = 0

        nome = input('Nome do Aluno: ')
        idade = int(input('Sua idade: '))
        sexo = input('Seu Sexo: ')

        arquivo_vazio_ou_Nao = os.stat(caminhoAluno).st_size == 0
        if (arquivo_vazio_ou_Nao):  # Se estiver vazio:

            quantidade_de_alunos += 1
            alunos = [{'Nome_A': nome, 'Idade': idade, 'Sexo': sexo, 'N_Bi': ' ', 'Ano_Lectivo': 0, 'Disciplinas': [], 'senha_A': ' ', 'ID': 0},]

            numBI = input('Numero do BI: ')
            alunos[0]['N_Bi'] = numBI

            ano = int(input('Ano Letivo: '))
            alunos[0]['Ano_Lectivo'] = ano

            if ano == 7:
                alunos[0]['Disciplinas'] = ['ED. FISICA', 'MATEMATICA', 'EVP', 'EMC', 'FISICA ', 'BIOLOGIA', 'GEOGRAFIA', 'HISTORIA', 'PORTUGUES', 'QUIMICA']
            elif ano == 8:
                alunos[0]['Disciplinas'] = ['ED. FISICA', 'MATEMATICA vol.2', 'EMC vol.2', 'FISICA vol.2', 'BIOLOGIA vol.2', 'GEOGRAFIA vol.2', 'INGLES vol.1 ', 'PORTUGUES vol.2', 'QUIMICA vol2']
            elif ano == 9:
                alunos[0]['Disciplinas'] = ['ED. FISICA', 'MATEMATICA vol.3', 'ED. LABORAL', 'EMC vol.3', 'EMPREENDEDORISMO', 'FISICA vol.3', 'GEOGRAFIA vol.3', 'INGLES vol.2', 'BIOLOGIA vol.3', 'PORTUGUES vol.3']

            senha = input('Digite a senha do aluno: ')
            alunos[0]['senha_A'] = senha

            numeroMatricula = randint(20230000, 20240000)
            alunos[0]['ID'] = numeroMatricula

            with open(caminhoAluno, 'w', encoding='utf8') as arquivo:
                json.dump(alunos, arquivo, ensure_ascii=False, indent=2,)

            print(quantidade_de_alunos, 'º ALUNO ADICIONADO AO SISTEMA.')

            resposta = str(input('DESEJA ADICIONAR MAIS ALUNOS?[S/N]: ').upper())
            if resposta == 'SIM' or resposta == 'S':
                os.system('cls')
                continue
            else:
                os.system('cls')
                loop = False
                break

        else:

            with open(caminhoAluno, 'r') as arquivo:
                dados_alunos = json.load(arquivo)

            dados_alunos.append({'Nome_A': nome, 'Idade': idade, 'Sexo': sexo, 'N_Bi': ' ', 'Ano_Lectivo': 0, 'Disciplinas': [], 'senha_A': ' ', 'ID': 0})

            quantidade_de_alunos, i = len(dados_alunos), len(dados_alunos)
            i -= 1

            def verifica_Existencia_de_BI(numbI):
                retorno = 0

                for dado in dados_alunos:
                    if dado.get('N_Bi') == numbI:
                        print('O numero do BI "{}", ja existe registrado. Com o aluno "{}".'.format(dado.get('N_Bi'), dado.get('Nome_A')))
                        retorno = 1

                if retorno == 1:
                    resposta = str(input('ADICIONAR NOVO NUMERO DE BI PARA O NOVO ALUNO?[S/N] ').upper())
                    if resposta == 'S' or resposta == 'SIM':
                        return 1
                    else:
                        return 2
                else:
                    return 0

            ciclo_Repeticao = True
            while ciclo_Repeticao:
                bI = str(input('Numero do BI: ').upper())
                resposta = verifica_Existencia_de_BI(bI)
                if resposta == 1:
                    continue
                elif resposta == 2:
                    print('OPERACAO CANCELADA!')
                    return
                else:
                    dados_alunos[i]['N_Bi'] = bI
                    ciclo_Repeticao = False
                    break

            ano = int(input('Ano Letivo: '))
            dados_alunos[i]['Ano_Lectivo'] = ano

            if ano == 7:
                dados_alunos[i]['Disciplinas'] = ['ED. FISICA', 'MATEMATICA', 'EVP', 'EMC', 'FISICA ', 'BIOLOGIA', 'GEOGRAFIA', 'HISTORIA', 'PORTUGUES', 'QUIMICA']
            elif ano == 8:
                dados_alunos[i]['Disciplinas'] = ['ED. FISICA', 'MATEMATICA vol.2', 'EMC vol.2', 'FISICA vol.2', 'BIOLOGIA vol.2', 'GEOGRAFIA vol.2', 'INGLES vol.1 ', 'PORTUGUES vol.2', 'QUIMICA vol2']
            elif ano == 9:
                dados_alunos[i]['Disciplinas'] = ['ED. FISICA', 'MATEMATICA vol.3', 'ED. LABORAL', 'EMC vol.3', 'EMPREENDEDORISMO', 'FISICA vol.3', 'GEOGRAFIA vol.3', 'INGLES vol.2', 'BIOLOGIA vol.3', 'PORTUGUES vol.3']

            senha = input('Digite a senha do aluno: ')
            dados_alunos[i]['senha_A'] = senha

            numeroMatricula = randint(20230000, 20240000)  # sera permitido apenas o cadastro de 10 mil alunos.
            for dado in dados_alunos:
                while dado.get('ID') == numeroMatricula:
                    numeroMatricula = randint(20230000, 20240000)
                else:
                    dados_alunos[i]['ID'] = numeroMatricula

            with open(caminhoAluno, 'w', encoding='utf8') as arquivo:
                json.dump(dados_alunos, arquivo, ensure_ascii=False, indent=2, )

            print(quantidade_de_alunos, 'º ALUNO ADICIONADO AO SISTEMA.')

            resposta = str(input('DESEJA ADICIONAR MAIS ALUNOS?[S/N]: ').upper())
            if resposta == 'SIM' or resposta == 'S':
                os.system('cls')
                continue
            else:
                os.system('cls')
                loop = False
                break


def rem_Professor():
    i = 1
    print('LISTA DOS PROFESSORES: ')
    for valor in professores:
        print(f'DADOS DO {i}º PROFESSOR:')
        i += 1
        print(valor)
    id = int(input('Informe o ID do professor que deseja eliminar: '))
    for pessoa in professores:
        if pessoa['ID'] == id:
            pessoa.clear()
    print('Professor Eliminado!')


def rem_aluno():
    i = 1
    print('LISTA DOS ALUNOS: ')
    for valor in alunos:
        print(f'DADOS DO {i}º PROFESSOR:')
        i += 1
        print(valor)
    id = int(input('Informe o numero de matricula do aluno que desejas eliminar: '))
    for pessoa in alunos:
        if pessoa['ID'] == id:
            pessoa.clear()
    print('Aluno Removido!')


def consultar_Prof():
    i = int(1)
    for valor in professores:
        print(f'DADOS DO {i}º PROFESSOR:')
        i += 1
        print(valor)
        print('')


def consultar_aluno():
    k = 1
    for valor in alunos:
        print(f'DADOS DO {k}º ALUNO:')
        k += 1
        print(valor)
        print('')


def prencGerent():
    try:
        escolhaG = int(input('[1]- Entrar como Gerenciador\n[2]- Criar Gerenciador\nSUA ESCOLHA: '))
    except ValueError:
        print('ESCOLHA INESISTENTE!')
    else:
        if escolhaG == 1:
            usuarioG = input('NOME USUARIO: ')
            senhaG = input('SUA SENHA: ')
            if usuarioG.upper() == inf_Gerente['Nome_G'].upper() and senhaG == inf_Gerente['Palavra_P']:
                print(f'BEM VINDO GERENTE {usuarioG.upper()}.\n')

                # add inf. para adc professores e alunos
                print("++++++++" * 6)
                print('\t\tG E R E N C I A D O R _ M E N U')
                print("++++++++" * 6)
                try:
                    escolhaG2 = int(input('\n[1]- Adicionar professor ou aluno.\n[2]- Remover professor ou aluno.'
                                          '\n[3]- Ver lista de professores de alunos. SUA ESCOLHA: '))
                except ValueError:
                    print('ESCOLHA INESISTENTE!')
                else:
                    if escolhaG2 == 1:
                        try:
                            escolhaG3 = int(input('\n[1]- Adicionar Professor.\n[2]- Adicionar Aluno.\nSUA ESCOLHA: '))
                        except ValueError:
                            print('ESCOLHA INESISTENTE!')
                        else:
                            if escolhaG3 == 1:
                                add_Professor()

                            elif escolhaG3 == 2:
                                # meter codigo para add alunos
                                add_aluno()
                            else:
                                print('ESCOLHA INESISTENTE!')
                    elif escolhaG2 == 2:
                        try:
                            escolhaG4 = int(input('[1]- Remover Professor.\n[2]- Remover Aluno.\nSUA ESCOLHA: '))
                        except ValueError:
                            print('ESCOLHA INESISTENTE!')
                        else:
                            if escolhaG4 == 1:
                                # meter funcao com o codigo para remover prof.
                                rem_Professor()

                            elif escolhaG4 == 2:
                                # meter funcao com o codigo para remover aluno
                                rem_aluno()

                            else:
                                print('ESCOLHA INESISTENTE!')
                    elif escolhaG2 == 3:
                        try:
                            escolhaG5 = int(input('[1]- Ver lista dos Professor.\n[2]- Ver lista dos Aluno.\nSUA ESCOLHA: '))
                        except ValueError:
                            print('ESCOLHA INESISTENTE!')
                        else:
                            if escolhaG5 == 1:
                                # meter funcao com o cogido de consultar professores
                                consultar_Prof()

                            elif escolhaG5 == 2:
                                # meter codigo para consultar lista de alunos
                                consultar_aluno()

                            else:
                                print('ESCOLHA INESISTENTE.')
                    else:
                        print('ESCOLHA INESISTENTE!')
            else:
                print('NOME DO USUARIO OU SENHA ESTA ERRADA!')

        elif escolhaG == 2:
            usuarioG2 = input('INFORME O SEU NOME: ')
            senhaG2 = input('INFORME A SUA PASSE: ')
            inf_Gerente.update({'Nome_G': usuarioG2, 'Palavra_P': senhaG2})
            print(f'BEM VINDO GERENTE {usuarioG2.upper()}.\n')
    # aqui tem que ter opcao de add e remover alunos e professor.
