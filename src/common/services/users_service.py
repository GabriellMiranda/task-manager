from common.repositories.users_repository import UserRepository

class UsersService:
    def __init__(self):
        self.users_repository = UserRepository()

    def create_user(self, user: dict) -> int:
        user_id = self.users_repository.create_user(user)
        return user_id