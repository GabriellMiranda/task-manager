
from common.services.users_service import UsersService
from common.schemas.users_schema import UserSchema


def handler(event, context):
    try:
        users_service = UsersService()
        user_data = UserSchema(**event)
        user_id = users_service.create_user(user_data.model_dump())
        
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": {
                "user_id": user_id,
                "message": "Usuário criado com sucesso"
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": {
                "error": str(e)
            }
        }

if __name__ == "__main__":
    user = {
        "name": "julia Silva",
        "email": "julia@email.com",
        "password": "senha123"
    }
    result = handler(user, None)
    print(f"✅ {result}")