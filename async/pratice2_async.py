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
    log('Carregando HTML...')
    await asyncio.sleep(6)
    log('✅ Terminado analytics')


async def main():
    await asyncio.gather(
        carregar_html(),
        carregar_css(),
        carregar_js(),
        carregar_imagens(),
        carregar_analytics()
    )

asyncio.run(main())
