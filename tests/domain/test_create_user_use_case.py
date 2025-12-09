from app.domain.use_cases.create_user import CreateUserUseCase


def test_create_user_returns_user_with_username_and_email():
    use_case = CreateUserUseCase()

    user = use_case.execute(username="john_doe", email="john@example.com")

    assert user.username == "john_doe"
    assert user.email == "john@example.com"
