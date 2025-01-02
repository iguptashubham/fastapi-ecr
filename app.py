from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn 
class response(BaseModel):
    question : str
    answer: str
    

app = FastAPI()

@app.post('/answer')
def get_answer(chat:response):
    question = chat.question
    answer = chat.answer
    return {'question':question,
            'answer':answer}
    
if __name__ == "__main__":
    uvicorn.run(app,port=8080)
