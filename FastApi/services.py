from pydantic import BaseModel

# Modelo Pydantic para os dados do usuário
class User(BaseModel):
    username: str
    email: str


db_users = {}


def create_user(user: User):
    user_id = len(db_users) + 1
    db_users[user_id] = user
    return user_id, user


def get_user(user_id: int):
    if user_id in db_users:
        return user_id, db_users[user_id]
    else:
        return None, {"error": "User ID not found"}
