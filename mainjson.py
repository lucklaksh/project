from fastapi import FastAPI

app = FastAPI()

@app.get('/json_data')
def index():
    return {'message':'Hello World !'}