import time 

def tarefa(nome):
    print(f'Iniciando {nome}')
    time.sleep(2)
    print(f'Finalizando {nome}')

def main():
    tarefa('A')
    tarefa('B')

main()
