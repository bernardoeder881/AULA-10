#calcula média de notas
#Não sabemos quantos alunos, mas todos terão notas sempre
def calcula_media(lista_notas):
    tot = sum(lista_notas)
    med = tot / len(lista_notas)
    return tot, med

contador = 1
while True:
    print(f'Aluno {contador}')
    aluno = input ('Nome do aluno: ')

    notas =[]
    try:
        for i in range(4):
            nota = float(input('informe a nota : '))
            notas.append(nota)
    
    except ValueError:
        print('Erro: Informe apenas valores válidos')
    else:
        total, media =calcula_media(notas)

        print('\nRESULTADO')
        print(f'Aluno:{aluno}')
        print(f'Total de pontos:{total}')
        print(f'Aluno:{media:.2f}')
    finally:
        print('Processo encerrado para o aluno')
    opcao = input ('Deseja calcular para outro aluno? ').strip().upper()
    if opcao != 'S':
        break
    contador +1
    
    

        
        
   

    