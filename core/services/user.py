from exceptions.http import INVALID_CREDENTIAL
from core.protocol.user import UserProtocol
from utils.hashing import Hash
from exceptions.http import BAD_REQUEST
from utils.JWTtoken import JWT
from schemas.user import User, ResetPassword
from schemas.token import Token, RefreshToken
from fastapi.security import OAuth2PasswordRequestForm

class UserService:
    def __init__(self,user_repo:UserProtocol) -> None:
        self.user_repo = user_repo

    def create_user(self,request:User) -> None:
        if not request.username:
            raise BAD_REQUEST("Username cannot be empty.")
        if len(request.password) < 6:
            raise BAD_REQUEST("Password have to contain at least 6 character.")
        user = self.user_repo.read_by_username(request.username)
        if user:
            raise BAD_REQUEST("Username already exist.")
        request.password = Hash.hash_password(request.password)
        self.user_repo.persist(request)
        return
    
    def reset_password(self,request:ResetPassword) -> None:
        if len(request.newPassword) < 6:
            raise BAD_REQUEST("Password have to contain at least 6 character.")
        user = self.user_repo.read_by_username(request.username)
        if not user:
            raise BAD_REQUEST("No matching username.")
        if not Hash.verify_password(request.oldPassword,user.password):
            raise BAD_REQUEST("Incorrect old password.")
        self.user_repo.update(user.username,{"password":Hash.hash_password(request.newPassword)})
        return

    def authenticate(self,request:OAuth2PasswordRequestForm) -> Token:
        user = self.user_repo.read_by_username(request.username)
        if not user:
            raise BAD_REQUEST("Invalid Credentials.")
        if not Hash.verify_password(request.password,user.password):
            raise BAD_REQUEST("Incorrect password.")
        access_token = JWT.create_access_token(
            data={"sub": user.username,"role":user.role}
        )
        refresh_token = JWT.create_refresh_token(
            data={"sub": user.username,"role":user.role}
        )
        return {"access_token": access_token, "token_type": "Bearer","refresh_token":refresh_token}

    def refresh_token(self,request:RefreshToken) -> Token:
        tokenData = JWT.verify_token(request.refresh_token)
        if tokenData.token_type == "access":
            raise INVALID_CREDENTIAL
        access_token = JWT.create_access_token(data={"sub": tokenData.username,"role":tokenData.role})
        refresh_token = JWT.create_refresh_token(data={"sub": tokenData.username,"role":tokenData.role})
        return {"access_token": access_token, "token_type": "Bearer","refresh_token":refresh_token}
    

   