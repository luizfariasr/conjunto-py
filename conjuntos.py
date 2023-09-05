# Mini Projeto - Operações com Conjuntos

def execute_operations(filename):
    with open(filename, 'r') as file:
        num_operations = int(file.readline().strip())

        for _ in range(num_operations):
            operation = file.readline().strip()
            set1 = set(file.readline().strip().split(', '))
            set2 = set(file.readline().strip().split(', '))

            if operation == 'U':
                result = set1.union(set2)
                operation_name = 'União'
            elif operation == 'I':
                result = set1.intersection(set2)
                operation_name = 'Interseção'
            elif operation == 'D':
                result = set1.difference(set2)
                operation_name = 'Diferença'
            elif operation == 'C':
                result = {(x, y) for x in set1 for y in set2}
                operation_name = 'Produto cartesiano'

            print(f'{operation_name}: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {result}')

file_name = input('Digite o nome do arquivo (sem a extensão .txt): ')

# adiciona automaticamente a extensão .txt ao arquivo
file_name += '.txt'

execute_operations(file_name)