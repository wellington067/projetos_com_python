"""Desenvolva um código que simule uma eleição com três candidatos.
- candidato_X => 889
- candidato_Y => 847
- candidato_Z => 515
- branco => 0

O código deve perguntar se deseja finalizar a votação depois do voto.
Caso o número do voto não corresponda a nenhum candidato ou seja 
branco, ele deve ser tratado como nulo. Se for inserido um texto 
ao invés de número, o código deve retornar uma mensagem para votar novamente.

Quando a votação for finalizada, o código deverá mostrar o vencedor,
aquele com o maior número de votos e, também, a quantidade de votos de cada
candidato, os brancos e nulos """

print('==============================================')
print('                   ELEIÇÃO')
print('==============================================')
print()
print()


candidato_X=0
candidato_Y=0
candidato_Z=0
branco=0
nulo=0
x=0

for x in range(15):
    print('------------------------------')
    print('     candidato_X => 889')
    print('     candidato_Y => 847')
    print('     candidato_Z => 515')
    print('     branco => 0')
    print('------------------------------')
    print()
    
    try:
        voto=int(input("número do candidato: "))
        print()
    except:
        print()
        print('você não digitou um número, tente novamente.')
        print()
        print()
        continue
    
    print()
    print('digite [y] para comfirmar ou [n] para tentar novamente.')
    confirm = input()
    
    if confirm == 'y':
        print()
        print('voto comfirmado com sucesso!')
        print()
    elif confirm == 'n':
        continue
    else:
        print()
        print('caractere inválido, tente novamente.')
        continue
        
    
    
    if voto == 889:
        candidato_X = candidato_X + 1
    elif voto == 847:
        candidato_Y = candidato_Y + 1
    elif voto == 515:
        candidato_Z = candidato_Z + 1
    elif voto == 0:
        branco = branco + 1
    else:
        nulo = nulo + 1
       

print()
print()
print('==================================================')
print('             resultado da eleição')
print('')
print('          candidato_X --------------', candidato_X)
print('          candidato_Y --------------', candidato_Y)
print('          candidato_Z --------------', candidato_Z)
print('          branco -------------------', branco)
print('          nulo ---------------------', nulo)
print()
print()
if candidato_X > candidato_Y and candidato_X > candidato_Z:
    mais_votado ='candidato_X '
    print('o ganhador foi',mais_votado,'com',candidato_X,'votos.')
    
elif candidato_Y > candidato_X and candidato_Y > candidato_Z:
    mais_votado = 'candidato_Y'
    print('o ganhador foi',mais_votado,'com',candidato_Y,'votos.')
    
elif candidato_Z > candidato_Y and candidato_Z> candidato_X:
    mais_votado = 'candidato_Z'
    print('o ganhador foi',mais_votado,'com',candidato_Z,'votos.')
    
print('==================================================')



