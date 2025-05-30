from databases import Database

DATABASE_URL = 'sqlite+aiosqlite:///./test.db'
database = Database(DATABASE_URL)