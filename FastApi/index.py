from fastapi import FastAPI
import uvicorn

from services import User, create_user, get_user

app = FastAPI()

# Endpoint para criar um novo usuário
@app.post("/create-user")
def create_user_endpoint(user: User):
    user_id, user_data = create_user(user)
    return {"user_id": user_id, "user_data": user_data}


# Endpoint para obter os dados de um usuário com base no ID
@app.get("/get-user/{user_id}")
def get_user_endpoint(user_id: int):
    user_id, user_data = get_user(user_id)
    if user_id is not None:
        return {"user_id": user_id, "user_data": user_data}
    else:
        return user_data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
