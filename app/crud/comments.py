from typing import Any, Dict, Optional, Union, List
from app.models.comments import Comments
from app.schemas.comments import CommentCreate, CommentUpdate
from app.crud.base import CRUDBase

class CRUDComment(CRUDBase[Comments, CommentCreate, CommentUpdate]):

    async def get_all(self, *, skip: int = 0, limit: int = 100) -> List[Comments]:
        return await Comments.all().offset(skip).limit(limit)

    async def get(self, *, commentID: str)-> Optional[Comments]:
        return await Comments.get(commentID=commentID)

    async def create(self, *, obj_in: CommentCreate) -> Comments:
        db_obj = await Comments.create(commentID=obj_in.commentID, 
        activity=obj_in.activity, comment_content=obj_in.comment_content, 
        date_create=obj_in.date_create, date_modified=obj_in.date_modified, 
        userID=obj_in.userID, cardID=obj_in.cardID)
        return db_obj 

    async def update(self, *, commentID: str, db_obj: Comments, obj_in: CommentUpdate) -> Comments:
        db_obj = await Comments.filter(commentID=commentID)
        obj_update = await db_obj.update(**db_obj.dict(exclude_unset=True))
        return obj_update

    async def remove(self, *, commentID: str) -> Comments:
        obj = await Comments.filter(commentID=commentID).delete()
        return obj

comments = CRUDComment(Comments)
        