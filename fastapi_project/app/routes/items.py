from fastapi import APIRouter
from app.db.database import database

router = APIRouter()

@router.get('/items')
async def listar_itens():
    query = 'SELECT * FROM items'
    return await database.fetch_all(query)

@router.post('/items')
async def criar_item(nome: str):
    query = 'INSERT INTO items(nome) VALUES (:nome)'
    await database.execute(query, {'nome': nome})
    return {'status': 'Item criado'}