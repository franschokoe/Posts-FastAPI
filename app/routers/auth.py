from fastapi import APIRouter , Depends , HTTPException , Response , status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas,models,utils,oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags=["Authentication"]
)


"""Login router for authentication""" 


@router.post("/login" , response_model= schemas.Token)
async def login(user_cred:OAuth2PasswordRequestForm = Depends() ,db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == user_cred.username).first()

    if not user :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail=f"Invalid Credentials")
    
    if not utils.verify_hashing(user_cred.password , user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="Invalid Credentials")
    
    # create a token
    access_token = oauth2.create_access_token(data={"user_id" : user.id})


    return {"access_token" : access_token , "token_type" : "bearer"}
