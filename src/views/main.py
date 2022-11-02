import sys
from pathlib import Path
from src.controlers.aluno import prencAluno
from src.controlers.professor import prencProf
from src.controlers.gerente import prencGerent

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


def menu():
    print("++++++++"*8)
    print('\t\tE S C O L A _ P R E P A R A T I A _ M E N U')
    print("++++++++"*8)
    print('Por Favor, Escolha uma das opcoes a baixo:')
    print('[1] - ENTRAR COMO GERENCIADOR. ')
    print('[2] - ENTRAR COMO PROFESSOR. ')
    print('[3] - ENTRAR COMO ALUNO. ')
    try:
        r = int(input('SUA ESCOLHA: '))
    except ValueError:
        print('ESCOLHA INESISTENTE!Por favor, volte a tentar.')
    return r

respFim = 'N'
while respFim.upper() == 'N':
    respInc = menu()
    if respInc == 1:
        print("++++++++" * 6)
        print('\t\tG E R E N C I A D O R _ M E N U')
        print("++++++++" * 6)
        prencGerent()

    elif respInc == 2:
        print("++++++++" * 6)
        print('\t\tP R O F E S S O R _ M E N U')
        print("++++++++" * 6)
        prencProf()

    elif respInc == 3:
        print("++++++++" * 6)
        print('\t\t\tA L U N O _ M E N U')
        print("++++++++" * 6)
        prencAluno()

    else:
        print('ESCOLHA INESISTENTE!Por favor, volte a tentar.')

    try:
        respFim = str(input('DESEJA TERMINAR O SISTEMA?[S/N]: '))
    except ValueError:
        print('ESCOLHA INESISTENTE!Por favor, volte a tentar.')



