from typing import Protocol
from core.entity.user import User as UserDTO

class UserProtocol(Protocol):
    def persist(self, user) -> UserDTO:
        ...

    def update(self,username: str,data) -> None:
        ...
    
    def read_by_username(self,username: str) -> UserDTO | None:
        ...
    