from app.domain.entities.user import User


class CreateUserUseCase:
    def execute(self, username: str, email: str) -> User:
        return User(username=username, email=email)
