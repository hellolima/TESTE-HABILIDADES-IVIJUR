from pydantic import BaseModel

# Modelo Pydantic para os dados do usuário
class User(BaseModel):
    username: str
    email: str


db_users = {}


def createUser(user: User):
    userID = len(db_users) + 1
    db_users[userID] = user
    return userID, user


def getUser(userID: int):
    if userID in db_users:
        return userID, db_users[userID]
    else:
        return None, {"error": "User ID not found"}
