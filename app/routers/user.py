from fastapi import Depends , HTTPException , status , APIRouter
from .. import schemas , models
# for database
from sqlalchemy.orm import Session
from ..database import get_db
# for security
from .. import utils

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/" , status_code=status.HTTP_201_CREATED , response_model=schemas.UserResponse)
async def create_user(user : schemas.CreateUser ,db: Session = Depends(get_db)):
    # Hash password
    # hashed_password = pwd_context.hash(user.password)
    # user.password = hashed_password

    # hashed = password_hash.hash(user.password)
    # user.password = hashed

    new_pwd = utils.hashing_password(user.password)
    user.password = new_pwd

    # with the model of user from models.py
    new_user = models.User(**user.dict())

    # perfomming db actions
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}" , response_model=schemas.UserResponse)
async def get_user(id : int , db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="not found")
    
    return user