from pydantic import BaseModel, EmailStr
from .events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: list[Event] ㅣ None = None
    
    
    
class UserSignIn(BaseModel):
    email: EmailStr
    password: str

