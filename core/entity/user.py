from pydantic import BaseModel

class User(BaseModel):
    id : int
    usernamae : str
    password : str
    role: str
    class Config():
        orm_mode = True