from ..database import get_db
from ..utils import hash_password

class UserRepository:
    def __init__(self):
        pass

    def create_user(self, user: dict) -> int:
        """Cria um novo usuário no banco de dados"""
        with get_db() as conn:
            cursor = conn.cursor()
            
            # Cria hash da senha
            password_hash = hash_password(user['password'])
            
            # Insere o usuário
            cursor.execute("""
                INSERT INTO users (name, email, password_hash)
                VALUES (?, ?, ?)
            """, (user['name'], user['email'], password_hash))
            
            user_id = cursor.lastrowid
            conn.commit()
            
            return user_id