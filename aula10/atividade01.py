saldo_inicial = 1000
saque = 0
def calc_saldo(a,b):
    n = a - b
    return n

try:
    saque = float(input(f'Seu saldo atual é de {calc_saldo(saldo_inicial,saque):.2f},\nInforme o valor deseja sacar: '))
except ValueError:
    print('Valor errado')
except KeyboardInterrupt:
    print('Operação cancelada')
else:
    if saque > saldo_inicial:
        print ('Saldo insuficiente!')
    elif saque <=2:
        print ('Saque precisa ser maior ou igual a R$ 2,00')
    else:
        print(f'Você sacou R${saque:.2f}')
        print(f'Saldo Atual é de R${calc_saldo(saldo_inicial,saque):.2f}')
finally:
    print(f'Operação finalizada!')