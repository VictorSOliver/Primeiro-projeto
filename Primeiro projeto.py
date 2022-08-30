
def inicio(l):
    if l == '0':
        return 1
    return -1


def q1(l):
    if l == 'x' or l == 'X':
        return 2
    return -1


def q2(l):
    if l in alfabeto:
        return 3
    return -1


def final(l):
    if l in alfabeto:
        return 3
    return -1


alfabeto = ['a', 'b', 'c', 'd', 'e', 'f',
            'A', 'B', 'C', 'D', 'E', 'F',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
cadeia = str(input('Digite a cadeia: '))
dfa = 0

for letra in cadeia:
    if dfa == 0:
        dfa = inicio(letra)
    elif dfa == 1:
        dfa = q1(letra)
    elif dfa == 2:
        dfa = q2(letra)
    elif dfa == 3:
        dfa = final(letra)
    elif dfa == -1:
        break

if dfa == 3:
    print('\nCadeia aceita!')
else:
    print('\nCadeia não aceita!')