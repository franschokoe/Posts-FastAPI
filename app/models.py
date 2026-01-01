from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

# Tables for posts
class Post(Base):
    __tablename__ = "post"

    id = Column(Integer , primary_key=True , index=True , nullable=False)
    title = Column(String , nullable=False)
    content = Column(String , nullable=False)
    published = Column(Boolean , server_default='TRUE' , nullable=False)
    created_at = Column(TIMESTAMP(timezone=True) , nullable=False , server_default=text('now()'))
    owner_id = Column(Integer , ForeignKey("users.id" ,ondelete="CASCADE") ,nullable= False)
    owner = relationship("User")
    phonenumber = Column(String , nullable=False )
    
# Table for users
class User(Base):
    __tablename__ = "users"
    id = Column(Integer , nullable=False , primary_key=True)
    email = Column(String , nullable=False , unique=True)
    password = Column(String , nullable=False , )
    created_at = Column(TIMESTAMP(timezone=True) , nullable=False , server_default=text('now()'))


# Table for Likes/Votes
class Vote(Base):
    __tablename__ = "votes"
    user_id= Column(Integer , ForeignKey("users.id" ,ondelete="CASCADE" ) , primary_key=True)
    post_id = Column(Integer , ForeignKey("post.id" , ondelete="CASCADE") , primary_key=True)


# class Shared(Base):
#     __tablename__ = "shared"
