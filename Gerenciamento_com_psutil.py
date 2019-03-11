#Matheus Moreira Peres Felippe
# TP 3 - Projeto de Bloco - Arquitetura de Computadores, Sistemas Operacionais e Redes
import psutil
import socket

cpu_percentual_uso_info = psutil.cpu_percent(interval=1)
cpu_nucleos_info = psutil.cpu_count(logical=False)
cpu_nucleos_info = psutil.cpu_count(logical=False)
cpu_tempo_processo_normal = psutil.cpu_times()
cpu_interrupcoes_info = psutil.cpu_stats( )
cpu_frequencia_info = psutil.cpu_freq()
memoria_info = psutil.virtual_memory()
memoria_swap_info = psutil.swap_memory( )
disco_info = psutil.disk_usage('.')
disco_entrada_saida_info = psutil.disk_io_counters()
disco_total = round(disco_info[0] / (1024 * 1024 * 1024))
disco_uso_porcentagem = (disco_info[3])
disco_disponivel = round(disco_info[2] / (1024 * 1024 * 1024))
hostname_info = socket.gethostname()
rede_info = socket.gethostbyname(hostname_info)
rede_estatisticas_info = psutil.net_io_counters()

flag = 9
print('Bem vindo ao monitoramento e análise do computador!')
print('Escolha a opção que deseja um relatório completo!!')
while flag != 0:
    print('\n')
    print('0 - SAIR')
    print('1 - Informações associadas ao Processador')
    print('2 - Informações associadas ao Memória')
    print('3 - Informações associadas ao Disco')
    print('4 - Informações associadas ao IP')
    print('5 - Deseja opter um resumo das estatísticas?')

    flag = int(input('Informe a opção desejada: '))
    if flag == 1:
        print('\n*** Informações sobre o PROCESSADOR *** \n')
        print(f'-Utilização atual da CPU {cpu_percentual_uso_info}%')
        print(f'-Número de núcleos físicos {cpu_nucleos_info}')
        print(f'-Tempo gasto pelos processos normais executados no modo de usuário {cpu_tempo_processo_normal[0]}')
        print(f'-Tempo gasto pelos processos em execução no modo kernel {cpu_tempo_processo_normal[2]}')
        print(f'-Tempo gasto sem fazer nada {cpu_tempo_processo_normal[2]}')
        print(f'-Número de interrupções desde a inicialização {cpu_interrupcoes_info[1]}')
        print(f'-Número de interrupções de software desde a inicialização {cpu_interrupcoes_info[2]}')
        print(f'-Número de chamadas do sistema desde a inicialização {cpu_interrupcoes_info[3]}')
        print(f'-Frequência atual {cpu_frequencia_info[0]} Mhz')
        print(f'-Frequência mínima {cpu_frequencia_info[1]} Mhz')
        print(f'-Frequência máxima {cpu_frequencia_info[2]} Mhz')

    elif flag == 2:
        print('\n *** Informações sobre o MEMÓRIA *** ')
        print('-Porcentagem do uso de memória: {} %'.format(memoria_info[2]))
        print(f'-Memória física total {memoria_info[0]}')
        print(f'-Memória física disponível {memoria_info[1]}')
        print(f'-Memória física usada {memoria_info[3]}')
        print(f'-Total de memória swap {memoria_swap_info[0]} bits')
        print(f'-Total de memória swap usado {memoria_swap_info[1]} bits')
        print(f'-Total memória de troca livre {memoria_swap_info[2]} bits')
        print(f'-Porcentagem do uso da memória swap {memoria_swap_info[3]} %')

    elif flag == 3:
        print('\n *** Informações sobre o DISCO *** ')
        print(f'-Tamanho do disco: {disco_total} GB')
        print(f'-Utilizado: {disco_uso_porcentagem} %')
        print(f'-Disponivel: {disco_disponivel} GB')
        print(f'-Número de leituras {disco_entrada_saida_info[0]} ')
        print(f'-Número de gravações {disco_entrada_saida_info[1]} ')
        print(f'-Número de bytes lidos {disco_entrada_saida_info[2]} ')
        print(f'-Número de bytes escritos {disco_entrada_saida_info[3]} ')
        print(f'-Tempo gasto lendo o disco {disco_entrada_saida_info[4]} milissegundos')
        print(f'-Tempo gasto escrevendo em disco {disco_entrada_saida_info[5]} milissegundos\n')

    elif flag == 4:
        print('\n *** Informações sobre a REDE *** ')
        print('-IP:', rede_info)
        print(f'-Número de bytes enviados {rede_estatisticas_info[0]} bits')
        print(f'-Número de bytes recebidos {rede_estatisticas_info[1]} bits')
        print(f'-Número de pacotes enviados {rede_estatisticas_info[2]} pacotes')
        print(f'-Número de pacotes recebidos {rede_estatisticas_info[3]} pacotes')
        print(f'-Número total de erros durante o recebimento {rede_estatisticas_info[4]} ')
        print(f'-Número total de erros durante o envio {rede_estatisticas_info[5]} ')
        print(f'-Número total de pacotes recebidos que foram descartados {rede_estatisticas_info[6]} ')
        print(f'-Número total de pacotes de saída que foram descartados {rede_estatisticas_info[7]} ')

    elif flag == 5:
        print('\n*** Processador ***')
        print('-Resumo das Estatísticas')
        print(f'-Utilização atual da CPU {cpu_percentual_uso_info}%')
        print(f'-Número de núcleos físicos {cpu_nucleos_info}')
        print('\n*** Memória ***')
        print('-Porcentagem do uso de memória: {} %'.format(memoria_info[2]))
        print(f'-Memória física total {memoria_info[0]}')
        print(f'-Memória física disponível {memoria_info[1]}')
        print(f'-Memória física usada {memoria_info[3]}')
        print('\n*** Disco ***')
        print(f'-Tamanho do disco: {disco_total} GB')
        print(f'-Utilizado: {disco_uso_porcentagem} %')
        print(f'-Disponivel: {disco_disponivel} GB')
        print('\n*** Rede ***')
        print('-IP:', rede_info)

    elif flag == 0:
        print('\nFim do Programa!')

    else:
        print('Opção invalida. Tente novamente!')
    print('============================================================================================================')
print('Obrigado por utilizar!')