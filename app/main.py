from fastapi import FastAPI

from app.domain.use_cases.create_user import CreateUserUseCase


app = FastAPI()


@app.get("/user")
async def get_user():
    use_case = CreateUserUseCase()
    user = use_case.execute(username="john_doe", email="john@example.com")
    return {"username": user.username, "email": user.email}
