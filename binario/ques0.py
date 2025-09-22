import sys

try:
    intValor = int(input('\ndigite um numero inteiro: '))
except ValueError:
    sys.exit('valor invalido. porfavor, digite um numero inteiro')
except KeyboardInterrupt:
    sys.exit('\nprograma interrompido pelo usuario')    
except Exception as erro:
    sys.exit('erro inesperado: {erro}')
else:

    print(f'\n{intValor} em binario...: {bin(intValor)}\n')