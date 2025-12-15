from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# for database
from .database import engine
from . import models
# routers
from .routers import post , user , auth ,vote

# models
"""Since we have the alembic and alembic autogenarate so the models are built"""
# models.Base.metadata.create_all(bind=engine)

app =  FastAPI()
@app.get("/")
async def root():
    return {"Posts" : "Social posts"}

# Implemanting CORS for app sharing data

origins = [
    # Links for other applications to connect with this 
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)
# Path for Posts
app.include_router(post.router)

# Path for users 
app.include_router(user.router)

# Path for Login
app.include_router(auth.router)

# Path for Votes/Likes
app.include_router(vote.router)











# How we get data from database using ORM
# @app.get("/sqlalchemy")
# async def test_post(db:Session = Depends(get_db)):

#     posts = db.query(models.Post).all()
#     return {"data" : posts}
