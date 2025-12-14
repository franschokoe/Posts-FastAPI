from fastapi import Depends , HTTPException , status , Response , APIRouter
from typing import List, Optional
# for database
from sqlalchemy.orm import Session
# To Work WIth SQL Functions
from sqlalchemy import func
from ..database import get_db
from .. import models ,schemas

from .. import oauth2


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

# @router.get("/" , response_model =List[schemas.PostResponse])
@router.get("/" , response_model =List[schemas.PostOut])
async def get_post(db: Session = Depends(get_db) , currrent_user: int = Depends(oauth2.get_current_user),
                    limit:int = 10 , skip:int = 0  , search: Optional[str] = ""):
    # For gertting your own posts
    # posts = db.query(models.Post).filter(models.Post.owner_id == currrent_user.id).all()

    """retriving all post"""
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    """Joining the Table"""
    results = db.query(models.Post , func.count(models.Vote.post_id).label("vote")).join(
                                            models.Vote, 
                                            models.Vote.post_id == models.Post.id,
                                            isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    if results != None:

        return results
    else: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="All post are not found")
    # if posts !=None:
    #     return posts

    # if results != None:
    #     return results
    # else:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="Error Occured")



# How we post/create data into the database
@router.post("/" , status_code=status.HTTP_201_CREATED , response_model=schemas.PostResponse)
async def create_post(post:schemas.PostCreate ,db: Session = Depends(get_db) ,currrent_user: int = Depends(oauth2.get_current_user)):

    """Makes the creation of the post to have user id"""
    new_post = models.Post(**post.dict() , owner_id = currrent_user.id)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return  new_post

# Get by id in sqlalchemy
@router.get("/{id}" , response_model=schemas.PostOut)
async def get_post(id: int,db: Session = Depends(get_db) , currrent_user: int = Depends(oauth2.get_current_user)):
    """Retriving by single user"""
    # post = db.query(models.Post).filter(models.Post.id == id).first()

    """Retriving after perfoming some Join innthe db"""
    results_query = db.query(models.Post , func.count(models.Vote.post_id).label("vote")).join(
                                            models.Vote, 
                                            models.Vote.post_id == models.Post.id,
                                            isouter=True).filter(models.Post.id == id).group_by(models.Post.id).first()


    if not results_query:
        raise HTTPException(status_code=404 , detail="Post not Found")
    

    return results_query


# delete in sqlalchemy

@router.delete("/{id}")
async def delete_post(id: int , db: Session = Depends(get_db) ,currrent_user: int = Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=404 , detail=f"Post with id: {id} does not exist")
    
    if post.owner_id != currrent_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="Not authorized to perfom")
    
    post.delete(synchronize_session = False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

    # MaY WAY ALSO WORK
    # deleted_post = db.query(models.Post).filter(models.Post.id == id).first()

    # db.delete(deleted_post)
    # db.commit()

    # if deleted_post == None:
    #     return {"data": "deleted"}


# UPDATING DATA INTO THE DATABASE

@router.put("/{id}")
async def update_post(id:int ,updated_post :schemas.PostCreate,  db : Session = Depends(get_db) , current_user: int = Depends(oauth2.get_current_user)):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None :
        raise HTTPException(status_code=404 , detail='Post not found')
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="Not authorized to perfom")
    

    post_query.update(updated_post.dict() , synchronize_session=False)

    db.commit()

    return post_query.first()