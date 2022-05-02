from time import sleep

print(' ' * 30, '=' * 80)
print('\n', ' ' * 30, 'Bem-Vindo a calculadora de IMC (Índice de Massa Corporal) e consumo de calorias!  \n')
print(' ' * 30, '=' * 30, '| \033[;1mLOGIN/CADASTRO\033[0;0m |', '=' * 30, '\n')
print(' ' * 30, 'Para fazer seu cadastro, crie um usuário e uma senha para acessar a calculadora!\n')

print(' ' * 30, end='')
user = input(' Crie um nome de usuário: ').strip()
print(' ' * 30, end='')
senha = input(' Crie uma senha: ').strip()

print('\n')
print(' ' * 30, end='')
user2 = input(' Digite seu nome de usuário cadastrado: ').strip()
print(' ' * 30, end='')
senha2 = input(' Digite sua senha cadastrada: ').strip()

cont = 1
cont2 = 4
while user2 != user or senha2 != senha:
    print('\n')
    print(' ' * 30, '\033[;1mSENHA E/OU USUÁRIO INVÁLIDO(S)!\033[0;0m\n\n')
    print(' ' * 30, f'Você possui mais {cont2} tentativa(s)!')
    print(' ' * 30, end='')
    user2 = input(' Digite seu nome de usuário cadastrado:').strip()
    print(' ' * 30, end='')
    senha2 = input(' Digite sua senha cadastrada:').strip()
    cont += 1
    cont2 -= 1
    if cont >= 5:
        break

if cont >= 5:
    print('\n')
    print(' ' * 30, end='')
    print(' 5 tentativas excedidas... SISTEMA ENCERRADO.')
    quit()

print('\n')
print(' ' * 30, end='')
print(' ENTRANDO.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)

print('\n\n', ' ' * 29, '=' * 27, '|\033[;1m CALCULADORA DE IMC\033[0;0m |', '=' * 27, '\n')

print(' ' * 30, 'Digite sua altura usando 2 casas decimais. Exemplo: 1.75\n')
print(' ' * 30, end='')
altura = float(input(' Informe sua altura: '))
print(' ' * 30, end='')
peso = float(input(' Informe o seu peso em Kg: '))

imc = (peso / altura ** 2)

m = ' '
pn = ' '
sp = ' '
o1 = ' '
o2 = ' '
o3 = ' '

if imc <= 18.5:
    m = '\033[1;93mx\033[0;0m'
elif 18.6 <= imc <= 24.9:
    pn = '\033[1;92mx\033[0;0m'
elif 15 <= imc <= 29.9:
    sp = '\033[1;93mx\033[0;0m'
elif 30 <= imc <= 34.9:
    o1 = '\033[1;91mx\033[0;0m'
elif 35 <= imc <= 39.9:
    o2 = '\033[1;91mx\033[0;0m'
elif imc >= 40:
    o3 = '\033[1;91mx\033[0;0m'

print('\n')
print(' ' * 30, end='')
print(f' Seu IMC é de: {imc:.1f}')

sleep(3)

tabelona = (f'                                                 |  [{m}] \033[1;93mMagreza\033[0;0m           |     < 18,5       |\n'
            f'                                                 |  [{pn}] \033[1;92mPeso Normal\033[0;0m       |   18,5 a 24,9    |\n'
            f'                                                 |  [{sp}] \033[1;93mSobre Peso\033[0;0m        |   25,0 a 29,9    |\n'
            f'                                                 |  [{o1}] \033[1;91mObesidade Grau 1\033[0;0m  |   30,0 a 34,9    |\n'
            f'                                                 |  [{o2}] \033[1;91mObesidade Grau 2\033[0;0m  |   35,0 a 39,9    |\n'
            f'                                                 |  [{o3}] \033[1;91mObesidade Grau 3\033[0;0m  |     > 40,0       |')

print(' ' * 65, end='')
print('TABELA IMC')
print(' ' * 50, end='')
print('-' * 44)
print(' ' * 49, end='')
print('|         ESTADO  ', end='')
print('       |       IMC        |')
print(' ' * 50, end='')
print('-' * 44)
print(tabelona)
print(' ' * 50, end='')
print('-' * 44)
print(' ' * 30, '\033[1;92mVERDE\033[0;0m = Estado Normal')
print(' ' * 30, '\033[1;93mAMARELO\033[0;0m = Estado Preocupante')
print(' ' * 30, '\033[1;91mVERMELHO\033[0;0m = Estado de Risco\n\n')

sleep(10)

print(' ' * 29, '=' * 30, '| \033[;1mCÁLCULO DE CALORIAS\033[0;0m |', '=' * 30, '\n\n')

print(' ' * 29, 'Nesta etapa serão necessárias algumas informações para fazer seu cálculo de calorias!')

print(' ' * 30, end='')
print('=' * 85)

print(' ' * 30, end='')
sexo = input('Informe seu sexo [M] ou [F]: ').upper().strip()
print(' ' * 30, end='')
idade = int(input('Informe sua idade: '))

if sexo == 'F':
    if 0 <= idade < 3:
        basal = (58.317 * peso) - 31.1
    elif 3 <= idade < 10:
        basal = (20.315 * peso) + 485.9
    elif 10 <= idade < 18:
        basal = (13.384 * peso) + 692.6
    elif 18 <= idade < 30:
        basal = (14.818 * peso) + 486.6
    elif 30 <= idade < 60:
        basal = (8.126 * peso) + 845.6
    elif idade >= 60:
        basal = (9.082 * peso) + 658.5

if sexo == 'M':
    if 0 <= idade < 3:
        basal = (59.512 * peso) - 30.4
    elif 3 <= idade < 10:
        basal = (22.706 * peso) + 504.3
    elif 10 <= idade <= 18:
        basal = (17.686 * peso) + 658.2
    elif 18 <= idade <= 30:
        basal = (15.057 * peso) + 692.2
    elif 30 <= idade <= 60:
        basal = (11.472 * peso) + 873.1
    elif idade >= 60:
        basal = (11.711 * peso) + 587.7

print('\n')
print(' ' * 30, end='')
print(f'Seu gasto calórico basal é de: {basal:.2f} calorias.\n\n')

sleep(2)

# adicionar refeições AQUI

print(' ' * 30, end='')
print('-' * 34, 'Atividade Física', '-' * 33)
print('\n')
print(' ' * 30, end='')
print('[1]Leve - Atividades do cotidiano')
print(' ' * 30, end='')
print('[2]Moderada - Atividades físicas praticadas em média 1 hora por dia')
print(' ' * 30, end='')
print('[3]Intensa - Atividades físicas praticadas 2 ou mais horas por dia')
print('\n')

print(' ' * 30, end='')
atividade = int(input('Informe seu fator de atividade física de acordo com os dados: '))

print(' ' * 30, end='')
peso_desejado = int(input('Digite o peso que gostaria de atingir: '))

if atividade == 1:
    calorias_total = basal * 1.55
elif atividade == 2:
    calorias_total = basal * 1.84
elif atividade == 3:
    calorias_total = basal * 2.2

if peso_desejado == peso:
    print(' ' * 30, end='')
    print(f' Sua quantidade de calorias necessárias para manter seu peso é de {calorias_total:.2f}')
elif peso_desejado < peso:
    calorias_emagrecer = calorias_total - (peso_desejado + 500)
    print(' ' * 30, end='')
    print(f'Sua quantidade de calorias necessárias para emagracer é {calorias_emagrecer:.2f}')
elif peso_desejado > peso:
    calorias_engordar = calorias_total + (peso_desejado + 500)
    print(' ' * 30, end='')
    print(f'Sua quantidade de calorias necessárias para engordar é {calorias_engordar:.2f}')
