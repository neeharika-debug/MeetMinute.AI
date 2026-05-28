import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file automatically

DB_CONFIG = {
    'host':     'db.zdjedicrwyikxynnptvk.supabase.co',
    'port':     6543,
    'dbname':   'postgres',
    'user':     'postgres',
    'password': os.getenv('SUPABASE_PASSWORD')  # reads from .env
}

def get_db():
    return psycopg2.connect(**DB_CONFIG)

def get_cursor(conn):
    return conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)