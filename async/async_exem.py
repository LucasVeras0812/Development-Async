import asyncio

async def tarefa(nome):
    print(f'Iniciando {nome}')
    await asyncio.sleep(2)
    print(f'Finalizando {nome}')

async def main():
    await asyncio.gather(
        tarefa('A'),
        tarefa('B')
    )

asyncio.run(main())

#✅ Funções assíncronas só podem usar AWAIT dentro de outras funções ASYNC.
# async def minha_funcao():
#     await asyncio.sleep(1)

#❌ Erro COMUM
#def minha_funcao():
#    await asyncio.sleep(1)  # ERRO! 'await' fora de função async