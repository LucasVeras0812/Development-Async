import asyncio
from datetime import datetime

def log(msg):
    print(f'[{datetime.now().strftime('%H:%M:%S')}] {msg}', flush=True)

async def carregar_html():
    log('Carregando HTML...')
    await asyncio.sleep(1)
    log('✅ Terminado HTML')

async def carregar_css():
    log('Carregando CSS...')
    await asyncio.sleep(2)
    log('✅ Terminado CSS')

async def carregar_js():
    log('Carregando JavaScript...')
    await asyncio.sleep(2.5)
    log('✅ Terminado JavaScript')

async def carregar_imagens():
    log('Carregando imagens...')
    await asyncio.sleep(4)
    log('✅ Terminado imagens')

async def carregar_analytics():
    log('Carregando analytics...')
    await asyncio.sleep(2)
    log('✅ Terminado analytics')


async def main():
    #Criado variáveis separadas para cada tipo
    html = asyncio.create_task(carregar_html())
    css = asyncio.create_task(carregar_css())
    js = asyncio.create_task(carregar_js())
    imagens = asyncio.create_task(carregar_imagens())

    #Aguarda as tarefas necessárias para o analytics
    await html
    await css
    await js
    await imagens

    #Depois de carregar o  HTML, CSS e JS podemos carregar o analytics
    await carregar_analytics()

asyncio.run(main())
