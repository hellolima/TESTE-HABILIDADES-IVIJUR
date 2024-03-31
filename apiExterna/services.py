import requests

def getPosts():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()
        posts = response.json()
        return posts
    except requests.RequestException as e:
        raise RuntimeError(f"Erro ao obter os posts: {e}")
