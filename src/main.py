from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379)

@app.get("/")
def read_root():
    return {"Hello": "World123"}


@app.get("/hist")
def read_root1():
    r.incr('hits')
    return {"Number of hits": r.get('hits')}