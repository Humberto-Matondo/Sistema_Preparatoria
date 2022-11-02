import sys
from pathlib import Path
from src.models.gerente import inf_Gerente
from src.models.aluno import alunos
from src.models.professor import professores

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

def add_Professor():
    i = 1
    for pessoa in professores:
        professor = str(input('Nome do Professor: '))
        senhaP = str(input('Senha do Professor: '))
        disc = str(input('Disciplina que Leciona: '))
        classe = int(input('A Classe que Leciona: '))

        pessoa.update({'Nome_P': professor, 'senhaP': senhaP, 'classe': classe, 'disciplina': disc, 'ID': i})
        i += 1
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
def add_aluno():
    i = 1
    numeroMatricula = 202201
    for aluno1 in alunos:
        nome = input('Nome do Aluno: ')
        idade = input('Sua idade: ')
        sexo = input('Seu Sexo: ')
        numBI = input('Numero do BI: ')
        ano = input('Ano Letivo: ')
        senhA = input('Digite a senha do aluno: ')
        aluno1.update(
            {'Nome_A': nome, 'Idade': idade, 'Sexo': sexo, 'N_Bi': numBI, 'Ano_Lectivo': ano, 'senha_A': senhA, 'ID': numeroMatricula})
        numeroMatricula += 1
        i += 1
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

               #add inf. para adc professores e alunos
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
                               #meter codigo para add alunos
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
                                #meter funcao com o codigo para remover prof.
                                rem_Professor()

                            elif escolhaG4 == 2:
                                #meter funcao com o codigo para remover aluno
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
                               #meter funcao com o cogido de consultar professores
                               consultar_Prof()

                           elif escolhaG5 == 2:
                               #meter codigo para consultar lista de alunos
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
    #aqui tem que ter opcao de add e remover alunos e professor.
