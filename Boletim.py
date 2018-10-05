# ---PAINEL-DE-CONTROLE---PAINEL-DE-CONTROLE---PAINEL-DE-CONTROLE---PAINEL-DE-CONTROLE---PAINEL-DE-CONTROLE---

# CONFIGURAÇÕES
media_anual_escola = 420
numero_materias = 14
media_por_materia = 70
comando_1 = 1
comando_2 = 2
limite_processos = 100
numero_sublinhas = 70
na = 'N/A'

# LINGUAGENS
port = [80, 80, 95, 84, na, na]
prodxt = [80, 70, 100, 80, na, na]
lit = [80, 60, 70, 84, na, na]
ing = [80, 62, 100, 84, na, na]
esp = [80, 65, 65, 84, na, na]

# HUMANAS
hist = [65, 85, 60, 80, na, na]
geog = [65, 80, 80, 80, na, na]
filo = [65, 82, 80, 80, na, na]
socio = [65, 75, 75, 80, na, na]

# EXATAS E BIO
mat = [70, 65, 100, 65, na, na]
fis = [95, 60, 55, 45, na, na]
quim = [95, 70, 80, 45, na, na]
bio = [95, 83, 80, 45, na, na]

# EDUCAÇÃO FÍSICA
edfis = [100, 80, 100, 70, na, na]

# LISTAS GERAIS
lista = [port, prodxt, lit, ing, esp, hist, geog, filo, socio, mat, fis, quim, bio, edfis]
materia = ['português', 'produção de texto', 'literatura', 'inglês', 'espanhol', 'história', 'geografia',
           'filosofia', 'sociologia', 'matemática', 'física', 'química', 'biologia', 'educação física']

# ======================================================================================================================
# ---ANIMAÇÃO-PRO-USUÁRIO---ANIMAÇÃO-PRO-USUÁRIO---ANIMAÇÃO-PRO-USUÁRIO---ANIMAÇÃO-PRO-USUÁRIO---ANIMAÇÃO-PRO-USUÁRIO---

from time import sleep

txt = {'clear': '\033[m',
       'red': '\033[31m',
       'blue': '\033[34m',
       'yellow': '\033[33m',
       'bold': '\033[1m',
       'underln': '\033[4m',
       'line': '-=-' * 31}

print('')
print('                                      {}M{}'.format(txt['bold'], txt['clear']), end='')
sleep(0.1)
print('{}E{}'.format(txt['bold'], txt['clear']), end='')
sleep(0.1)
print('{}U{}'.format(txt['bold'], txt['clear']), end=' ')
sleep(0.1)
print('{}B{}'.format(txt['bold'], txt['clear']), end='')
sleep(0.1)
print('{}O{}'.format(txt['bold'], txt['clear']), end='')
sleep(0.1)
print('{}L{}'.format(txt['bold'], txt['clear']), end='')
sleep(0.1)
print('{}E{}'.format(txt['bold'], txt['clear']), end='')
sleep(0.1)
print('{}T{}'.format(txt['bold'], txt['clear']), end='')
sleep(0.1)
print('{}I{}'.format(txt['bold'], txt['clear']), end='')
sleep(0.1)
print('{}M{}'.format(txt['bold'], txt['clear']))
sleep(0.1)

print(txt['line'])
print("""|                                                                                           |
|    \033[1;31m-LINGUAGENS-\033[m            \033[1;33m-HUMANAS-\033[m            \033[1;34m-EXATAS-\033[m            \033[1;35m-OUTRAS-\033[m              |
|    \033[31m1.português\033[m             \033[33m6.história\033[m           \033[34m10.matemática\033[m       \033[35m14.educação física\033[m    |
|    \033[31m2.produção de texto\033[m     \033[33m7.geografia\033[m          \033[34m11.física\033[m                                 |
|    \033[31m3.literatura\033[m            \033[33m8.filosofia\033[m          \033[34m12.química\033[m                                |
|    \033[31m4.inglês\033[m                \033[33m9.sociologia\033[m         \033[34m13.biologia\033[m                               |
|    \033[31m5.espanhol\033[m                                                                             |
|                                                                                           |""")
print(txt['line'])

# ======================================================================================================================
# ---PROCESSAMENTO---PROCESSAMENTO---PROCESSAMENTO---PROCESSAMENTO---PROCESSAMENTO---PROCESSAMENTO---PROCESSAMENTO---

sleep(0.75)
print('deseja ver todas as notas ou analisar uma matéria? ')
controle1 = int(input('1 [TODAS] / 2 [ANALISAR]: '))
print()

#----------------------------
# COMEÇO DO BOLTETIM COMPLETO
#----------------------------

if controle1 == comando_1:
    print('\033[1m=\033[m' * numero_sublinhas)
    print('-' * numero_sublinhas)
    for c in range(0, numero_materias):
        if lista[c][0] == na:
            a = txt['yellow']
        elif lista[c][0] >= media_por_materia:
            a = txt['blue']
        elif lista[c][0] < media_por_materia:
            a = txt['red']
        if lista[c][1] == na:
            b = txt['yellow']
        elif lista[c][1] >= media_por_materia:
            b = txt['blue']
        elif lista[c][1] < media_por_materia:
            b = txt['red']
        if lista[c][2] == na:
            d = txt['yellow']
        elif lista[c][2] >= media_por_materia:
            d = txt['blue']
        elif lista[c][2] < media_por_materia:
            d = txt['red']
        if lista[c][3] == na:
            e = txt['yellow']
        elif lista[c][3] >= media_por_materia:
            e = txt['blue']
        elif lista[c][3] < media_por_materia:
            e = txt['red']
        if lista[c][4] == na:
            f = txt['yellow']
        elif lista[c][4] >= media_por_materia:
            f = txt['blue']
        elif lista[c][4] < media_por_materia:
            f = txt['red']
        if lista[c][4] == na:
            g = txt['yellow']
        elif lista[c][4] >= media_por_materia:
            g = txt['blue']
        elif lista[c][4] < media_por_materia:
            g = txt['red']
        if lista[c][5] == na:
            if lista[c][4] == na:
                if lista[c][3] == na:
                    if lista[c][2] == na:
                        if lista[c][1] == na:
                               soma = lista[c][0]
                        else:
                            soma = lista[c][0] + lista[c][1]
                    else:
                        soma = lista[c][0] + lista[c][1] + lista[c][2]
                else:
                    soma = lista[c][0] + lista[c][1] + lista[c][2] + lista[c][3]
            else:
                soma = lista[c][0] + lista[c][1] + lista[c][2] + lista[c][3] + lista[c][4]
        else:
            soma = lista[c][0] + lista[c][1] + lista[c][2] + lista[c][3] + lista[c][4] + lista[c][5]
        if soma >= media_anual_escola:
            resul = ''
        else:
            resul = media_anual_escola - soma
        if soma >= media_anual_escola:
            op = ''
            cl = ''
            y = ''
            fal = ''
        else:
            fal = 'faltam'
            op = '('
            cl = ')'
            y = '\033[37m'
        print('\033[1m{}=>\033[m P1:{}{}{} P2:{}{}{} P3:{}{}{} P4:{}{}{} P5:{}{}{} P6:{}{}{} {}{}{}{}{}{}'.format(materia[c],
                                                                                     a, lista[c][0], txt['clear'],
                                                                                     b, lista[c][1], txt['clear'],
                                                                                     d, lista[c][2], txt['clear'],
                                                                                     e, lista[c][3], txt['clear'],
                                                                                     f, lista[c][4], txt['clear'],
                                                                                     g, lista[c][5], txt['clear'],
                                                                                     y, fal, op, resul, cl, txt['clear']))
        print('-' * numero_sublinhas)

# -------------------------------
# FIM DO BOLETIM COMPLETO
# ENTRANDO NO PROCESSO DE ANÁLISE
# PERMISSÃO PRA CICLO
# -------------------------------

    print('\033[1m=\033[m' * numero_sublinhas)
    print()
    sleep(1)
    print('deseja analisar uma matéria?')
    permição_repetição = int(input('1 [SIM] / 2 [NÃO]: '))
    if permição_repetição == comando_1:
            sleep(1.25)
            print()
    elif permição_repetição == comando_2:
        sleep(0.5)
        print('\033[1m=\033[m' * numero_sublinhas)
        print()
        print('\033[1;36mOBRIGADO POR LHE SER ÚTIL, MESTRE DO UNIVERSO\033[m')
        print()
        breakpoint()
    else:
        print('\033[1m*COMANDO INVÁLIDO*\033[m')
        breakpoint()

# ---------------------
#  PROCESSO DE ANÁLISE
# ---------------------

    for numero_processos in range(0, limite_processos):
        print()
        print('\033[1m=\033[m' * numero_sublinhas)
        subject = int(input('{}NÚMERO{} da matéria: '.format(txt['underln'], txt['clear'], txt['underln'], txt['clear'])))
        if subject < 1 or subject > numero_materias:
            print()
            print('\033[1m*NÚMERO INVÁLIDO*\033[m')
            breakpoint()
        else:
            print('{}{}=>{}'.format(txt['bold'], materia[subject-1], txt['clear']), end=' ')
            if lista[subject - 1][0] == na:
                a = txt['yellow']
            elif lista[subject - 1][0] >= media_por_materia:
                a = txt['blue']
            elif lista[subject - 1][0] < media_por_materia:
                a = txt['red']
            if lista[subject - 1][1] == na:
                b = txt['yellow']
            elif lista[subject - 1][1] >= media_por_materia:
                b = txt['blue']
            elif lista[subject - 1][1] < media_por_materia:
                b = txt['red']
            if lista[subject - 1][2] == na:
                c = txt['yellow']
            elif lista[subject - 1][2] >= media_por_materia:
                c = txt['blue']
            elif lista[subject - 1][2] < media_por_materia:
                c = txt['red']
            if lista[subject - 1][3] == na:
                d = txt['yellow']
            elif lista[subject - 1][3] >= media_por_materia:
                d = txt['blue']
            elif lista[subject - 1][3] < media_por_materia:
                d = txt['red']
            if lista[subject - 1][4] == na:
                e = txt['yellow']
            elif lista[subject - 1][4] >= media_por_materia:
                e = txt['blue']
            elif lista[subject - 1][4] < media_por_materia:
                e = txt['red']
            if lista[subject - 1][5] == na:
                f = txt['yellow']
            elif lista[subject - 1][5] >= media_por_materia:
                f = txt['blue']
            elif lista[subject - 1][5] < media_por_materia:
                f = txt['red']
            print('P1:{}{}{} P2:{}{}{} P3:{}{}{} P4:{}{}{} P5:{}{}{} P6:{}{}{}'.format(a, lista[subject - 1][0], txt['clear'],
                                                                                       b, lista[subject - 1][1], txt['clear'],
                                                                                       c, lista[subject - 1][2], txt['clear'],
                                                                                       d, lista[subject - 1][3], txt['clear'],
                                                                                       e, lista[subject - 1][4], txt['clear'],
                                                                                       f, lista[subject - 1][5], txt['clear'],))
        sleep(0.5)
        print('-' * numero_sublinhas)

# ---------------------------
# PONTOS FALNTANDO PRA MÉDIA
# ---------------------------

        if lista[subject-1][5] == na:
            if lista[subject-1][4] == na:
                if lista[subject-1][3] == na:
                    if lista[subject-1][2] == na:
                        if lista[subject-1][1] == na:
                            if lista[subject-1][0] == na:
                                print('{}NÃO HÁ NOTAS NESSA MATÉRIA{}'.format(txt['bold'], txt['clear']))
                        else:
                            total = lista[subject-1][0] + lista[subject-1][1]
                            (print('você precisa tirar \033[1m{}\033[m na 3,º 4º, 5º e 6º prova'.format((media_anual_escola - total) / 4)))
                    else:
                        total = lista[subject-1][0] + lista[subject-1][1] + lista[subject-1][2]
                        (print('você precisa tirar \033[1m{}\033[m na 4º, 5º e 6º prova'.format((media_anual_escola - total) / 3)))
                else:
                    total = lista[subject-1][0] + lista[subject-1][1] + lista[subject-1][2] + lista[subject-1][3]
                    (print('você precisa tirar \033[1m{}\033[m na 5º e 6º prova'.format((media_anual_escola - total) / 2)))
            else:
                total = lista[subject-1][0] + lista[subject-1][1] + lista[subject-1][2] + lista[subject-1][3] + lista[subject-1][4]
                print('você precisa tirar \033[1m{}\033[m na 6º prova'.format(media_anual_escola - total))
        print('-' * numero_sublinhas)

# ------------------
# CONTROLE DE CICLO
# ------------------

        sleep(1)
        print('deseja analisar outra matéria?')
        permição_repetição = int(input('1 [SIM] / 2 [NÃO]: '))
        if permição_repetição == comando_1:
                sleep(1)
                print('\033[1m=\033[m' * numero_sublinhas)
                sleep(0.25)
                print()
        elif permição_repetição == comando_2:
            sleep(0.5)
            print('\033[1m=\033[m' * numero_sublinhas)
            print()
            print('\033[1;36mOBRIGADO POR LHE SER ÚTIL, MESTRE DO UNIVERSO\033[m')
            breakpoint()
        else:
            print('\033[1m*COMANDO INVÁLIDO*\033[m')
            breakpoint()

# --------------------------------------------
# FIM DO CICLO
# ENTRANDO NO CICLO DE ESCOLHA DIRETA (opção2)
# --------------------------------------------

elif controle1 == comando_2:
    for numero_processos in range(0, limite_processos):
        print()
        print('\033[1m=\033[m' * numero_sublinhas)
        print('-' * numero_sublinhas)
        subject = int(input('{}NÚMERO{} da matéria: '.format(txt['underln'], txt['clear'], txt['underln'], txt['clear'])))
        if subject < 1 or subject > numero_materias:
            print()
            print('\033[1m*NÚMERO INVÁLIDO*\033[m')
            breakpoint()
        else:
            print('{}{}=>{}'.format(txt['bold'], materia[subject-1], txt['clear']), end=' ')
            if lista[subject - 1][0] == na:
                a = txt['yellow']
            elif lista[subject - 1][0] >= media_por_materia:
                a = txt['blue']
            elif lista[subject - 1][0] < media_por_materia:
                a = txt['red']
            if lista[subject - 1][1] == na:
                b = txt['yellow']
            elif lista[subject - 1][1] >= media_por_materia:
                b = txt['blue']
            elif lista[subject - 1][1] < media_por_materia:
                b = txt['red']
            if lista[subject - 1][2] == na:
                c = txt['yellow']
            elif lista[subject - 1][2] >= media_por_materia:
                c = txt['blue']
            elif lista[subject - 1][2] < media_por_materia:
                c = txt['red']
            if lista[subject - 1][3] == na:
                d = txt['yellow']
            elif lista[subject - 1][3] >= media_por_materia:
                d = txt['blue']
            elif lista[subject - 1][3] < media_por_materia:
                d = txt['red']
            if lista[subject - 1][4] == na:
                e = txt['yellow']
            elif lista[subject - 1][4] >= media_por_materia:
                e = txt['blue']
            elif lista[subject - 1][4] < media_por_materia:
                e = txt['red']
            if lista[subject - 1][5] == na:
                f = txt['yellow']
            elif lista[subject - 1][5] >= media_por_materia:
                f = txt['blue']
            elif lista[subject - 1][5] < media_por_materia:
                f = txt['red']
            print('P1:{}{}{} P2:{}{}{} P3:{}{}{} P4:{}{}{} P5:{}{}{} P6:{}{}{}'.format(a, lista[subject - 1][0], txt['clear'],
                                                                                       b, lista[subject - 1][1], txt['clear'],
                                                                                       c, lista[subject - 1][2], txt['clear'],
                                                                                       d, lista[subject - 1][3], txt['clear'],
                                                                                       e, lista[subject - 1][4], txt['clear'],
                                                                                       f, lista[subject - 1][5], txt['clear'],))

# ---------------------------
# PONTOS FALNTANDO PRA MÉDIA
# ---------------------------

        sleep(0.5)
        print('-' * numero_sublinhas)
        if lista[subject-1][5] == na:
            if lista[subject-1][4] == na:
                if lista[subject-1][3] == na:
                    if lista[subject-1][2] == na:
                        if lista[subject-1][1] == na:
                            if lista[subject-1][0] == na:
                                print('{}NÃO HÁ NOTAS NESSA MATÉRIA{}'.format(txt['bold'], txt['clear']))
                        else:
                            total = lista[subject-1][0] + lista[subject-1][1]
                            (print('você precisa tirar \033[1m{}\033[m na 3,º 4º, 5º e 6º prova'.format((media_anual_escola - total) / 4)))
                    else:
                        total = lista[subject-1][0] + lista[subject-1][1] + lista[subject-1][2]
                        (print('você precisa tirar \033[1m{}\033[m na 4º, 5º e 6º prova'.format((media_anual_escola - total) / 3)))
                else:
                    total = lista[subject-1][0] + lista[subject-1][1] + lista[subject-1][2] + lista[subject-1][3]
                    (print('você precisa tirar \033[1m{}\033[m na 5º e 6º prova'.format((media_anual_escola - total) / 2)))
            else:
                total = lista[subject-1][0] + lista[subject-1][1] + lista[subject-1][2] + lista[subject-1][3] + lista[subject-1][4]
                print('você precisa tirar \033[1m{}\033[m na 6º prova'.format(media_anual_escola - total))
        print('-' * numero_sublinhas)

# -------------------
# PERMISSÃO PRA CICLO
# -------------------

        sleep(1)
        print('deseja analisar outra matéria?')
        permição_repetição = int(input('1 [SIM] / 2 [NÃO]: '))
        if permição_repetição == comando_1:
                sleep(1)
                print('\033[1m=\033[m' * numero_sublinhas)
                sleep(0.25)
                print()
        elif permição_repetição == comando_2:
            sleep(0.5)
            print('\033[1m=\033[m' * numero_sublinhas)
            print()
            print('\033[1;36mOBRIGADO POR LHE SER ÚTIL, MESTRE DO UNIVERSO\033[m')
            print()
            breakpoint()
        else:
            print('\033[1m*COMANDO INVÁLIDO*\033[m')
            breakpoint()
else:
    print('\033[1m*COMANDO INVÁLIDO*\033[m')
    breakpoint()

