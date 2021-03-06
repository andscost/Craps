#craps
import random 

jogo = True

valor = [0]*4


dado1 = 0
dado2 = 0

#iniciando o jogo
print('Bem Vindo ao Craps!')
dinheiro = int(input('Quanto dinheiro vc tem?: '))
while jogo == True:
    continuar_aposta = True
    mudar_de_fase = False
    print('Vc tem {0} ainda na sua conta'.format(dinheiro))
    jogar = input('Vc quer apostar(a) ou sair do jogo(s): ')
    if jogar == 's':
        jogo = False
    else: #inicio da rodada
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        fase = 'Come Out'
        #apostas em come out
        valor_total_apostas = 0
        while continuar_aposta == True:
            print('//////////////////////////////////')
            print('Vc está na fase '+fase)
            print('Os tipos de aposta disponiveis sao:\nPass line bet(plb)\nField(f)\nAny Craps(ac)\nTwelve(t) ')
            tipo_de_aposta = input('Que tipo de aposta vc gostaria de fazer?: ')
            valor_da_aposta = int(input('Quanto vc quer apostar em '+tipo_de_aposta+'?: '))
            print('//////////////////////////////////')
            valor_total_apostas += valor_da_aposta
            if valor_total_apostas > dinheiro:
                print("insira uma quantia dentro de seu orçamento para fazer uma aposta valida")
                valor_total_apostas -= valor_da_aposta
            elif tipo_de_aposta == 'plb':
                if valor_da_aposta != valor[0] and valor[0] != 0:
                    valor_total_apostas -= valor_da_aposta
                    dinheiro += valor[0]
                    valor[0] = 0
                    print('A aposta em '+tipo_de_aposta+' foi zerada, por favor preencha o valor novamente')   
                else:
                    valor[0] = valor_da_aposta
            elif tipo_de_aposta == 'f' :
                if valor_da_aposta <= valor[1] and valor[1] != 0:
                    valor_total_apostas -= valor_da_aposta
                    dinheiro += valor[1]
                    valor[1] = 0
                    print('A aposta em '+tipo_de_aposta+' foi zerada, por favor preencha o valor novamente')
                else:
                    valor[1] = valor_da_aposta
            elif tipo_de_aposta == 'ac':
                if valor_da_aposta <= valor[2] and valor[2] != 0:
                    valor_total_apostas -= valor_da_aposta
                    dinheiro += valor[2]
                    valor[2] = 0
                    print('A aposta em '+tipo_de_aposta+' foi zerada, por favor preencha o valor novamente')
                else:
                    valor[2] = valor_da_aposta
            elif tipo_de_aposta == 't':
                if valor_da_aposta <= valor[3] and valor[3] != 0:
                    valor_total_apostas -= valor_da_aposta
                    dinheiro += valor[3]
                    valor[3] = 0
                    print('A aposta em '+tipo_de_aposta+' foi zerada, por favor preencha o valor novamente')
                else:
                    valor[3] = valor_da_aposta
            else:
                print('favor, escolher uma aposta valida')
                valor_total_apostas -= valor_da_aposta
            print('Dinheiro disponivel: {0}\nValores das apostas:\nPass line bet: {1}\nField: {2}\nAny Craps: {3}\nTwelve: {4}'.format(dinheiro-valor_total_apostas, valor[0],valor[1],valor[2],valor[3])) 
            print('Vc pode mudar o valor de alguma aposta ou fazer apostas em outros tipos')
            nova_aposta = input('vc gostaria de fazer isso? (s/n): ')
            if nova_aposta == 'n':
                continuar_aposta = False
                dinheiro = dinheiro-valor[0]-valor[1]-valor[2]-valor[3]
        #rodada come out
        soma_dos_dados = dado1+dado2
        print('//////////////////////////////////')
        print('Dados foram jogados:\nDado1 = {0}\nDado2 = {1}\nSoma dos dados= {2}\n'.format(dado1,dado2,soma_dos_dados))
        #passlinebet
        if valor[0] > 0:
            if soma_dos_dados == 7 or soma_dos_dados == 11:
                print('ganhou {0} em pass line bet'.format(valor[0]))
                dinheiro = dinheiro+valor[0]*2
                valor[0] = 0
            elif soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12 :
                print('perdeu {0} em pass line bet'.format(valor[0]))
                valor[0] = 0
            else:
                print('as apostas do pass line bet foram para a fase Point')
                mudar_de_fase = True
        #field             
        if valor[1] > 0:
            if soma_dos_dados == 5 or soma_dos_dados == 6 or soma_dos_dados == 7 or soma_dos_dados == 8:
                print('perdeu {0} em field'.format(valor[1]))
            elif soma_dos_dados == 2:
                print('ganhou {0} em field'.format(valor[1]*2))
                dinheiro = dinheiro+valor[1]*3
            elif soma_dos_dados == 12:
                print('ganhou {0} em field'.format(valor[1]*3))
                dinheiro = dinheiro+valor[1]*4
            else:
                print('ganhou {0} em field'.format(valor[1]))
                dinheiro = dinheiro+valor[1]*2
            valor[1] = 0
        #anycraps
        if valor[2] > 0:
            if soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12 :
                print('ganhou {0} em anycraps'.format(valor[2]*7))
                dinheiro = dinheiro+valor[2]*8
            else:
                print('perdeu {0} em anycraps'.format(valor[2]))
            valor[2] = 0
        #twelve
        if valor[3] > 0:
            if soma_dos_dados == 12:
                print('ganhou {0} em twelve'.format(valor[3]*30))
                dinheiro = dinheiro+valor[3]*31
            else:
                print('perdeu {0} em twelve'.format(valor[3]))
            valor[3] = 0
        #point
        if mudar_de_fase == True:
            mudar_de_fase = False
            continuar_aposta = True
            fase = 'Point'
            #aposta fase point
            valor_total_apostas = 0
            while mudar_de_fase == False:
                while continuar_aposta:
                    print('//////////////////////////////////')
                    print('Vc está na fase '+fase)
                    print('total da aposta da fase Point: {0}'.format(valor_total_apostas))
                    print('Os tipos de aposta disponiveis sao:\nField(f)\nAny Craps(ac)\nTwelve(t) ')
                    tipo_de_aposta = input('Que tipo de aposta vc gostaria de fazer? (caso nao queira apostar, digite n): ')
                    if tipo_de_aposta == 'n':
                        continuar_aposta = False
                    else:
                        valor_da_aposta = int(input('Quanto vc quer apostar em '+tipo_de_aposta+'?: '))
                        print('total da aposta da fase Point: {0}'.format(valor_total_apostas))
                        print('valor da aposta escolhida: {0}'.format(valor_da_aposta))
                        valor_total_apostas += valor_da_aposta
                        print('aposta total: {0}'.format(valor_total_apostas))
                        print('//////////////////////////////////')
                        if valor_total_apostas > dinheiro:
                            print("insira uma quantia dentro de seu orçamento para fazer uma aposta valida")
                            valor_total_apostas -= valor_da_aposta
                        elif tipo_de_aposta == 'f':
                            if valor_da_aposta <= valor[1] and valor[1] != 0:
                                valor_total_apostas -= valor_da_aposta
                                dinheiro += valor[1]
                                valor[1] = 0
                                print('A aposta em '+tipo_de_aposta+' foi zerada, por favor preencha o valor novamente')
                            else:
                                valor[1] = valor_da_aposta
                        elif tipo_de_aposta == 'ac':
                            if valor_da_aposta <= valor[2] and valor[2] != 0:
                                valor_total_apostas -= valor_da_aposta
                                dinheiro += valor[2]
                                valor[2] = 0
                                print('A aposta em '+tipo_de_aposta+' foi zerada, por favor preencha o valor novamente')
                            else:
                                valor[2] = valor_da_aposta
                        elif tipo_de_aposta == 't':
                            if valor_da_aposta <= valor[3] and valor[3] != 0:
                                valor_total_apostas -= valor_da_aposta
                                dinheiro += valor[3]
                                valor[3] = 0
                                print('A aposta em '+tipo_de_aposta+' foi zerada, por favor preencha o valor novamente')
                            else:
                                valor[3] = valor_da_aposta
                        print('Dinheiro disponivel: {0}\nValores das apostas:\nPass line bet: {1}\nField: {2}\nAny Craps: {3}\nTwelve: {4}'.format(dinheiro-valor_total_apostas, valor[0],valor[1],valor[2],valor[3])) 
                        print('Vc pode mudar o valor de alguma aposta ou fazer apostas em outros tipos')
                        nova_aposta = input('vc gostaria de fazer isso? (s/n): ')
                        if nova_aposta == 'n':
                            continuar_aposta = False
                            dinheiro = dinheiro-valor[1]-valor[2]-valor[3]
                #fase point
                dado1 = random.randint(1,6)
                dado2 = random.randint(1,6)
                sdado_point = dado1+dado2  
                print('//////////////////////////////////')
                print('Dados foram jogados na fase Point:\nDado1 = {0}\nDado2 = {1}\nSoma dos dados= {2}\n'.format(dado1,dado2,sdado_point))
                print('Soma dos dados na fase Come Out: {0}'.format(soma_dos_dados))
                #field             
                if valor[1] > 0:
                    if soma_dos_dados == 5 or soma_dos_dados == 6 or soma_dos_dados == 7 or soma_dos_dados == 8:
                        print('perdeu {0} em field'.format(valor[1]))
                    elif soma_dos_dados == 2:
                        print('ganhou {0} em field'.format(valor[1]*2))
                        dinheiro = dinheiro+valor[1]*3
                    elif soma_dos_dados == 12:
                        print('ganhou {0} em field'.format(valor[1]*3))
                        dinheiro = dinheiro+valor[1]*4
                    else:
                        print('ganhou {0} em field'.format(valor[1]))
                        dinheiro = dinheiro+valor[1]*2
                    valor[1] = 0
                #anycraps
                elif valor[2] > 0:
                    if soma_dos_dados == 2 or soma_dos_dados == 3 or soma_dos_dados == 12 :
                        print('ganhou {0} em anycraps'.format(valor[2]*7))
                        dinheiro = dinheiro+valor[2]*8
                    else:
                        print('perdeu {0} em anycraps'.format(valor[2]))
                    valor[2] = 0
                #twelve
                elif valor[3] > 0:
                    if soma_dos_dados == 12:
                        print('ganhou {0} em twelve'.format(valor[3]*30))
                        dinheiro = dinheiro+valor[3]*31
                    else:
                        print('perdeu {0} em twelve'.format(valor[3]))
                    valor[3] = 0
                #pass line bet
                elif soma_dos_dados == sdado_point:
                    print('ganhou {0} em pass line bet'.format(valor[0]))
                    dinheiro = dinheiro+valor[0]*2
                    valor[0] = 0
                    mudar_de_fase = True
                elif sdado_point == 7:
                    print('perdeu {0} em pass line bet'.format(valor[0]))
                    valor[0] = 0
                    mudar_de_fase = True
                else:
                    print('vamos repetir a fase point')
    if dinheiro <= 0:
        jogo = False
print('obrigado por jogar! Volte sempre.')
