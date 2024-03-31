from fastapi import FastAPI
import uvicorn

from services import User, createUser, getUser

app = FastAPI()

# Endpoint para criar um novo usuário
@app.post("/create-user")
def createUserEndpoint(user: User):
    userId, userData = createUser(user)
    return {"userId": userId, "userData": userData}


# Endpoint para obter os dados de um usuário com base no ID
@app.get("/get-user/{userId}")
def getUserEndpoint(userId: int):
    userId, userData = getUser(userId)
    if userId is not None:
        return {"userId": userId, "userData": userData}
    else:
        return userData


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
