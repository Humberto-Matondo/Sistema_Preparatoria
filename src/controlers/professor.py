import sys
from pathlib import Path

from src.models.professor import professores

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


def prencProf():
    professor = input('NOME PROFESSOR: ').upper()
    senhaP = input('SUA SENHA: ')
    # vai ter que estar em um for para efetuar a busca
    i = int(0)
    for prof in professores:
        if professor == prof['Nome_P'].upper() and senhaP == prof['senhaP']:
            print(f'BEM VINDO PROFESSOR(a) {professor.upper()}.\n')
            i += 1
            break
    if i == 0:
        print('NOME DO USUARIO OU SENHA ESTA ERRADA!')

        # Aqui tem que ter opcao de ver lista de alunos, e atribuir notas
