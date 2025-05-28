import asyncio
from datetime import datetime

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)

async def carregar_cabecalho(nome):
    log(f'Carregando {nome}')
    await asyncio.sleep(4)
    log(f'Terminando {nome}')
    await asyncio.sleep(2)

async def carregar_conteudo(nome):
    await asyncio.sleep(6)
    log(f'Carregando {nome}')
    await asyncio.sleep(1)
    log(f'Terminando {nome}')

async def carregar_rodape(nome):
    await asyncio.sleep(9)
    log(f'Carregando {nome}')
    await asyncio.sleep(1)
    log(f'Terminando {nome}')

async def main():
    await asyncio.gather(
        carregar_cabecalho('cabeçalho'),
        carregar_conteudo('conteúdo'),
        carregar_rodape('rodapé')
    )

asyncio.run(main())