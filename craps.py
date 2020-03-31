#craps
import random 

jogo = True
continuar_aposta = True
mudar_de_fase = False
#valor atribuido para cada tipo de aposta
valor_plb = 0
valor_f = 0
valor_ac = 0
valor_t = 0

dado1 = 0
dado2 = 0

#iniciando o jogo
print('Bem Vindo ao Craps!')
dinheiro = int(input('Quanto dinheiro vc tem?: '))
while jogo == True:
    print('Vc tem {0} ainda na sua conta'.format(dinheiro))
    jogar = input('Vc quer apostar(a) ou sair do jogo(s): ')
    if jogar == 's':
        jogo = False
    else: #inicio da rodada
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        print('//////////////////////////////////')
        fase = 'Come Out'
        #apostas em come out
        while continuar_aposta == True:
            print('Vc está na fase '+fase)
            print('Os tipos de aposta disponiveis sao:\nPass line bet(plb)\nField(f)\nAny Craps(ac)\nTwelve(t) ')
            tipo_de_aposta = input('Que tipo de aposta vc gostaria de fazer?: ')
            valor_da_aposta = int(input('Quanto vc quer apostar em '+tipo_de_aposta+'?: '))
            if valor_da_aposta > dinheiro:
                print("insira uma quantia dentro de seu orçamento para fazer uma aposta valida\ndinheiro disponivel: {0}".format(dinheiro))
            if tipo_de_aposta == 'plb':
                valor_plb = valor_da_aposta
            if tipo_de_aposta == 'f':
                valor_f = valor_da_aposta
            if tipo_de_aposta == 'ac':
                valor_ac = valor_da_aposta
            if tipo_de_aposta == 't':
                valor_t = valor_da_aposta
            print('Valores das apostas:\nPass line bet: {0}\nField: {1}\nAny Craps: {2}\nTwelve: {3}'.format(valor_plb,valor_f,valor_ac,valor_t))
            print('Dinheiro disponivel: {0}'.format(dinheiro-valor_plb-valor_f-valor_ac-valor_t))    
            print('Vc pode mudar o valor de alguma aposta ou fazer apostas em outros tipos')
            nova_aposta = input('vc gostaria de fazer isso? (s/n): ')
            if nova_aposta == 'n':
                continuar_aposta = False
            #rodada come out
            print('Dados foram jogados:\nDado1 = {0}\nDado2 = {1}'.format(dado1,dado2))
            soma_dos_dados = dado1+dado2
            if valor_plb > 0:
                if soma_dos_dados == 7 or soma_dos_dados == 11:
                    print('ganhou {0} em pass line bet'.format(valor_plb))
                    dinheiro = dinheiro+valor_plb
                if soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12 :
                    print('perdeu {0} em pass line bet'.format(valor_plb))
                    dinheiro = dinheiro-valor_plb
                else:
                    mudar_de_fase = True                
            #if valor_f > 0:
            #if valor_ac > 0:
            #if valor_t > 0:
    if dinheiro >= 0:
        jogo = False
print('obrigado por jogar! Volte sempre.')

