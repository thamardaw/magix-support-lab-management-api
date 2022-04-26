from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from infrastructure.session import get_db
from core.entity.user import User as UserDTO
from infrastructure.models.user import User

class UserRepository:
    def __init__(self,db:Session=Depends(get_db)):
        self._db = db

    def persist(self, user) -> UserDTO:
        new_user = User(**user.dict())
        self._db.add(new_user)
        self._db.flush()
        self._db.refresh(new_user)
        return UserDTO.from_orm(new_user)

    def update(self,username: str,data) -> None:
        user = self._db.query(User).filter(User.username == username)
        user.update(data)
        self._db.flush()
        return

    def read_by_username(self,username: str) -> UserDTO | None:
        user = self._db.query(User).filter(User.username == username).first()
        if user is None: return None
        return UserDTO.from_orm(user)
