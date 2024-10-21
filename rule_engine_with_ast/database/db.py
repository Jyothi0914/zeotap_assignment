import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    return conn

def store_rule(rule_string, ast):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO rules (rule_string, ast) VALUES (%s, %s)", 
                (rule_string, str(ast)))
    conn.commit()
    cur.close()
    conn.close()

def fetch_rule(rule_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT rule_string, ast FROM rules WHERE id = %s", (rule_id,))
    rule = cur.fetchone()
    cur.close()
    conn.close()
    return rule
