from jose import JWTError , jwt
from datetime import datetime , timedelta
from . import schemas , models
from .database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends , HTTPException , status 
from fastapi.security import OAuth2PasswordBearer
# connections
from .config import settings
# Environment
# import os
# from dotenv import load_dotenv

# load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# SECRET_KEY 
SECRET_KEY = settings.secret_key
# ALGORITHM
ALGORITHM = settings.algorithm
# TIME OF EXPIRE
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data:dict):

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})

    encoded_jwt = jwt.encode(to_encode , SECRET_KEY , algorithm=ALGORITHM)
    return encoded_jwt

# VERIFYING THE JWT TOKEN
def verify_access_token(token:str , cred_exception):

    try:

        payload = jwt.decode(token , SECRET_KEY , algorithms=ALGORITHM)

        id: str = payload.get("user_id")

        if id is None:
            return cred_exception
        
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise cred_exception
    
    return token_data
    
def get_current_user(token:str = Depends(oauth2_scheme)  , db : Session = Depends(get_db)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,
                                          detail="Could not Validate" , 
                                          headers={"WWW-Authenticate" : "Bearer"}
                                          )
    
    token = verify_access_token(token , credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user