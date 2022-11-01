exemplo: list[dict[str, int]] = [
{'Nome': 'q', 'ID': '1'}, {'Nome': 'a', 'ID': '1'}
]
#TESTE PARA LISTAR PESSOAS E ADD UM ID:
i = 1
n = 202201
for pessoa in exemplo:
    nome = str(input(f'{i} NOME: '))
    pessoa.update({'Nome': nome, 'ID': n})
    i += 1
    n += 1

print('LISTA_PESSOAS: ')
for pessoa in exemplo:
    print(pessoa)


k = int(input('Numero: '))
for pessoa in exemplo:
    if pessoa['ID'] == k:
        pessoa.clear()

print('LISTA_PESSOAS: ')
for pessoa in exemplo:
    print(pessoa)/

