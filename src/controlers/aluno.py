import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from src.models.aluno import alunos

def prencAluno():
    aluno1 = input('NOME DO ALUNO: ')
    senhaA = input('SUA SENHA: ')
    i = 0
    for aluno in alunos:
        if aluno1.upper() == aluno['Nome_A'].upper() and senhaA == aluno['senha_A']:
            print(f'BEM VINDO {aluno1.upper()}.\n')
            i+=1
            break
    if i == 0:
        print('NOME DO USUARIO OU SEJA ESTA ERRADA!')

    #Precisa ter opcao de consultar nota