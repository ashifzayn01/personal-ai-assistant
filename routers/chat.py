# from fastapi import APIRouter
# from pydantic import BaseModel

# from chat import chat_with_ai

# router = APIRouter()


# class ChatRequest(BaseModel):
#     message: str
    
# class ChatResponse(BaseModel):
#     response: str    


# @router.post("/chat")
# def chat(request: ChatRequest):
#     return chat_with_ai(request.message)

# we dont have credit so we are  creating response  by own 

from fastapi import APIRouter
from pydantic import BaseModel

from chat import chat_with_ai

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = chat_with_ai(request.message)

    return {
        "response": result
    }


