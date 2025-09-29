'''
   Exemplo 03 -  Calculando do endereço de rede a partir de um IP e CIDR
'''
# Define a variável 'strIP' com o endereço IP em formato de string 
# ('xxx.xxx.xxx.xxx')
strIP   = '192.168.1.10'
print(f'O Endereço IPv4 é...........................: {strIP}\n')

# Define a variável 'intCIDR' com o valor 24, que representa a quantidade 
# de bits da máscara de sub-rede (CIDR)
intCIDR = 24
print(f'Valor CIDR (bits na máscara)................: /{intCIDR}\n')

