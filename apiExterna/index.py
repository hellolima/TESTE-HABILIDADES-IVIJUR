from fastapi import FastAPI
from services import getPosts

app = FastAPI()

# Endpoint para obter os posts dos usuários
@app.get("/posts")
async def readPosts():
    posts = getPosts()
    return posts

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
