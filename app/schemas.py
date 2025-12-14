from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict , EmailStr , Field , conint
from annotated_types import Le

# SCHEMAS FOR USERS

class CreateUser(BaseModel):
    email: EmailStr
    password : str
    # created_at: datetime


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        # orm_mode = True
        from_attribute = True

# Login

class UserLogin(BaseModel):
    email: EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type: str


class TokenData(BaseModel):

    id: Optional[int] = None

# Posts


class PostBase(BaseModel):
    title: str
    content : str
    published : bool = True
    phonenumber : str

class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at : datetime
    owner_id: int
    owner: UserResponse
    # title : str
    # content : str
    # published : bool

    class Config:
        # orm_mode = True
        from_attribute = True

class PostOut(BaseModel):
    Post : PostResponse  #Was supposed to use the Post as P capitals not lower case
    vote : int

    class Config:
        # orm_mode = True
        from_attribute = True
    # model_config = ConfigDict(from_attributes=True)
    # class Config:
    #     orm_mode  = True


# class Post(BaseModel):
#     title : str
#     content : str
#     published : bool = True

# class UpdatePost(BaseModel):
#     title : str
#     content : str
#     published : bool

# class CreatePost(BaseModel):
#     title : str
#     content : str
#     published : bool = True

# ForVote/Likes
class Vote(BaseModel):
    post_id: int
    dir: conint(le= 1) # type: ignore

