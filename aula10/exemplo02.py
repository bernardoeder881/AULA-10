#Cálculo de produtividade
#-------------------------

print('=== Cálculo de Produtividade ===')

for i in range(5):
    try:
        total_produzido = float(input('Valor total da venda: '))
        funcionarios = int(input('Total de Funcionários: '))

        media_por_funconario = total_produzido / funcionarios
        print(f'Media por funcionário: { media_por_funconario: .2f}')
    except ValueError:
        print ('Informe um número')
    except ZeroDivisionError:
        print ('Funcionário não pode ser Zero')
    except KeyboardInterrupt:
         print ('Teclado interrompido')