from fastapi import FastAPI
import asyncio

app = FastAPI()

async def tarefa_lenta():
    await asyncio.sleep(4)
    return {'status': 'Concluído'}

@app.get("/ping")
async def ping():
    return {"ping": "pong"}

@app.get('/processar')
async def processar():
    res = await tarefa_lenta()
    return res