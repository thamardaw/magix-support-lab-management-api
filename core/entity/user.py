from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id : int
    usernamae : Optional[str] = None
    password : Optional[str] = None
    role: Optional[str] = None
    class Config():
        orm_mode = True