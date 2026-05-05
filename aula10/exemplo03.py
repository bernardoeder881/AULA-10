
print('=== Cálculo de Produtividade ===')


try:
    total_produzido = float(input('Valor total da venda: '))
    funcionarios = int(input('Total de Funcionários: '))
    media_por_funconario = total_produzido / funcionarios
      
except (ValueError, TypeError):
      print ('Informe um número')
except ZeroDivisionError:
      print ('Funcionário não pode ser Zero')
except KeyboardInterrupt:
      print ('Operação cancelada')
else:
    print(f'Média por funcionário: {media_por_funconario:.2f}')
#Com erro ou não o bloco do finally sempre irá executar:?
finally:
     print('Programa encerrado!')    

