import sqlite3
import os
from contextlib import contextmanager
from datetime import datetime

# Configuração do banco de dados
DATABASE_PATH = "task_manager.db"

def get_connection():
    """Cria uma conexão com o banco SQLite"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Para retornar resultados como dicionários
    return conn

@contextmanager
def get_db():
    """Context manager para gerenciar conexões do banco"""
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()

def create_tables():
    """Cria todas as tabelas no banco de dados"""
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Tabela users
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Tabela projects
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            )
        """)
        
        # Tabela tasks
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                status TEXT DEFAULT 'todo' CHECK (status IN ('todo', 'doing', 'done')),
                due_date DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE
            )
        """)
        
        # Criar índices para melhor performance
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_email ON users (email)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_projects_user_id ON projects (user_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_tasks_project_id ON tasks (project_id)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks (status)")
        
        conn.commit()
        print("✅ Tabelas criadas com sucesso!")

def init_database():
    """Inicializa o banco de dados"""
    if not os.path.exists(DATABASE_PATH):
        print("🔄 Criando banco de dados...")
        create_tables()
    else:
        print("📁 Banco de dados já existe")

def reset_database():
    """Remove e recria o banco de dados (CUIDADO: apaga todos os dados!)"""
    if os.path.exists(DATABASE_PATH):
        os.remove(DATABASE_PATH)
        print("🗑️ Banco de dados removido")
    
    create_tables()
    print("🔄 Banco de dados recriado")

if __name__ == "__main__":
    # Executa quando o arquivo é chamado diretamente
    init_database()
