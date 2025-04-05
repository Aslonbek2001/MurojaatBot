TOKEN = "6739248690:AAGUyQf3BIGDqTuf3i185PQrHBrZrgk7RRM"


DB_USER = "myuser"
DB_PASSWORD = "mypassword"
DB_NAME = "murojaat"
DB_HOST = "localhost"
DB_PORT = "5432"


# DATABASE_URL = "sqlite+aiosqlite:///database.db"
DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


# 3 ta tilda 
# Statisika:
# Murojaatlar soni, Javob berilganlar soni, kimga nechta javob bergani haqida ma'lumot
