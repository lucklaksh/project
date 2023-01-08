from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

# nothing will come in the request body
"""
@router.post('/new')
def create_blog():
    pass

"""

"""
class BlogModel(BaseModel):
    pass

@router.post('/new')
def create_blog(blog: BaseModel):
    return "Ok"
"""


class BlogModel(BaseModel):
    title : str
    content : str
    nb_comments : int
    published : Optional[bool]
    name : str

@router.post('/new')
def create_blog(blog: BlogModel):
    # return "Ok"
    # return blog
    return {"Data":blog}